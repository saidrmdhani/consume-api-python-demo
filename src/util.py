import urllib.request, urllib.response, requests
import datetime, json

class Util:

	# Call a GET request on the URL and return a string
	def get(url: str) -> bytes:

		with urllib.request.urlopen(url) as response:
   			return response.read()

	# Call a GET request on the URL and return JSON data
	def get_json(url: str) -> dict:
		data: dict = { 'data': {}, 'total': 0 }
		with urllib.request.urlopen(url) as response:
			data['data'] = json.load(response)
		data['total'] = response.getheader('X-WP-TotalPages')
		return data

	# Download a file and save a local copy
	def download_file(url: str, filename: str) -> None:
		try:
			print('Downloading: ' + url)
			myfile = requests.get(url)
			open('data/' + filename, 'wb').write(myfile.content)
			print(filename + ' has been downloaded successfully.')
		except:
			print('Error while downloading ' + filename)
