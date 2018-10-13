import data
import tokenization

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
