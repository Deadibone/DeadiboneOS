import requests
from bs4 import BeautifulSoup

def google_search(query):
    """Search Google and return the titles and links of the results."""
    try:
        # Prepare the search URL
        url = f"https://www.google.com/search?q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        
        # Send the request
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find and print search results
        results = soup.find_all('h3')  # Titles are usually in <h3> tags
        links = soup.find_all('a')

        for title, link in zip(results, links):
            if 'href' in link.attrs:
                print(f"Title: {title.get_text()}")
                print(f"Link: https://google.com{link['href']}")
                print()
    
    except requests.exceptions.RequestException as e:
        print(f"Error during the request: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: google <search query>")
    else:
        query = ' '.join(sys.argv[1:]).strip()
        google_search(query)