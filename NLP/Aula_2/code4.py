import itertools
from collections import defaultdict
from gensim.corpora.dictionary import Dictionary
from NLP.src.nlp_utils import get_pre_process_wiki_articles

# Create a Dictionary from the articles: dictionary
articles = get_pre_process_wiki_articles()
dictionary = Dictionary(articles)

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Get the fifth document in corpus: doc
doc = corpus[4]

# Sort the doc for frequency: bow_doc
bow_doc = sorted(doc, key=lambda w: w[1], reverse=True)

# Print the top 5 words of the document alongside the count
for word_id, word_count in bow_doc[:5]:
    print("The token ",__,"appears ",__ , "times")

# Create the defaultdict: total_word_count
total_word_count = defaultdict(int)
for word_id, word_count in itertools.chain.from_iterable(corpus):
    __[__] += __

# Choose a key between 0 and 10 and show the count with a print function.
key = __
print("the key", __,"in defaultdict has count: ", ___,'\n')

# Create a sorted list from the defaultdict: sorted_word_count
sorted_word_count = sorted(____, key=lambda w: w[1], reverse=True)

# Print the top 5 words across all documents alongside the count
for ____, ____ in sorted_word_count[:5]:
    print(____.____(____), ____)

