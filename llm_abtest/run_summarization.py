import json
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from tqdm import tqdm

# Load the dataset
with open("eff_blogs.json", "r", encoding="utf-8") as f:
    docs = json.load(f)

# Model A: T5
tokenizer_t5 = AutoTokenizer.from_pretrained("t5-small")
model_t5 = AutoModelForSeq2SeqLM.from_pretrained("t5-small")
pipe_t5 = pipeline("summarization", model=model_t5, tokenizer=tokenizer_t5)

# Model B: BART
tokenizer_bart = AutoTokenizer.from_pretrained("facebook/bart-base")
model_bart = AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-base")
pipe_bart = pipeline("summarization", model=model_bart, tokenizer=tokenizer_bart)

results = []

for item in tqdm(docs, desc="Summarizing..."):
    text = item["text"]

    # Truncate to ~1024 tokens for speed/safety
    input_text = text.strip().replace("\n", " ")[:2000]

    # T5 Prompt
    t5_input = "summarize: " + input_text
    t5_summary = pipe_t5(t5_input, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]

    # BART Prompt
    bart_input = "Summarize this article:\n" + input_text
    bart_summary = pipe_bart(bart_input, max_length=100, min_length=30, do_sample=False)[0]["summary_text"]

    results.append({
        "id": item["id"],
        "title": item["title"],
        "url": item["url"],
        "input_text": input_text,
        "summary_t5": t5_summary,
        "summary_bart": bart_summary
    })

# Save A/B test results
with open("summarization_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print("✅ Summarization complete. Results saved to summarization_results.json")
