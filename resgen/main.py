import tokenization
import data

def test_parsing_listing():
    tokens = tokenization.tokenize(data.fidelity_listing)
    for token in tokens:
        print('- ' + token)
    print('Found ' + str(len(tokens)) + ' tokens')

def test_is_data():
    assert data.is_data('C', data.languages) # check regular language
    assert data.is_data('HTML5', data.languages) # check alias

if __name__ == '__main__':
    test_is_data()
    test_parsing_listing()
