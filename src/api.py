from src.util import Util
from src.config import Config
import json, io

# An example API class
class API:

	# Static initialization
	def static_init() -> None:

		return Config.static_init()

	def download_all_media() -> None:

		page = 1
		images = API.get_page_images(1)
		while page <= int(images['total']):
			images = API.get_page_images(page)
			page = page + 1
			API.download_page_images(images['data'])

	# Get page images
	def get_page_images(page: int) -> dict:

		url: str = Config.get_url() + '/wp-json/wp/v2/media?per_page=5&page=' + str(page)
		data = Util.get_json(url)
		return data

	def download_page_images(images: dict) -> None:

		for image in images:
			filename = image['title']['rendered'] + '.' + image['mime_type'].split('/')[1]
			Util.download_file(image['source_url'], filename)