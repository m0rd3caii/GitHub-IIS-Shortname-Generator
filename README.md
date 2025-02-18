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
git clone https://github.com/m0rd3caii/GitHub-Shortname-Scanner.git
cd github-shortname-scanner
pip install -r requirements.txt
```

## Configuration

Set up your token here:

```py
"Authorization": "token YOUR_GITHUB_TOKEN"
```
(in gsnw.py)

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

## Using with IIS ShortScan

This tool is particularly useful when combined with ShortScan IIS, a tool used to enumerate short filenames on IIS servers.

### Scenario

#### 1. Run ShortScan IIS against a target  

```bash
shortscan https://target.com/
```
Example Output:
```
_LOGMO~1             _LOGMO?    
DOCKER~3             DOCKER?    
DOCKER~2             DOCKER?    
DOCKER~1             DOCKER?    
WEB~1.CON            WEB.CON?   
```
#### 2.Use GitHub Shortname Scanner to find matching filenames:

```
python gsnw.py WEB -o wordlist.txt
```

#### 3.Cross-check results

Compare the results from ``wordlist.txt`` with ShortScan IIS output to determine the full filenames and improve enumeration.










