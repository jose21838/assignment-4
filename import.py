import json
import difflib

# Load the dictionary data from a JSON file
with open('dictionary.json', 'r') as file:
    data = json.load(file)

def get_definition(word, dictionary):
    word = word.lower()  # Make the search case-insensitive
    if word in dictionary:
        return dictionary[word]
    else:
        return "The word is not in the dictionary."

def get_closest_match(word, dictionary):
    word = word.lower()
    closest_matches = difflib.get_close_matches(word, dictionary.keys(), n=1)
    if closest_matches:
        return closest_matches[0]
    else:
        return None

def get_definition_with_suggestions(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    else:
        closest_match = get_closest_match(word, dictionary)
        if closest_match:
            return f"The word is not in the dictionary. Did you mean '{closest_match}'?"
        else:
            return "The word is not in the dictionary and no close match found."

# Example usage
word = input("Enter a word: ")
definition = get_definition_with_suggestions(word, data)
print(definition)
