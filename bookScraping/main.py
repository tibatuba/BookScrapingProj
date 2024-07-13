import requests
from bs4 import BeautifulSoup
import pandas as pd

# Base URL of the website to scrape
base_url = 'https://books.toscrape.com/catalogue/category/books/travel_2/page-{}.html'

# Lists to store the scraped data
titles = []
prices = []
ratings = []
availabilities = []
genres = []

# Function to convert rating text to numerical value
def rating_to_number(rating):
    rating_dict = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }
    return rating_dict.get(rating, 0)

# Loop through multiple pages
for page in range(1, 50):  # Change range to the number of pages you want to scrape
    # Construct the URL for the current page
    url = base_url.format(page)
    
    # Send a GET request to the website
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all the book items
        books = soup.find_all('article', class_='product_pod')
        
        # Loop through each book item and extract the required details
        for book in books:
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text
            rating = rating_to_number(book.p['class'][1])
            availability = book.find('p', class_='instock availability').text.strip()

            # Navigate to the book detail page to get the genre
            book_url = "https://books.toscrape.com/catalogue/" + book.h3.a['href']
            book_response = requests.get(book_url)
            book_soup = BeautifulSoup(book_response.content, 'html.parser')
            genre = book_soup.find('ul', class_='breadcrumb').find_all('li')[2].a.text.strip()

            titles.append(title)
            prices.append(price)
            ratings.append(rating)
            availabilities.append(availability)
            genres.append(genre)

# Create a DataFrame from the lists
data = pd.DataFrame({
    'Title': titles,
    'Price': prices,
    'Rating': ratings,
    'Availability': availabilities,
    'Genre': genres
})

# Print the first few rows of the DataFrame to verify the 'Genre' column
print(data.head())

# Save the DataFrame to a CSV file
data.to_csv('books.csv', index=False)

print('Data scraped and saved to books.csv')
