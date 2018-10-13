import data
import listings
import skills
import tokenization

def test_parsing_listing():
    fidelity_listing = listings.Listing(data.fidelity_listing)
    for token in fidelity_listing.tokens:
        print(' - ' + token)
    print('Found ' + str(len(fidelity_listing.tokens)) + ' tokens')
    print(fidelity_listing.get_languages())

def test_is_data():
    assert skills._is_skill('C', data.languages) # check regular language
    assert skills._is_skill('HTML5', data.languages) # check alias
    assert skills.is_language('jaVA')

if __name__ == '__main__':
    test_is_data()
    test_parsing_listing()
