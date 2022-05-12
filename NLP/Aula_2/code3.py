# Import Dictionary
___
from NLP.src.nlp_utils import get_pre_process_wiki_articles

# Create a Dictionary from the articles: dictionary
articles = get_pre_process_wiki_articles()
dictionary =___(___)

# Select the id for "computer": computer_id
computer_id = __(__)

# Use computer_id with the dictionary to print the word
print('the word', __, 'has index', __, 'in dictionary')

# Create a MmCorpus: corpus
corpus = [_._(_) for article in _]

# Print the first 10 word ids with their frequency counts from the fifth document
print(corpus[_][:_])
