import requests
import config
from bs4 import BeautifulSoup

class Scrape:
    def refresh(self):
        try:
            # Get the page itself and make it parseable
            page = requests.get(f"http://wsprnet.org/olddb?mode=html&band=all&limit=500&findcall=&findreporter={config.RECEIVED_BY}&sort=date")
        except:
            return { 'status': 500 }
        
        soup = BeautifulSoup(page.content, 'html.parser')

        # Find all results with a "table" element
        self.results = soup.find_all('tr')

        return { 'status': 200 }
        

    def return_message(self):
        # Going to make an array of objects. Each object is a "record" from Wspr.
        results_as_json = []
        
        # Starting from the fourth element, find every table cell (which will correspond to a record). 
        for result in self.results[4::]:
            cells = result.find_all('td')

            date = cells[0].get_text().strip()
            call = cells[1].get_text().strip()
            freq = float(cells[2].get_text().strip())
            snr = cells[3].get_text().strip()
            drift = int(cells[4].get_text().strip())
            grid = cells[5].get_text().strip()
            power_dbm = cells[6].get_text().strip()
            power_w = float(cells[7].get_text().strip())
            reporter = cells[8].get_text().strip()
            reporter_loc = cells[9].get_text().strip()
            dist_km = int(cells[10].get_text().strip())
            dist_mi = int(cells[11].get_text().strip())
            mode = cells[12].get_text().strip()

            results_as_json.append({
                'date': date,
                'call': call,
                'freq': freq,
                'snr': snr,
                'drift': drift,
                'grid': grid,
                'power_dbm': power_dbm,
                'power_w': power_w,
                'reporter_call': reporter,
                'reporter_loc': reporter_loc,
                'distance_km': dist_km,
                'distance_mi': dist_mi,
                'mode': mode
            })

        return results_as_json
