import json
import csv

with open("abtest_input.jsonl") as f:
    records = [json.loads(line) for line in f]

results = []
print("🔍 Beginning manual rating (T5 = a, BART = b, Tie = t, Skip = s):")

for r in records:
    print("\n" + "-" * 80)
    print(f"🔹 Article ID {r['id']}: {r['title']}")
    print("\n📄 ARTICLE (start):", r['article'][:600], "...\n")
    print("🅰️ T5 Summary:\n", r['t5_summary'])
    print("🅱️ BART Summary:\n", r['bart_summary'])

    while True:
        choice = input("\nWhich is better? [a = T5, b = BART, t = Tie, s = Skip]: ").strip().lower()
        if choice in ["a", "b", "t", "s"]:
            results.append({
                "id": r["id"],
                "title": r["title"],
                "choice": choice
            })
            break
        else:
            print("❌ Invalid choice. Try again.")

# Save ratings
with open("manual_ratings.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "title", "choice"])
    writer.writeheader()
    writer.writerows(results)

print("\n✅ All ratings saved to manual_ratings.csv")
