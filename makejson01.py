#!/usr/bin/python3
"""Reviewing how to parse json | Alta3 Research"""

# JSON is part of the Python Standard Library
import json

def main():
    """runtime code"""
    ## create a blob of data to work with
    hitchhikers = [{"name": "Zaphod Beeblebrox", "species": "Betelgeusian"},
      {"name": "Arthur Dent", "species": "Human"}]

    ## display our Python data (a list containing two dictionaries)
    print(hitchhikers)

    ## open a new file in write mode

        ## use the JSON library
        ## USAGE: json.dump(input data, file like object) ##
    
        
         ## Create the JSON string
    jsonstring = json.dumps(hitchhikers)

    ## Display a single string of JSON
    print(jsonstring)

if __name__ == "__main__":
    main()

