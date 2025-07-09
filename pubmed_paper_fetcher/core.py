import requests
from typing import List, Dict, Tuple
import csv
import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "institute", "college", "school", "hospital", "center", "centre"]
    return all(kw.lower() not in affiliation.lower() for kw in academic_keywords)

def extract_paper_info(paper: Dict) -> Tuple[str, str, str, List[str], List[str], str]:
    pmid = paper.get("uid", "")
    title = paper.get("title", "")
    pub_date = paper.get("pubdate", "")
    authors = paper.get("authors", [])

    non_academic_authors = []
    company_affiliations = []
    email = ""

    for author in authors:
        affil = author.get("affiliation", "")
        name = author.get("name", "")
        if affil and is_non_academic(affil):
            non_academic_authors.append(name)
            company_affiliations.append(affil)
        if not email:
            email_match = re.search(r"[\w.+-]+@[\w-]+\.[\w.-]+", affil)
            if email_match:
                email = email_match.group(0)

    return pmid, title, pub_date, non_academic_authors, company_affiliations, email

def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "retmode": "json",
        "term": query,
        "retmax": 20,
    }
    ids_response = requests.get(url, params=params)
    ids = ids_response.json().get("esearchresult", {}).get("idlist", [])

    if debug:
        print(f"Fetched {len(ids)} paper IDs")

    fetch_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    fetch_params = {
        "db": "pubmed",
        "retmode": "json",
        "id": ",".join(ids)
    }
    summary_response = requests.get(fetch_url, params=fetch_params)
    return list(summary_response.json().get("result", {}).values())[1:]  # skip 'uids'

def save_to_csv(papers: List[Tuple], filename: str):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["PubmedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)", "Corresponding Author Email"])
        for row in papers:
            writer.writerow([
                row[0], row[1], row[2],
                "; ".join(row[3]),
                "; ".join(row[4]),
                row[5]
            ])
