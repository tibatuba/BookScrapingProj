# Web Scraping Project Extracting Data and Manipulating It Using Tools Like Flask and Plotly

# With CSS, HTML, BeautifulSoup, and Python I was able to display the data that was scraped from bookstoscrape.com in a meaningful way using graphs and filters while simultaneously making it aesthetic

This project was built along with a Youtube video displaying how to do web scraping. This project demonstrates the use of the following:

* CSS and the various aesthetics and formatting it adds to a websites look
* HTML and its part in enabling the display of the data on the webpage
* Panads was used to to read and clean up the file, filtering data based on search query and genre selection, extracting only the unique genres for use in the dropdown menu, and finally sorting the data in ascending format.
* Flask handles the request and therefore access to the root url 'index', Flask uses request.args.get to extract query parameters from the URL, and Flask calls render_template to render the index.html template, passing the necessary context variables.
* Plotly is used to create the data visual and includes creating a bar chart with the function px.bar that crates the x, and y-axis in addition to the interactive hover data addition to the graph.

  Here is a short demo showing what the site has to offer! Enjoy!
[book prices app.zip](https://github.com/user-attachments/files/16228085/book.prices.app.zip)
