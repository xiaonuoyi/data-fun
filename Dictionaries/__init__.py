from json_flatten import json_flatten

if __name__ == "__main__":
    json_file_path = "\Users\kz98\OneDrive\Documents\Projects - Data Fun\data-fun\Dictionaries\JSON\product_example.json"
    keys_file_path = "\Users\kz98\OneDrive\Documents\Projects - Data Fun\data-fun\Dictionaries\JSON\example_argument.json"
    output_file_path = "\Users\kz98\OneDrive\Documents\Projects - Data Fun\data-fun\Dictionaries\JSON\example_output_from_script.json"
    
    success = json_flatten(json_file_path, keys_file_path, output_file_path)
    if success:
        print("JSON flattening was successful. Check the output file.")
    else:
        print("An error occurred during JSON flattening.")