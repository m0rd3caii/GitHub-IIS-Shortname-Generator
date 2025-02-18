# GitHub Shortname Scanner  

GitHub Shortname Scanner is a tool that searches for filenames in public GitHub repositories based on a given keyword and generates a wordlist. This can be useful for security researchers and penetration testers to create wordlists for further analysis, such as identifying potential IIS shortname enumeration vulnerabilities.  

## Features  
✅ Searches GitHub for files matching a given partial name  
✅ Extracts unique filenames from search results  
✅ Saves results to a wordlist file  
✅ Useful for wordlist generation in security research  

## Installation  
Clone the repository and install dependencies:  

```bash
git clone https://github.com/your-username/github-shortname-scanner.git
cd github-shortname-scanner
pip install -r requirements.txt
```

## Usage

```
python gsnw.py WEBDEV -o wordlist.txt
```
This command searches for filenames containing "WEBDEV" and saves the results in wordlist.txt.

## Example Output

Searching for files matching: WEBDEV

Results saved to: wordlist.txt
```
Found matches:
--------------------------------------------------
- .env.webdev
- WebDev.md
- WebDeveloper.java
- webdev.txt
- webdev.py
- webdev.sh
- webdev.html
- webdevicons.lua
- webdevweekly.ts

Total unique matches: 86
```


