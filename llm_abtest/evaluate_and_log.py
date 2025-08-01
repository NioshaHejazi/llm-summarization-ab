import pandas as pd
import evaluate
import wandb

# Load data
df = pd.read_csv("manual_ratings_full.csv")

# Rename for easier access
df.rename(columns={
    "summary_t5": "t5_summary",
    "summary_bart": "bart_summary",
    "input_text": "article"
}, inplace=True)

# Load metrics
rouge = evaluate.load("rouge")
bert_score = evaluate.load("bertscore")

# Initialize W&B
wandb.init(project="llm-summarization-abtest", name="automatic_metrics")

# Evaluate and log
for model in ["t5", "bart"]:
    summaries = df[f"{model}_summary"].astype(str).tolist()
    references = df["article"].astype(str).tolist()

    rouge_result = rouge.compute(predictions=summaries, references=references)
    bert_result = bert_score.compute(predictions=summaries, references=references, lang="en")

    wandb.log({
        f"{model}_rouge1": rouge_result["rouge1"],
        f"{model}_rougeL": rouge_result["rougeL"],
        f"{model}_bert_score_precision": sum(bert_result["precision"]) / len(bert_result["precision"]),
        f"{model}_bert_score_recall": sum(bert_result["recall"]) / len(bert_result["recall"]),
        f"{model}_bert_score_f1": sum(bert_result["f1"]) / len(bert_result["f1"]),
    })

print("✅ Evaluation completed and logged to W&B.")
