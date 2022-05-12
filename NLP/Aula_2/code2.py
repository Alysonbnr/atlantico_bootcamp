# Import WordNetLemmatizer and Counter
__
__
from NLP.src.nlp_utils import get_wiki_article_lower_tokens, get_english_stop_words


lower_tokens = get_wiki_article_lower_tokens()

# Retain alphabetic words: alpha_only
alpha_only = [_ for t in __ if __]

english_stop = get_english_stop_words()
# Remove all stop words: no_stops
no_stops = [__ for t in __ if __ not in __]

# Instantiate the WordNetLemmatizer
wordnet_lemmatizer = __()

# Lemmatize all tokens into a new list: lemmatized
lemmatized = [__(__) for t in __]

# Create the bag-of-words: bow
bow = __

# Print the 10 most common tokens
___
