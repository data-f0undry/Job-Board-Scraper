[![Run on Apify](https://img.shields.io/badge/Run%20on-Apify-141414?logo=apify&logoColor=white&labelColor=141414)](https://apify.com/data_foundry/job-board-scraper)

# Job Board Scraper

Open roles from 10 ATS career sites, with a diff of what opened and closed since the last run.

Companies publish their openings on their own career sites long before aggregators show them. This Actor finds the board for a company across 10 ATS platforms and returns every open role, then tells you what changed.

## Features

- 10 platforms: Greenhouse, Ashby, Lever, Workable, SmartRecruiters, Recruitee, Personio, Rippling, Breezy, Teamtailor
- Board discovery from the company slug - no URL needed
- Opened and closed roles per company since the last run
- Per-company isolation: one broken board never stops the run
- Webhook alerts, HMAC signed

## Usage

### Input

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `companies` | array | Company slugs, e.g. `stripe`, `ramp`. |
| `includeDescriptions` | boolean | Include full role description text. |
| `maxJobsPerCompany` | integer | Cap for very large boards. |
| `webhookUrl / webhookSecret` | string | Where to POST changes and the signing key. |
| `concurrency / timeoutSecs` | integer | Throughput and per-company budget. |

```json
{
  "companies": [
    "stripe",
    "ramp",
    "vercel"
  ]
}
```

### Output

```json
{
  "company": "ramp",
  "platform": "ashby",
  "title": "Revenue Operations Manager",
  "department": "Revenue",
  "location": "New York, NY",
  "url": "https://jobs.ashbyhq.com/ramp/..."
}
```

## Run it

**Apify Console** - open [data_foundry/job-board-scraper](https://apify.com/data_foundry/job-board-scraper), paste the input, click Start.

**API (Python)**

```bash
pip install apify-client
```

```python
from apify_client import ApifyClient

client = ApifyClient("<YOUR_API_TOKEN>")
run = client.actor("job-board-scraper").call(run_input={"companies": ["stripe", "ramp", "vercel"]})
for item in client.dataset(run["default_dataset_id"]).iterate_items():
    print(item)
```

**CLI**

```bash
apify call data_foundry/job-board-scraper --input-file input.json --output-dataset
```

Or run the included example: `python run_actor.py`.

## Pricing

**$10 per 1,000 companies scanned** ($0.01 each). Every role on the board is included.

You are not charged for the Apify platform usage, only for the events above. Failed items are not billed.

## Limitations

- The first run is a baseline.
- Discovery picks the largest matching board, so a namesake with one job does not win.
- Careers pages that are not on a supported ATS are out of scope.
- No LinkedIn, and no login of any kind.

These are documented deliberately: an Actor that hides its limits generates refund requests.

## Links

- [Actor on Apify](https://apify.com/data_foundry/job-board-scraper)
- [All Data Foundry Actors](https://apify.com/data_foundry)
- [Issues](https://github.com/data-f0undry/Job-Board-Scraper/issues)

## License

Apache-2.0. See [LICENSE](LICENSE).
