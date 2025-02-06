import json
from collections import OrderedDict
from collections.abc import MutableMapping
from typing import List

def flatten(dictionary, keys, parent_key='', separator='.'):
    """
    Function to flatten a nested dictionary and extract specific keys.

    :param dictionary: Dictionary to read from - usually from a JSON file
    :param keys: Keys to be extracted - from keys_file_path
    :parent_key: Base key to use for concatenation (empty by default)
    :separator: Separator to use for concatenating keys (default is a dot '.')
    
    """
        
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, MutableMapping):
            items.extend(flatten(value, keys, new_key, separator=separator).items())
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, MutableMapping):
                    items.extend(flatten(item, keys, new_key, separator=separator).items())
                else:
                    if new_key in keys:
                        items.append((new_key, item))
        else:
            if new_key in keys:
                items.append((new_key, value))
    return dict(items)


def json_flatten(json_file_path: str, keys_file_path: str, output_file_path: str) -> bool:
    """
    Function to read a nested JSON file and a keys file, flattens the 
    JSON based on the specified keys and writes the flattened JSON to 
    an output file.

    :param json_file_path: File path to read nested JSON from 
    :param keys_file_path: File path to read key paths to be flattened
    :param output_file_path: File path to write flattened JSON to 
    :return:

    """

    try:
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        
        with open(keys_file_path, 'r') as f:
            keys = json.load(f)
        
        flattened_data = flatten(data, keys)
        
        with open(output_file_path, 'w') as f:
            json.dump(flattened_data, f, indent=4)
        
        print("Run successfully")
        return True
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False