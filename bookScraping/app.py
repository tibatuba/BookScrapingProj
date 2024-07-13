from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route('/')
def index():
    # Read the data from the CSV file
    data = pd.read_csv('books.csv')

    # Clean the Price column by removing unwanted characters (e.g., currency symbols)
    data['Price'] = data['Price'].str.replace('Â', '').str.replace('£', '').astype(float)

    # Get query parameters for search, sort, and genre
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', 'Title')
    sort_order = request.args.get('order', 'asc')
    genre = request.args.get('genre', '')

    # Filter data based on search query
    if search_query:
        data = data[data['Title'].str.contains(search_query, case=False)]

    # Filter data based on genre
    if genre:
        data = data[data['Genre'] == genre]

    # Sort data based on sort_by and sort_order
    data = data.sort_values(by=sort_by, ascending=(sort_order == 'asc'))

    # Create a Plotly bar chart with the book titles on the x-axis and prices on the y-axis
    fig = px.bar(data, x='Title', y='Price', color='Rating', hover_data=['Availability', 'Genre'], title='Book Prices')
    
    # Update the layout of the chart for better readability
    fig.update_layout(
        xaxis_title='Book Title',
        yaxis_title='Price',
        xaxis={'categoryorder': 'total descending', 'tickangle': -45},
        margin=dict(l=20, r=20, t=50, b=150),  # Adjusting margins for better space utilization
        height=600,  # Adjusting the height for better readability
        width=1000  # Adjusting the width for better readability
    )

    # Convert the Plotly figure to HTML for rendering in the web page
    graph = fig.to_html(full_html=False)
    
    # Get unique genres for the dropdown menu
    genres = data['Genre'].unique()

    return render_template('index.html', graph=graph, search_query=search_query, sort_by=sort_by, sort_order=sort_order, genre=genre, genres=genres)

if __name__ == '__main__':
    app.run(debug=True)
