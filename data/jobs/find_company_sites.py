from googlesearch import search
import json

def find_company_page(company_name, num_results=1):
    try:
        query = f"{company_name} official site"
        results = list(search(query, num_results=num_results, lang="en"))
        return results[0] if results else None
    except Exception as e:
        print(f"Error searching for {company_name}: {e}")
        return None

if __name__ == "__main__":
    with open("matched_companies.json", "r") as f:
        companies = json.load(f)
    
    company_pages = {}

    for company in companies:
        print(f"Searching for {company}...")
        main_page = find_company_page(company)
        company_pages[company] = main_page

    with open("company_main_pages.json", "w", encoding="utf-8") as json_file:
        json.dump(company_pages, json_file, indent=4)