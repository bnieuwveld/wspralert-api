'''
Corresponds to a record from Wsprnet.
'''
class Record:
    def __init__(self, date, call, freq, snr, drift, grid, power_dbm, power_w, reporter, reporter_loc, dist_km, dist_mi, mode):
        self.date = date
        self.call = call
        self.freq = freq
        self.snr = snr
        self.drift = drift
        self.grid = grid
        self.power_dbm = power_dbm
        self.power_w = power_w
        self.reporter = reporter
        self.reporter_loc = reporter_loc
        self.dist_km = dist_km
        self.dist_mi = dist_mi
        self.mode = mode
