import pandas as pd
import wandb

# Load the manual ratings CSV
df = pd.read_csv("manual_ratings.csv")

# Count each choice
counts = df["choice"].value_counts()
model_a_wins = counts.get("a", 0)
model_b_wins = counts.get("b", 0)
ties = counts.get("t", 0)
skips = counts.get("s", 0)

total_valid = model_a_wins + model_b_wins + ties

# Start wandb session
wandb.init(project="llm-summarization-abtest", name="manual_rating_analysis")

# Log metrics
if total_valid > 0:
    wandb.log({
        "model_a_wins": model_a_wins,
        "model_b_wins": model_b_wins,
        "ties": ties,
        "skips": skips,
        "model_a_win_rate": model_a_wins / total_valid,
        "model_b_win_rate": model_b_wins / total_valid,
        "tie_rate": ties / total_valid,
    })
else:
    print("⚠️ No valid votes (a/b/t) to analyze.")

# Optional: print to terminal
print("📊 Manual Rating Summary:")
print(counts)

wandb.finish()

