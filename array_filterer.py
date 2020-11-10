def filter_list(array, power_filter, distance_filter):
    filtered_list = list(filter(lambda record: record['power_w'] >= power_filter and record['distance_km'] >= distance_filter, array))
    return filtered_list