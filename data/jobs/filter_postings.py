import pandas as pd
import json

# Load JSON files
with open("cpe_companies_with_counts.json", "r", encoding="utf-8") as cpe_file:
    cpe_companies = set(json.load(cpe_file).keys())

with open("cs_companies_with_counts.json", "r", encoding="utf-8") as cs_file:
    cs_companies = set(json.load(cs_file).keys())

all_companies = cpe_companies.union(cs_companies)

postings = pd.read_csv("postings.csv")
filtered_postings = postings[postings["company_name"].isin(all_companies)]
matched_companies = filtered_postings["company_name"].dropna().unique().tolist()
filtered_postings.to_csv("filtered_postings.csv", index=False)

with open("matched_companies.json", "w", encoding="utf-8") as match_file:
    json.dump(matched_companies, match_file, indent=4)

print("Filtered postings saved to 'filtered_postings.csv'.")
print("Matched companies saved to 'matched_companies.json'.")
