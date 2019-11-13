from src.api import API as API

class Example: 

	def static_init() -> None:
		return API.static_init()

	def download_wp_media() -> None:
		return API.download_all_media()


Example.static_init()
Example.download_wp_media()