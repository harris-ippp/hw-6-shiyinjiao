#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs

addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(addr)
soup = bs(resp.content, "html.parser")
# Find all table rows containing "election_item":
rows = soup.find_all("tr", "election_item")
year = []
_id = []
# Within the same row find the first instance of a cell containing the year
# Extract the ID from the row, split on dashes to extract the numbers
for row in rows:
    year.append(row.find("td","year first").string)
    _id.append(row.get("id")[-5:])
# Concatenate years and election IDs with a space in between and a new line for each year
# and write to a file 'ELECTION_ID'
with open('ELECTION_ID','w') as ELECTION_ID_file:
    for i in range(len(year)):
        ELECTION_ID_file.write(year[i] + ' ' + _id[i] + "\n")
