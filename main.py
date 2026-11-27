import requests
import os
import argparse


API_URL = "https://api.restcountries.com/countries/v5"  # Replace with your chosen API endpoint

def fetch_data():
    """Fetch data from the API. Returns the raw JSON response, or an empty list on failure."""
    API_KEY = os.environ.get("REST_COUNTRIES_API_KEY")
    if not API_KEY:
        print("No API key found. Set REST_COUNTRIES_API_KEY and try again.")

    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(API_URL, headers=headers)
        response.raise_for_status()
        return response.json()["data"]["objects"]
    except requests.exceptions.RequestException as e:
        print(f"Error could not fetch data: {e}")
        return []

def process_data(records):
    """Extract and transform the fields you need. Returns a list of dictionaries."""
    country_code_dict = {record.get("codes", {}).get("alpha_3"):
                        record.get("names", {}).get("common","Unknown")
                        for record in records}
    results = []
    for record in records:
        results.append({
            "name": record.get("names", {}).get("common","Unknown"),
            "region": record.get("region", "Unknown"),
            "languages": [lang["name"] for lang in record.get("languages", [])],
            "borders": [country_code_dict.get(code,code)
                for code in record.get("borders", [])] or "None",
            "code": record.get("codes", {}).get("alpha_3", "Unknown") or "None",
        })
    return results

def language_set(results):
    return sorted({language.title() for record in results
                         for language in record["languages"]})

def display_by_language(results, language):
    print(f"\nCountries where {language} is spoken:")
    for country in results:
        if language in country["languages"]:
            print(f"{country["name"]}"
                f"\n\tRegion: {country["region"]}"
                f"\n\tBorders: {", ".join(country["borders"])}"
                f"\n\tOfficial Languages: {", ".join(country["languages"])}")
            
def main():    
    data = fetch_data()
    results = process_data(data)
    if not results:
        print("No data returned.")
        return
    else:
        print(f"Fetched {len(results)} records.")
    
    parser = argparse.ArgumentParser(description="Query country data by language.")
    parser.add_argument("language", type=str.title, choices=language_set(results), help=f"Choose a language.")
    args = parser.parse_args()

    display_by_language(results, args.language)

    # while True:
    #     language = input(f"Filter countries by language. Available languages: {", ".join(language_set(results))}"
    #                      "\nChoose an available language: ").title()
    #     if not language:
    #         print(f"\nPlease enter a value.\n")
    #     elif language in (language_set(results)):
    #         display_by_language(results, language)
    #         return
    #     else:
    #         print(f"\nNot an available language. Try again.\n")
             
if __name__ == "__main__":
    main()
