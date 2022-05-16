import requests
import random
import os
from bs4 import BeautifulSoup as bs

session = requests.session()

def get_link():
	global session
	text_file = open("Output2.txt", "r")
	word = text_file.read()
	text_file.close()

	endpoint = "https://www.youtube.com/results?search_query=" + word
	responce = session.get(endpoint)

	soup = bs(responce.text, "html.parser")
	poo = str(soup)

	sep = 'https://i.ytimg.com'

	div = poo.find(sep)
	poo = poo[div:]
	poo = poo[23:34]
	Final = "https://www.youtube.com/watch?v=" + poo

	text_file = open("Output2.txt", "w")
	text_file.write(Final)
	text_file.close()
	os._exit(0)


get_link()