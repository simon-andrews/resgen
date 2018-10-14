.PHONY: google

fidelity:
	cd resgen && python3 -c "import requests; import data; requests.post('http://127.0.0.1:5000/genresume', data={'data': data.fidelity_listing})"

google:
	cd resgen && python3 -c "import requests; import data; requests.post('http://127.0.0.1:5000/genresume', data={'data': data.google_listing})"
