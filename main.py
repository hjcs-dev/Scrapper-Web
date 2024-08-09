import requests

def detect_website_type(url):
    """Detects the type of website based on HTML content."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        # Basic detection based on common elements
        html_content = response.text
        if 'wp-content' in html_content:
            return 'WordPress'
        elif 'joomla' in html_content:
            return 'Joomla'
        elif 'drupal' in html_content:
            return 'Drupal'
        elif 'magento' in html_content:
            return 'Magento'
        elif 'typo3' in html_content:
            return 'TYPO3'
        # More generic detection for various sites
        elif '<meta name="description"' in html_content:
            return 'General Website'
        
        return 'Unknown'
    except requests.RequestException as e:
        print(f"Error detecting website type for {url}: {e}")
        return 'Error'

def save_html_content(url, filename):
    """Fetches and saves the HTML content of the website."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"HTML content saved to '{filename}'.")
    except requests.RequestException as e:
        print(f"Error fetching content for {url}: {e}")

def main():
    url = input("Enter the URL of the site to scrape: ")
    website_type = detect_website_type(url)
    print(f"Detected Website Type: {website_type}")

    filename = 'website_content.html'
    save_html_content(url, filename)

if __name__ == "__main__":
    main()
