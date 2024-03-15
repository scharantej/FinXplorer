
# Import necessary modules
from flask import Flask, render_template, request, jsonify
import sqlite3

# Create a Flask application
app = Flask(__name__)

# Define the database connection
conn = sqlite3.connect('financial_news.db')
c = conn.cursor()

# Define the home route
@app.route('/')
def index():
    # Get all the news articles from the database
    c.execute('SELECT * FROM articles')
    articles = c.fetchall()

    # Render the index page with the articles
    return render_template('index.html', articles=articles)

# Define the article route
@app.route('/article/<int:article_id>')
def get_article(article_id):
    # Get the article with the specified ID from the database
    c.execute('SELECT * FROM articles WHERE id=?', (article_id,))
    article = c.fetchone()

    # Render the article page with the article
    return render_template('article.html', article=article)

# API route to get all news articles
@app.route('/api/articles')
def get_articles():
    # Get all the news articles from the database
    c.execute('SELECT * FROM articles')
    articles = c.fetchall()

    # Convert the articles to JSON format
    articles_json = jsonify(articles)

    # Return the JSON response
    return articles_json

# API route to get a specific news article
@app.route('/api/article/<int:article_id>')
def get_article_api(article_id):
    # Get the article with the specified ID from the database
    c.execute('SELECT * FROM articles WHERE id=?', (article_id,))
    article = c.fetchone()

    # Convert the article to JSON format
    article_json = jsonify(article)

    # Return the JSON response
    return article_json

# API route to search news articles
@app.route('/api/articles/search')
def search_articles():
    # Get the search query from the request
    query = request.args.get('query')

    # Search the database for articles that match the query
    c.execute('SELECT * FROM articles WHERE title LIKE ? OR content LIKE ?', ('%' + query + '%', '%' + query + '%'))
    articles = c.fetchall()

    # Convert the articles to JSON format
    articles_json = jsonify(articles)

    # Return the JSON response
    return articles_json

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
