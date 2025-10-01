# Ubuntu_Requests
The Wisdom of Ubuntu

"I am because we are" — this program embodies Ubuntu philosophy by connecting to the global web community, respectfully fetching shared resources, and organizing them for later appreciation.

Program Overview

The Ubuntu Image Fetcher is a Python tool that:

Prompts the user for one or more image URLs.

Downloads each image respectfully from the internet.

Saves them into a Fetched_Images directory.

Handles errors gracefully and avoids duplicates.

This reflects the Ubuntu principles of:

Community → Connecting to shared web resources.

Respect → Handling errors without crashing.

Sharing → Organizing images for reuse and distribution.

Practicality → A useful, real-world tool.

Features

Accepts multiple URLs at once (separated by spaces).

Creates a Fetched_Images directory automatically.

Checks HTTP headers before download to confirm file type.

Skips non-image files and overly large files.

Prevents duplicate downloads.

Graceful error handling for connection issues.

 Example Run
Welcome to the Ubuntu Image Fetcher (Extended Edition)
A mindful tool for respectfully collecting images

Please enter image URLs (separated by spaces): 
https://example.com/photo1.jpg https://example.com/document.pdf https://example.com/photo1.jpg

✓ Successfully fetched: photo1.jpg
✗ Skipping https://example.com/document.pdf (not an image)
⚠ Skipping duplicate: photo1.jpg

Connection strengthened. Community enriched. ✨

Requirements

Python 3.x

requests library

Install dependencies (if needed):

pip install requests

 How to Run

Save the script as ubuntu_fetcher.py.

Run in terminal:

python ubuntu_fetcher.py


Enter one or more image URLs separated by spaces.

Images will be saved in the Fetched_Images folder.

 Notes on Precautions

Only image files (jpg, png, gif, etc.) are downloaded.

Large files (e.g., >10MB) are skipped for safety.

Duplicate images are skipped to avoid redundancy.

 Closing Thought

"A person is a person through other persons."
Every image fetched represents a connection strengthened with the global community.
