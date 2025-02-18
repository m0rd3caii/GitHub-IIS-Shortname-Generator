import requests
import json
from pathlib import Path
import time
import sys
import argparse

class GitHubNameSearcher:
    def __init__(self):
        self.base_url = "https://api.github.com/search/code"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            # Add your GitHub token here if you have one
            "Authorization": "token YOUR_GITHUB_TOKEN"
        }

    def search_files(self, partial_name):
        """
        Search GitHub for files containing the partial name
        """
        query = f"filename:{partial_name}"
        params = {
            "q": query,
            "per_page": 100
        }

        try:
            response = requests.get(
                self.base_url,
                headers=self.headers,
                params=params
            )
            
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                print("Rate limit exceeded. Please wait or use a GitHub token.")
                return None
            else:
                print(f"Error: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"Error performing search: {str(e)}")
            return None

    def process_results(self, results, output_file=None):
        """
        Process and display search results, optionally saving to a file
        """
        if not results or 'items' not in results:
            return

        unique_names = set()
        for item in results['items']:
            name = item['name']
            unique_names.add(name)

        # Sort the names
        sorted_names = sorted(unique_names)

        # If output file is specified, save to file
        if output_file:
            try:
                with open(output_file, 'a') as f:
                    for name in sorted_names:
                        f.write(f"{name}\n")
                print(f"\nResults saved to: {output_file}")
            except Exception as e:
                print(f"Error saving to file: {str(e)}")

        # Display results in console
        print("\nFound matches:")
        print("-" * 50)
        for name in sorted_names:
            print(f"- {name}")
        print(f"\nTotal unique matches: {len(unique_names)}")

def parse_arguments():
    parser = argparse.ArgumentParser(description='GitHub Short Name Wordlist Generator')
    parser.add_argument('partial_name', help='Partial name to search for')
    parser.add_argument('-o', '--output', help='Output file to save results')
    return parser.parse_args()

def main():
    args = parse_arguments()
    searcher = GitHubNameSearcher()
    
    print(f"Searching for files matching: {args.partial_name}")
    
    results = searcher.search_files(args.partial_name)
    if results:
        searcher.process_results(results, args.output)

if __name__ == "__main__":
    main()
