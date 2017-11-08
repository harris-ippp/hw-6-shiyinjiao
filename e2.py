#!/usr/bin/env python

import requests
for line in open("ELECTION_ID"):
    year = line[:4]
    _id = line[-6:].strip()
    addr = "http://historical.elections.virginia.gov/elections/download/"
    addr += _id
    addr += "/precincts_include:0/"
    resp = requests.get(addr)
    file_name = "president_general_" + year + ".csv"
    with open(file_name, "w") as out:
        out.write(resp.text)
