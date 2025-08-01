import json

# Load your summarization results
with open("summarization_results.json") as f:
    data = json.load(f)

# Build abtest_input.jsonl
with open("abtest_input.jsonl", "w") as out:
    for i, row in enumerate(data):
        record = {
            "id": i + 1,
            "title": row.get("title", "Untitled"),
            "article": row["input_text"],
            "t5_summary": row["summary_t5"],
            "bart_summary": row["summary_bart"]
        }
        out.write(json.dumps(record) + "\n")

print("✅ abtest_input.jsonl created.")
