"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from helpers import datetime_to_str

def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    with open(filename, 'w') as csv_file:
        csv_file.write(','.join(list(fieldnames)) + '\n')
        for close_approach in results:
            values = list(map(str, [close_approach.time, close_approach.distance,\
                close_approach.velocity, close_approach.neo.designation,\
                close_approach.neo.name, close_approach.neo.diameter,\
                close_approach.neo.hazardous]))
            csv_file.write(','.join(values) + '\n')



def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    write_value = []
    for close_approach in results:
        write_value.append({
            "datetime_utc": datetime_to_str(close_approach.time),
            "distance_au": close_approach.distance,
            "velocity_km_s": close_approach.velocity,
            "neo": {
                "designation": close_approach.neo.designation,
                "name": close_approach.neo.name,
                "diameter_km": close_approach.neo.diameter,
                "potentially_hazardous": close_approach.neo.hazardous
            }
        })
    with open(filename, 'w') as json_file:
        json_str = json.dumps(write_value)
        json_file.write(json_str)
    
