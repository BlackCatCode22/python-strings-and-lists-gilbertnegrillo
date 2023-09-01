# pythonProgramTwo.py

# Name: Gilbert Negrillo
# Date: 26 August 2023
# Class: CIT-95

text = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."
input("\n" + text) # Takes the given text as input.
print("\n Length calculation: " + str(int(len(text)))) # Returns the length of the text.
input("\n" + text) # Takes the given text as input.
print("\n Uppercase and lowercase conversion: " + str(text.upper()) + " " + str(text.lower())) # Returns text in uppercase letters followed by the text in lowercase letters.
input("\n" + text) # Takes the given text as input
print("\n Word count: " + str(int(text.count("")))) # Returns the total number of words in the text.
print("\nSubstring extraction: " + text + " " + str((text[0:88:1]))) # Takes the given text and returns the substring of text starting from the start index and ending at the end index.[start:stop:step]
print("\n" + text) # Takes the given text as input.
target_word = input("\n Enter a target word: ") # Target word (input by user).
replacement_word = input("\n Enter a replacement word: ") # Replacement word (input by user).
print("\n Word replacement: " + str(text.replace(target_word, replacement_word))) # Returns the text with all occurrences of the target word replaced by the replacement word.
print("\n" + text) # Takes the given text as input.
print("\n Whitespace removal: " + str(text.replace(" ", ""))) # Returns the text with all leading and trailing whitespaces removed.
print("\n" + text) # Takes the given text as input.
print("\n Splitting into sentences: " + str(text.split())) # Returns a list of sentences present in the text.
input("\n" + text) # Takes the given text as input.
print("\n Text with each word reversed: " + str(text[::-1])) # Returns text with each word revered.
character_count = input(str("\n" + text + " Enter a character from the text: ")) # Takes the given text and a character as input.
print("\n Number of occurrences of the specified character in the text: " + str(int(text.count(character_count)))) # Returns the number of occurrences of the specified character in the text.
substring_count = input(str("\n" + text + " Enter a substring from the text: ")) # Takes the given text and a substring as input.
print("\n Number of occurrences of the specified substring in the text: " + str(int(text.count(substring_count)))) # Returns the number of occurrences of the specificed substring in the text.

print("\n" + "Lists: ")

word_list = ["python", "is", "an", "amazing", "programming", "language.", "it", "is", "versatile", "easy", "to", "learn", "and", "powerful."]
print("\n List Creation: " + str(word_list)) # Created a list called word_list by splitting the given text into words.
word_list.append("Pythonic") # Append the word "Pythonic" to the word_list.
print("\n Appending: " + str(word_list))
word_list.insert(0,"awesome") # Insert the word "awesome" at the beginning of the word_list.
print("\n Insertion: " + str(word_list))
print("\n Indexing: " + str(word_list[2]) + " \n slicing: " + str(word_list[5:9])) # Print the third word in the word_list and then print a sublist containing the words from the 6th to 9th position.
word_list.remove("amazing") # Remove the word "amazing" from the word_list.
print("\n Removal: " + str(word_list))
word_list.sort() # Sort the word_list in alphabetical order.
print("\n Sorting: " + str(word_list))
print("\n Counting: " + str(int(word_list.count("is")))) # Count the occurrences of the word "is" in the word_list
string_sentence = " " # String sentence.
print("\n Joining: " + str(string_sentence.join(word_list))) # Join the words in the word_list with spaces.
print("\n Reversal: " + str(word_list[::-1])) # Reverse the order of elements in the word_list.
copied_list = word_list.copy() # Create a new list copied_list.
print("\n Copying: " + str(copied_list)) # Copy the contents of the word_list.