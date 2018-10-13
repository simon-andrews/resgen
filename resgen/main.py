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

    print('### GOOGLE ###')
    google_listing = listings.Listing(data.google_listing)
    print(google_listing.get_languages())
    print(google_listing.get_frameworks_and_tools())

if __name__ == '__main__':
    test_parsing_listing()
