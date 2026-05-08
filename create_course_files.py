import os
import yt_dlp

playlist_url = 'https://youtube.com/playlist?list=PLDoPjvoNmBAw_t_XWUFbBX-c9MafPk9ji'

# Configuration to only extract information, not download the videos
ydl_opts = {
    'extract_flat': True,
    'quiet': True
}

print("Fetching playlist data...")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(playlist_url, download=False)
    
    for i, entry in enumerate(info['entries'], start=1):
        # Fallback to 'Video_X' if title is missing
        title = entry.get('title', f'Video_{i}')
        
        # Sanitize the title to ensure it's a valid filename
        safe_title = "".join(c for c in title if c.isalnum() or c in " -_").strip()
        
        # Format: "01 - Video Title.html"
        file_name = f"{i:02d} - {safe_title}.html"
        
        # Basic HTML Boilerplate
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body>
    <!-- Notes for {title} -->
</body>
</html>"""
        
        # Create the file
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"Created: {file_name}")

print("Done! All HTML files have been generated.")