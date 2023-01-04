# This script is a search engine that allows the user to search a local CSV file for a specific string. 
# The search results are displayed to the user, and the user can choose to view one of the articles 
# in the search results. If the user wants to search for something else, they can do so by entering 
# "y" at the prompt. If they don't want to search again, they can enter "n" to exit the search loop. 
# The script uses the csv library to read the CSV file and extract the relevant data.

# This script searches a local CSV file for a specific string.
# The local_database_search function is imported from the SearchEngine module.
from SearchEngine import local_database_search

# The local_database_search function is called with the path to the CSV file as an argument.
local_database_search('./Hermes-Python-CSV-Search-Engine/exampleCSV.csv')