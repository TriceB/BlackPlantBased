import json
import requests
from bs4 import BeautifulSoup
from pprint import pprint

offset = 30
url = "https://www.yelp.com/collection/user/rendered_items?collection_id=djWWa-tq8K_5y8BVc38ttg&offset=" + str(offset) + "&sort_by=date"
	# "https://www.yelp.com/collection/djWWa-tq8K_5y8BVc38ttg"

header = {
	'authority': 'www.yelp.com',
	'method': "GET",
	'path': '/collection/user/rendered_items?collection_id=djWWa-tq8K_5y8BVc38ttg&offset=100&sort_by=date',
	'scheme': 'https',
	'accept': '*/*',
	'accept-encoding': 'gzip, deflate, br',
	'accept-language': 'en-US,en;q=0.9',
	'cookie': 'bse=270abba02f85435db48b26cfe1e74243; hl=en_US; wdi=1|929147CDEB88ED6E|0x1.7f5ed981c08fap+30|0c6baa6c98744ffc; _fbp=fb.1.1607973079057.487308967; G_ENABLED_IDPS=google; zs=uuu4zJTYYsy8zF1trtGrtDAm7LjXXw; zss=6ArvY3i85J8vqS0Qc_HVxXTs7LjXXw; recentlocations=Bronx,+NY;;Downtown,+Houston,+TX;;Round+Rock,+TX;;Austin,+TX;;Providence,+RI;;Philadelphia,+PA;;Honolulu,+HI;;japan;;Kitasenju+Station,+Adachi,+Tokyo; location={"city":+"Los+Angeles",+"state":+"CA",+"country":+"US",+"latitude":+34.052392981469445,+"longitude":+-118.24368000761717,+"max_latitude":+34.1682093,+"min_latitude":+33.9547806,+"max_longitude":+-118.1529362,+"min_longitude":+-118.4896057,+"zip":+"",+"address1":+"",+"address2":+"",+"address3":+"",+"neighborhood":+"",+"borough":+"",+"provenance":+"YELP_GEOCODING_ENGINE",+"display":+"Los+Angeles,+CA",+"unformatted":+"Los+Angeles,+CA",+"isGoogleHood":+false,+"usingDefaultZip":+false,+"accuracy":+4,+"language":+null}; hsfd=0; sc=a6ce91fd52; xcj=1|TgRsaO5NMOOqHY-1B74ZdxlrXJCKMFxRpS1lfbjuaQU; OptanonConsent=isIABGlobal=false&datestamp=Tue+Mar+09+2021+22:40:40+GMT-0600+(Central+Standard+Time)&version=6.10.0&hosts=&consentId=9e7df4cc-955c-4c63-9a12-7fde9aab5dd4&interactionCount=0&landingPath=NotLandingPage&AwaitingReconsent=false&groups=BG10:1,C0003:1,C0002:1,C0001:1,C0004:1',
	'referer': 'https://www.yelp.com/collection/djWWa-tq8K_5y8BVc38ttg',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'same-origin',
	'sec-gpc': '1',
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36',
	'x-requested-with': 'XMLHttpRequest'
}

req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
# print(soup.prettify())
print(soup)

# for list_markup in soup:
# 	if list_markup != "":
# 		print(list_markup)

div = soup.select("[class='collection-container u-flex']")

# print(div)

a_tags = soup.select("[data-analytics-label='biz-name']")
print(a_tags)

# href = soup.select("[href]")
# print(href)

list_of_biz_names = []


def get_biz_names():
	length = len(a_tags)
	print(length)
	next_biz = 0
	while next_biz < length:
		for biz in a_tags:
			a_tags_list = a_tags[next_biz]
			print(a_tags_list)
			biz_name = a_tags_list["href"]
			biz_name_stripped = biz_name.strip("/biz/")
			print(biz_name_stripped)
			next_biz += 1
			list_of_biz_names.append(biz_name_stripped)

	return list_of_biz_names


get_biz_names()


print(list_of_biz_names)


