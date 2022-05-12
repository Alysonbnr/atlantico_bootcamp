from gensim.corpora.dictionary import Dictionary
from NLP.src.nlp_utils import get_pre_process_wiki_articles
from gensim.models import TfidfModel

# Create a Dictionary from the articles: dictionary
articles = get_pre_process_wiki_articles()
dictionary = Dictionary(articles)

# Create a MmCorpus: corpus
corpus = [dictionary.doc2bow(article) for article in articles]

# Get the fifth document in corpus: doc
doc = corpus[4]

# Create a new TfidfModel using the corpus: tfidf
tfidf = __(__)
# Calculate the tfidf weights of doc: tfidf_weights
tfidf_weights = __[__]

# Print the first five weights
print(___)

# Sort the weights from highest to lowest: sorted_tfidf_weights
sorted_tfidf_weights = ___

# Print the top 5 weighted words
for term_id, weight in sorted_tfidf_weights[:5]:
    print(__,__)