import pandas as pd

# Importing the file 'tweets.csv' and assigning it to the variable df
df = pd.read_csv('tweets.csv')

# Initializing an empty dictionary to store language counts
langs_count = {}

# Iterating over the 'lang' column in the DataFrame df
for entry in df['lang']:
    # Checking if the language is already in the dictionary
    if entry in langs_count:
        # Incrementing the count of the language by 1
        langs_count[entry] += 1
    else:
        # Adding the new language to the dictionary with a count of 1
        langs_count[entry] = 1

# Printing the dictionary of language counts
print(langs_count)

