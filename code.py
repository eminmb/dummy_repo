# Importing the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape article titles and links from a news website 
def scrape_news(url):
    # Send a GET request to the provided URL
    response = requests.get(url)
    
    # If the request is successful, proceed to scrape the content
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all article tags (specific to the website structure)
        articles = soup.find_all('article')

        # Create lists to store titles and URLs
        titles = []
        urls = []

        # Loop through each article and extract the title and URL
        for article in articles:
            # Extract the title
            title_tag = article.find('h2')
            if title_tag:
                title = title_tag.get_text(strip=True)
                titles.append(title)
                
                # Extract the link associated with the article
                link_tag = article.find('a', href=True)
                if link_tag:
                    url = link_tag['href']
                    urls.append(url)

        # Return the titles and URLs as lists
        return titles, urls

    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")
        return [], []

# Function to save the scraped data to a CSV file
def save_to_csv(titles, urls, filename="news_articles.csv"):
    # Create a pandas DataFrame from the titles and URLs
    df = pd.DataFrame({'Title': titles, 'URL': urls})

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main function to initiate the scraping
if __name__ == "__main__":
    # URL of the news website to scrape
    news_url = "https://example-news-website.com"  # Replace with a real news website
    
    # Scrape the titles and URLs
    titles, urls = scrape_news(news_url)
    
    # If data is scraped successfully, save it to a CSV file
    if titles and urls:
        save_to_csv(titles, urls)
    else:
        print("No data to save.")
