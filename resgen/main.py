from listings import fidelity_listing
import parsing

def test_parsing_listing():
    tokens = parsing.listify(fidelity_listing)
    for token in tokens:
        print('- ' + token)
    print('Found ' + str(len(tokens)) + ' tokens')

if __name__ == '__main__':
    test_parsing_listing()
