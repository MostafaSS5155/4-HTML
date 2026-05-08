import os

print("Adding '#' to files...")

for filename in os.listdir('.'):
    # Only target HTML files and prevent adding multiple # if run twice
    if filename.endswith('.html') and not filename.startswith('#'):
        new_name = f"#{filename}"
        os.rename(filename, new_name)
        print(f"Renamed to: {new_name}")

print("Done! All files updated.")