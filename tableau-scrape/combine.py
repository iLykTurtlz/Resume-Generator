import json
from constants import CS_EMPLOYMENT_COUNTS, CPE_EMPLOYMENT_COUNTS

with open("cs_companies.json", "r") as f:
    comps = json.load(f)
    final_json_cs = {}
    for i, comp in enumerate(comps):
        final_json_cs[comp] = CS_EMPLOYMENT_COUNTS[i] if i < len(CS_EMPLOYMENT_COUNTS) else 1
        
with open("cpe_companies.json", "r") as f:
    comps = json.load(f)
    final_json_cpe = {}
    for i, comp in enumerate(comps):
        final_json_cpe[comp] = CPE_EMPLOYMENT_COUNTS[i] if i < len(CPE_EMPLOYMENT_COUNTS) else 1
        
with open("cs_companies_with_counts.json", "w") as f:
    json.dump(final_json_cs, f, indent=4)
    
with open("cpe_companies_with_counts.json", "w") as f:
    json.dump(final_json_cpe, f, indent=4)