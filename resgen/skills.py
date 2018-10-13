import data
import tokenization

# Does a list `mainlist` contain `subset` (in order)?
# master = [1, 2, 3, 4, 5]
# _lcs(master, [2,3]) -> True
# _lcs(master, [3,2]) -> False
def _list_contains_subset(main_list, subset):
    for index in range(len(main_list) - len(subset) + 1):
        mset = list()
        for i in range(len(subset)):
            mset.append(main_list[index + i])
        if mset == subset:
            return True
    return False

# does a list of tokens contain a phrase?
# similar to _list_contains_subset
# master = ['the', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']
# contains_phrase(master, 'brown fox') -> True
# contains_phrase(master, 'quick fox') -> False
def token_list_contains_phrase(token_list, phrase):
    token_list = [tokenization.clean_word(token) for token in token_list]
    phrase_word_list = [tokenization.clean_word(word) for word in phrase.split(' ')]
    return _list_contains_subset(token_list, phrase_word_list)

def find_skills(tokens, dataset):
    detected_skills = set()
    for datapoint in dataset['data']:
        if token_list_contains_phrase(tokens, datapoint):
            detected_skills.add(datapoint)
    for aliased_thing in dataset['aliases']:
        for alias in dataset['aliases'][aliased_thing]:
            if token_list_contains_phrase(tokens, alias):
                detected_skills.add(alias)
    return detected_skills

###########################################################################
## stuff that isn't used anymore but might still be useful in the future ##
###########################################################################

# is a token inside the dataset (or is an alias)?
def _is_skill(token, dataset):
    token = tokenization.clean_word(token)
    for datapoint in dataset['data']:
        if token == tokenization.clean_word(datapoint):
            return True
    for aliased_thing in dataset['aliases']:
        for alias in dataset['aliases'][aliased_thing]:
            if token == tokenization.clean_word(alias):
                return True
    return False

def is_language(token):
    return _is_skill(token, data.languages)

def is_framework_or_tool(token):
    return _is_skill(token, data.frameworks_and_tools)
