# PubMed Paper Fetcher

A Python CLI tool to search PubMed, extract research articles, **filter for non-academic authors**, and export results to CSV.  
Ideal for researchers, pharma companies, or data analysts looking for **industry-authored publications**.

---

## Project Overview

PubMed contains millions of biomedical papers — but it’s hard to filter for authors from **non-academic institutions** (like pharmaceutical/biotech companies).  
This tool solves that.

You enter a search term (e.g., `"cancer AND immunotherapy"`), and it will:
- Query PubMed using the E-Utilities API
- Retrieve the latest 20 papers
- Identify **non-academic authors** based on their affiliation
- Export the filtered results to a CSV file

---

## Features

✅ Keyword-based PubMed search  
✅ Filters out universities, colleges, hospitals, etc.  
✅ Extracts authors, affiliations, publication date, email  
✅ Saves clean, structured output to `.csv`  
✅ Command-line friendly  
✅ Built with `requests`, `tqdm`, `Poetry`, and `Typer`

---

## Technologies Used

| Tool         | Purpose                        |
|--------------|--------------------------------|
| Python 3.10+ | Programming language           |
| Poetry       | Dependency + project manager   |
| Requests     | HTTP requests to PubMed API    |
| TQDM         | Progress bar for fetching data |
| Typer        | Building the CLI interface     |
| Git & GitHub | Version control                |

---

## Installation

```bash
# Clone the repo
git clone https://github.com/Thulasikunchala/pubmed-paper-fetcher.git
cd pubmed-paper-fetcher

# Install dependencies
python -m poetry install
l



