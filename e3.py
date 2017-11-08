#!/usr/bin/env python

import pandas as pd
import matplotlib
%matplotlib inline

# Write a for loop, placing up all dataframes (elections) in a list
#1) define a list outside the loop, append each dataframe into that list
year = ['2016', '2012', '2008', '2004', '2000', '1996', '1992', '1988', '1984', \
'1980', '1976', '1972', '1968', '1964', '1960', '1956', '1952', '1948', '1944', \
'1940', '1936', '1932', '1928', '1924']
elections = []
for i in range(24):
    # Take the first row as the header
    file_name = "president_general_" + year[i] + ".csv"
    header = pd.read_csv(file_name, nrows = 1).dropna(axis = 1)
    # Import the header and second row as a dictionary
    d = header.iloc[0].to_dict()
    df = pd.read_csv(file_name, index_col = 0, thousands = ",", skiprows = [1])
    # Rename to democrat/republican
    df.rename(inplace = True, columns = d)
    # Drop empty columns
    df.dropna(inplace = True, axis = 1)
    # Add year variable
    df["Year"] = year[i]
    elections.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])
    #print(elections)
#2) Concatenate the lists using pd.concat(list)
elections_df = pd.concat(elections)
# Define a new column, Republican Share
elections_df["Republican Share"] = elections_df["Republican"] / elections_df["Total Votes Cast"]
elections_df.reset_index(inplace=True)

# plot the Republican vote share in Accomack County, Albermarle County, Alexandria City, and Alleghany County
mask1 = elections_df["County/City"] == "Accomack County"
mask2 = elections_df["County/City"] == "Albemarle County"
mask3 = elections_df["County/City"] == "Alexandria City"
mask4 = elections_df["County/City"] == "Alleghany County"
fig1 = elections_df[mask1].plot(x = "Year", y = "Republican Share", kind = "bar", title = "Republican vote share in Accomack County")
fig1.figure.savefig("accomack_county.pdf")
fig2 = elections_df[mask2].plot(x = "Year", y = "Republican Share", kind = "bar", title = "Republican vote share in Albemarle County")
fig2.figure.savefig("albemarle_county.pdf")
fig3 = elections_df[mask3].plot(x = "Year", y = "Republican Share", kind = "bar", title = "Republican vote share in Alexandria County")
fig3.figure.savefig("alexandria_county.pdf")
fig4 = elections_df[mask4].plot(x = "Year", y = "Republican Share", kind = "bar", title = "Republican vote share in Alleghany County")
fig4.figure.savefig("alleghany_county.pdf")
