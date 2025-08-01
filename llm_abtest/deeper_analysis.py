# deeper_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import json
import wandb

# --- Load manual ratings ---
ratings_df = pd.read_csv("manual_ratings.csv")

# --- Load full summarization results ---
with open("summarization_results.json") as f:
    summary_data = json.load(f)

summary_df = pd.DataFrame(summary_data)

# --- Merge on 'id' ---
full_df = pd.merge(summary_df, ratings_df, on="id", how="inner")

# --- Save merged output ---
full_df.to_csv("manual_ratings_full.csv", index=False)
print("✅ Saved: manual_ratings_full.csv")

# --- Plot bar chart ---
counts = full_df["choice"].value_counts()
counts.plot(kind="bar", title="Manual Rating Counts")
plt.xlabel("Choice (a = T5, b = BART, t = Tie, s = Skip)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.close()
print("📊 Saved plot: rating_distribution.png")

# --- Log to wandb ---
wandb.init(project="llm-summarization-abtest", name="deeper_analysis")
wandb.log({
    "manual_rating_distribution": wandb.Image("rating_distribution.png")
})
wandb.finish()
