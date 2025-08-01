import json
import csv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load data
with open("summarization_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

rows = []

for item in data:
    t5_summary = item["summary_t5"]
    bart_summary = item["summary_bart"]
    input_text = item["input_text"]

    # Metrics
    t5_len = len(t5_summary.split())
    bart_len = len(bart_summary.split())

    embeddings = embedder.encode([input_text, t5_summary, bart_summary])
    sim_t5_input = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    sim_bart_input = cosine_similarity([embeddings[0]], [embeddings[2]])[0][0]
    sim_t5_bart = cosine_similarity([embeddings[1]], [embeddings[2]])[0][0]

    rows.append({
        "id": item["id"],
        "title": item["title"],
        "url": item["url"],
        "t5_length": t5_len,
        "bart_length": bart_len,
        "sim_t5_input": sim_t5_input,
        "sim_bart_input": sim_bart_input,
        "sim_t5_bart": sim_t5_bart,
        "t5_summary": t5_summary,
        "bart_summary": bart_summary
    })

# Write to CSV
with open("evaluation_results.csv", "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = list(rows[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print("✅ Results exported to evaluation_results.csv")
