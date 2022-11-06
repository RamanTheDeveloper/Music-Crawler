import requests
from bs4 import BeautifulSoup


#Youtube URL
base_url = "https://www.youtube.com/"
converter_url = "https://ytmp3.nu/"

search_term = input("Please type in the song name: ")
search_url = base_url + "results?search_query=" + search_term
print(search_url)

