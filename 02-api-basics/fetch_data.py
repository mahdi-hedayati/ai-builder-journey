import json
import urllib.request

url = "https://api.adviceslip.com/advice"
request = urllib.request.Request(
    url,
    headers={"User-Agent": "ai-builder-journey/1.0"},
)

with urllib.request.urlopen(request, timeout=10) as response:
    data = json.load(response)

advice = data["slip"]["advice"]
advice_id = data["slip"]["id"]

print("Random advice")
print("-" * 40)
print(f"#{advice_id}: {advice}")
