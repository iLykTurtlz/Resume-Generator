import pandas as pd
import json
from sentence_transformers import SentenceTransformer, util
from tqdm import tqdm

with open("cpe_companies_with_counts.json", "r") as cpe_file:
    cpe_companies = set(json.load(cpe_file).keys())

with open("cs_companies_with_counts.json", "r") as cs_file:
    cs_companies = set(json.load(cs_file).keys())

with open("job_titles.json", "r") as f:
    jobs = json.load(f)

all_companies = cpe_companies.union(cs_companies)
postings = pd.read_csv("postings.csv")

model = SentenceTransformer("all-MiniLM-L6-v2")
job_embeddings = {job: model.encode(job, convert_to_tensor=True) for job in jobs}

def semantic_match(title, threshold=0.7):
    if not isinstance(title, str):
        return False
    title_embedding = model.encode(title, convert_to_tensor=True)
    for job, job_embedding in job_embeddings.items():
        similarity = util.cos_sim(title_embedding, job_embedding).item()
        if similarity >= threshold:
            return True
    return False

tqdm.pandas(desc="Processing job titles")
postings["title_matches"] = postings["title"].progress_apply(semantic_match)

filtered_postings = postings[
    postings["company_name"].isin(all_companies) & postings["title_matches"]
]

matched_companies = filtered_postings["company_name"].dropna().unique().tolist()
filtered_postings.to_csv("filtered_postings.csv", index=False)

with open("matched_companies.json", "w") as match_file:
    json.dump(matched_companies, match_file, indent=4)

print("Filtered postings saved to 'filtered_postings.csv'.")
print("Matched companies saved to 'matched_companies.json'.")
