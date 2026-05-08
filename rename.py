import os
import re

print("Renaming files...")

# Loop through all files in the current folder
for filename in os.listdir('.'):
    if filename.endswith('.html'):
        # Find the specific pattern and replace it with an empty string
        new_name = re.sub(r'^\d{2} - Learn HTML In Arabic 2021 - ', '', filename)
        
        # Rename the file if a match was found and changed
        if new_name != filename:
            os.rename(filename, new_name)
            print(f"Renamed to: {new_name}")

print("All files renamed successfully!")