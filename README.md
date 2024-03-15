## Building a Financial Newsfeed Application with Flask

### HTML Files
- **index.html**:
   - The main page of the application.
   - Displays a list of news articles related to financial topics.

- **article.html**:
   - Displays the details of a specific news article, including its title, content, and publication date.

### Routes
- **@app.route('/')**: Maps the URL '/' to the 'index' function, which renders the 'index.html' page.

- **@app.route('/article/<int:article_id>')**: Maps the URL '/article/<int:article_id>' to the 'get_article' function, which retrieves and renders the article with the provided 'article_id' using 'article.html'.

- **@app.route('/api/articles')**: Maps the URL '/api/articles' to the 'get_articles' function, which returns a JSON response containing all available news articles.

- **@app.route('/api/article/<int:article_id>')**: Maps the URL '/api/article/<int:article_id>' to the 'get_article_api' function, which returns a JSON response containing the details of the article with the provided 'article_id'.

- **@app.route('/api/articles/search')**: Maps the URL '/api/articles/search' to the 'search_articles' function, which takes a search query as a parameter and returns a JSON response containing the matching news articles.