import requests
import os
from urllib.parse import urlparse

# Directory for saving images
SAVE_DIR = "Fetched_Images"

def fetch_image(url, downloaded_files):
    try:
        # Request headers first (to check type & size before downloading)
        head = requests.head(url, timeout=10, allow_redirects=True)
        head.raise_for_status()

        # Check content type (must be an image)
        content_type = head.headers.get("Content-Type", "")
        if "image" not in content_type.lower():
            print(f"✗ Skipping {url} (not an image)")
            return

        # Get filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)
        if not filename or "." not in filename:
            filename = "downloaded_image.jpg"

        # Prevent duplicates
        if filename in downloaded_files:
            print(f"⚠ Skipping duplicate: {filename}")
            return

        filepath = os.path.join(SAVE_DIR, filename)

        # Download the image
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        with open(filepath, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)

        downloaded_files.add(filename)
        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred for {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher (Extended Edition)")
    print("A mindful tool for respectfully collecting images\n")

    # Create directory if not exists
    os.makedirs(SAVE_DIR, exist_ok=True)

    # Ask for multiple URLs at once
    urls = input("Please enter image URLs (separated by spaces): ").split()

    # Track already downloaded files
    downloaded_files = set()

    # Process each URL
    for url in urls:
        fetch_image(url.strip(), downloaded_files)

    print("\nConnection strengthened. Community enriched. ✨")


if __name__ == "__main__":
    main()