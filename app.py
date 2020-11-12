from flask import request, url_for
from flask_api import FlaskAPI, status, exceptions
from flask_cors import CORS
from Scrape import Scrape
import array_filterer

app = FlaskAPI(__name__)
CORS(app)
scraper = Scrape()

@app.route('/api/scrape')
def root():
    # Get the query parameters
    min_power = float(request.args.get("min_power")) if request.args.get("min_power") else 0
    min_distance = float(request.args.get("min_distance")) if request.args.get("min_distance") else 0

    refresh = scraper.refresh()

    if refresh['status'] == 500:
        return { 'error': 'Error connecting to Wsprnet!' }

    results = scraper.return_message()

    filtered_results = array_filterer.filter_list(results, min_power, min_distance)

    # Send our results now to the database logic.
    # We want to save these new results in a Redis store, and see if they're stronger than any other recent/previous signals
    # TODO

    return filtered_results
    
if __name__ == "__main__":
    app.run()