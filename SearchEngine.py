import csv

def local_database_search(file_path):
    # Keep the search loop going until the user decides to stop
    search_loop = True
    while search_loop:
        # Create an empty dictionary to store the search results
        search_results = {}
        # Initialize a counter for the search results
        count = 1
        # Initialize a counter for the search result display
        result_count = 1
        # Open the file and create a CSV reader
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            # Prompt the user for a search query
            title_search = input("What would you like to search for? ")
            # Iterate through the rows of the file
            for row in reader:
                # If the search query is in the title, add it to the search results
                if title_search in row['title']:
                    an = row['articleNum']
                    title = row['title']
                    search_results[count] = an, title
                    count += 1
            # Print the search results
            print('\nHermes Search Engine')
            print('(c) Hermes Corporation. All rights reserved.\n')
            print(f"{len(search_results)} search results for '{title_search}'\n")
            for i in search_results:
                a = search_results.get(result_count)
                print(result_count, ': ', a[1])
                result_count += 1
        # If there are search results, ask the user which one they want to read
        while search_results:
            with open(file_path, 'r') as file:
                reader1 = csv.DictReader(file)
                test_input = int(input("What article would you like to read? (Enter the number attached): "))
                # If the user input is a valid search result, print the article text
                for i in range(1, 100):
                    if test_input == i:
                        selection = search_results[i][0]
                        for row in reader1:
                            if str(selection) in row["articleNum"]:
                                print(row['text'].replace('|', '\n'), end='\n')
                        # Clear the search results so we don't ask the user to read an article again
                        search_results = {}
        # Ask the user if they want to search for something else
        input_select = input("Did you want to search for something else? (y/n): ")
        # If the user wants to search again, go back to the start of the loop
        if input_select == 'y':
            continue
        # If the user doesn't want to search again, exit the loop
        elif input_select == 'n':
            search_loop = False
        # If the user input is invalid, print an error message
        else:
            print(f"'{input_select}' is an invalid command")
