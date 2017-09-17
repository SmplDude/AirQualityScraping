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
		pageTables = bsObj.find_all("table", class_="AQData")
		tableRows = pageTables[3].find_all('tr')
		time = tableRows[2].td.small.text
		print("Time: ", time)
		aqi = tableRows[5].td.string
		aqi = "".join(aqi.split())
		print("Air Quality Index: ", aqi)
	except AttributeError as e:
		return None
	
	return tableCellList

print()
zipcode = input("input zipcode: ")
print()
url = "https://airnow.gov/index.cfm?action=airnow.local_city&zipcode={}&submit=Go".format(zipcode)
htmlTags = getAQI(url)
if htmlTags == None:
	print("Problem retrieving AQI")
else :
	healthyLevel = htmlTags[0].text
	print("Your air today is: ", healthyLevel)
	print()