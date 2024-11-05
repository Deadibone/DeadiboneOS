import os
import requests
import sys

def fetch(url):
    """Download a file from the given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Extract the filename from the URL
        filename = url.split('/')[-1]

        # Save the file
        with open(filename, 'wb') as f:
            f.write(response.content)
        
        print(f"Downloaded: {filename}")
    
    except requests.exceptions.MissingSchema:
        print("Invalid URL. Please specify a valid URL.")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: fetch <URL>")
    else:
        fetch(sys.argv[1])