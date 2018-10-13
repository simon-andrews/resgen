import data
import listings
import tokenization

def test_parsing_listing():
    fidelity_listing = listings.Listing(data.fidelity_listing)
    for token in fidelity_listing.tokens:
        print(' - ' + token)
    print('Found ' + str(len(fidelity_listing.tokens)) + ' tokens')

def test_is_data():
    assert data.is_data('C', data.languages) # check regular language
    assert data.is_data('HTML5', data.languages) # check alias

if __name__ == '__main__':
    test_is_data()
    test_parsing_listing()
