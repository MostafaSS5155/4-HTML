import os

print("Clearing contents of HTML files...")
count = 0

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        # Opening a file in 'w' (write) mode and closing it immediately empties it
        open(filename, 'w').close()
        count += 1

print(f"Done! Emptied {count} files.")