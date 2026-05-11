import os
import requests
from bs4 import BeautifulSoup
import re

print("Starting direct URL scraping...")
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

# 1. Grab all your local HTML files
local_files = [f for f in os.listdir('.') if f.endswith('.html') and f.startswith('#')]
local_files.sort()

for filename in local_files:
    # 2. Extract the title from your file name
    # Looks for the pattern: "#XX - " and grabs everything after it until ".html"
    match = re.search(r'#\d{2} - (.*?)\.html', filename)
    if not match:
        continue
        
    title = match.group(1)
    
    # 3. Convert the title to match Elzero's URL format
    # Example: "First Project And First Page" -> "first-project-and-first-page"
    slug = title.lower().replace(' ', '-')
    url = f"https://elzero.org/html-{slug}/"
    
    print(f"\nTargeting: {url}")
    
    try:
        response = requests.get(url, headers=headers)
        
        # Check if the page actually exists
        if response.status_code != 200:
            print(f"   -> [FAILED] Page not found. The URL might be slightly different on the website.")
            continue
            
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 4. Extract the code block
        code_content = ""
        
        # Elzero uses standard <pre> tags or a plugin called EnlighterJS
        code_blocks = soup.find_all('pre')
        
        if code_blocks:
            for block in code_blocks:
                # Grab the raw text inside the code block
                code_content += block.get_text(strip=False) + "\n\n"
        else:
            code_content = f"\n"
            
        # 5. Write the extracted code into your local file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(code_content.strip())
            
        print(f"   -> [SUCCESS] Saved code to {filename}")
        
    except Exception as e:
        print(f"   -> [ERROR] Something went wrong: {e}")

print("\nAll done! Check your files.")