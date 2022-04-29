import matplotlib.pyplot as plt
import re
from nltk.tokenize import regexp_tokenize
from NLP.src.nlp_utils import get_sample_Santo_Graal

# Split the script into lines: lines
holy_grail = get_sample_Santo_Graal()
lines = holy_grail.___(___)

# Replace all script lines for speaker
pattern = "[A-Z]{2,}(\s)?(#\d)?([A-Z]{2,})?:"
lines = [re.__(pattern, __, __) for l in __]

# Tokenize each line: tokenized_lines
tokenized_lines = [regexp_tokenize(__,__) for s in __]

# Make a frequency list of lengths: line_num_words
line_num_words = [___ for t_line in tokenized_lines]

# Plot a histogram of the line lengths
___

# Show the plot
___