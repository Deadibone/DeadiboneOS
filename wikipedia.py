import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_article(title):
    """Fetch and print the Wikipedia article for the given title."""
    url = f"https://en.wikipedia.org/wiki/{title.replace(' ', '_')}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get the article title and content
        article_title = soup.find('h1').get_text()
        paragraphs = soup.find_all('p')

        print(f"\n{article_title}\n")
        for paragraph in paragraphs:
            print(paragraph.get_text())
            print()  # Add a newline for better readability

    except requests.exceptions.HTTPError as e:
        print(f"Error fetching article: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: wikipedia <article title>")
    else:
        title = ' '.join(sys.argv[1:]).strip()
        fetch_wikipedia_article(title)