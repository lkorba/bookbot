def count_words(text):
  words = text.split()
  return len(words)

def count_characters(text):
    # Create an empty dictionary to store character counts
    char_counts = {}
    # Iterate through each character in the text
    for char in text:
        # If the character is already in the dictionary, increment its count
        # If not, add it to the dictionary with a count of 1
        char_counts[char.lower()] = char_counts.get(char.lower(), 0) + 1
        # Above oneliner is equivalent of below:
        # Get the lowercase version of the character
        # lowercase_char = char.lower()
        # Get the current count (or 0 if character not seen before)
        # current_count = char_counts.get(lowercase_char, 0)
        # Increment the count
        # new_count = current_count + 1
        # Update the dictionary with the new count
        # char_counts[lowercase_char] = new_count
    return char_counts
def chars_dict_to_sorted_list(char_counts):
    # Create a list to hold your dictionaries
    result = []
    
    # Convert your char_counts into a list of dictionaries
    for char, count in char_counts.items():
        char_info = {"char": char, "count": count}
        result.append(char_info)
    
    # Define a sort helper function (similar to the hint)
    def sort_on(dict):
        return dict["count"]
    
    # Sort the list in descending order (reverse=True)
    result.sort(reverse=True, key=sort_on)
    
    return result

def print_report(word_count, character_counts, bookfile):
  print("============ BOOKBOT ============")
  print("Analyzing book found at " + bookfile)
  print("----------- Word Count ----------")
  print("Found " + str(word_count) + " total words")
  print("--------- Character Count -------")
  for item in chars_dict_to_sorted_list(character_counts):
     print(str(item["char"]) + ": " + str(item["count"]))