"""Python - official apify-client."""
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("data_foundry/job-board-scraper").call(run_input={
    "companies": [
        "stripe",
        "ramp",
        "vercel"
    ]
})
print("dataset:", run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)
