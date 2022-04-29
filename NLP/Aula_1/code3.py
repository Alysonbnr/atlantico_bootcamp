from nltk.tokenize import sent_tokenize
from NLP.src.nlp_utils import get_sample_Santo_Graal

scene_one =  get_sample_Santo_Graal()
sentences =  sent_tokenize(scene_one)
# Search for the first occurrence of "coconuts" in scene_one: match
match = ___

# Print the start and end indexes of match
print(__, __)
print (match)

# Write a regular expression to search for anything in square brackets: pattern1
pattern1 = r"___"

# Use re.search to find the first text in square brackets
print(____)

# Find the script notation at the beginning of the fourth sentence and print it
pattern2 = r"___"
print(____)