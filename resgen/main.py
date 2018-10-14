from flask import Flask, request
import data
import listings
import resumes
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
    #test_parsing_listing()
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, world!"

    @app.route('/genresume', methods=['POST'])
    def genresume():
        listing_data = request.form['data']

        l = listings.Listing(listing_data)
        r = resumes.ResumeManager('sample_data/resume.json')

        things_to_look_for = l.get_skills()
        resumes.rank_resume(r.data, things_to_look_for)

        outpath = r.render_pdf()

        return "hello, world"

    app.run(debug=True)
