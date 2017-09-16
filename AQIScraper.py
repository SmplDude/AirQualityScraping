from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
def getAQI(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		return None
	try:
		bsObj = BeautifulSoup(html, "html.parser")
		tableCellList = bsObj.find_all('td', class_="AQDataLg")
	except AttributeError as e:
		return None
	return tableCellList[0].text

zipcode = input("input zipcode: ")
url = "https://airnow.gov/index.cfm?action=airnow.local_city&zipcode={}&submit=Go".format(zipcode)
print(url)
airQuality = getAQI(url)
if airQuality == None:
	print("Problem retrieving AQI")
else :
	print("Your air today is: ", airQuality)