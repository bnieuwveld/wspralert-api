from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS
from Scrape import Scrape

app = FlaskAPI(__name__)
CORS(app)
scraper = Scrape()

@app.route('/api/scrape')
def root():
    scraper = Scrape()
    refresh = scraper.refresh()

    if refresh['status'] == 500:
        return { 'error': 'Error connecting to Wsprnet!' }

    results = scraper.return_message()

    # Send our results now to the database logic.
    # We want to save these new results in a Redis store, and see if they're stronger than any other recent/previous signals
    # TODO

    return results
    
if __name__ == "__main__":
    app.run(debug=True)