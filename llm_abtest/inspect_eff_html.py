# save as inspect_eff_html.py
import requests

res = requests.get("https://www.eff.org/deeplinks", headers={"User-Agent": "Mozilla/5.0"})
with open("eff_raw.html", "w", encoding="utf-8") as f:
    f.write(res.text)

print("✅ Saved raw HTML to eff_raw.html")
