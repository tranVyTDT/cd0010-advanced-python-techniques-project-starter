"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json
import itertools

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    near_earth_objects = []
    with open(neo_csv_path, newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        headers = next(reader)
        
        for row in reader:
            kwargs = {
                "designation": row[headers.index("pdes")],
                "name": row[headers.index("name")],
                "diameter": row[headers.index("diameter")],
                "hazardous": row[headers.index("pha")]
            } 
            near_earth_objects.append(
                NearEarthObject(**kwargs)
            )
            

    return near_earth_objects


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path) as json_file:
        json_data = json.load(json_file)
    
    close_approachs = []
    fields = {field:i for i,field in enumerate(json_data.get("fields"))}
    data = json_data.get("data")
    
    for la in data:
        kwargs = {
            "_designation": la[fields["des"]],
            "time": la[fields["cd"]],
            "distance": la[fields["dist"]],
            "velocity": la[fields["v_rel"]]
        }
        close_approachs.append(
            CloseApproach(**kwargs)
        )

    return close_approachs

