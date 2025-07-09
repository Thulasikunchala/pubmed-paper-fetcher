import argparse
from pubmed_paper_fetcher.core import fetch_papers, extract_paper_info, save_to_csv

def cli():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="Search query string")
    parser.add_argument("-d", "--debug", action="store_true", help="Print debug information")
    parser.add_argument("-f", "--file", type=str, help="CSV output filename")
    args = parser.parse_args()

    papers_raw = fetch_papers(args.query, debug=args.debug)
    papers_info = [extract_paper_info(p) for p in papers_raw if p.get("authors")]

    if args.file:
        save_to_csv(papers_info, args.file)
        print(f"Saved {len(papers_info)} results to {args.file}")
    else:
        for paper in papers_info:
            print(paper)

# IMPORTANT: Entry point must be named `main`
def main():
    cli()

if __name__ == "__main__":
    main()
