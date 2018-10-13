import nltk

# "standardizes" words so they can be compared easily
def clean_word(word):
    word = word.strip() # remove whitespace
    word = word.lower() # convert to lowercase
    return word

def clean_word_list(word_list):
    cleaned_list = list()
    for word in word_list:
        word = clean_word(word)
        try:
            assert word not in ['.', ',', '(', ')', '\'', '"', ':', ';', '/'] # remove punctuation
            assert not word.isnumeric() # remove numbers
            assert word not in nltk.corpus.stopwords.words('english') # remove stopwords (and, or...)
        except AssertionError:
            continue
        cleaned_list.append(word)
    return cleaned_list

# converts a job listing string into a list of useful words, in an easy to use
# "normalized" format
def listify(job_listing):
    words = nltk.word_tokenize(job_listing) # tokenize
    words = clean_word_list(words) # get rid of extra garbage
    words = list(set(words)) # remove duplicates
    return words
