import tweepy
import time
import requests
import bs4
import lxml

auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

api = tweepy.API(auth)

lastprice=0

while(True):
	res=requests.get("https://www.coindesk.com/price/bitcoin")
	soup = bs4.BeautifulSoup(res.text, 'lxml')
	price = float(soup.find("div", {"class": "price-large"}).text[1:].replace(',',''))
	if(price!=lastprice):
		msg=f"BTC price has changed from ${lastprice} to ${price}. "
		change=abs(lastprice-price)
		if(price>lastprice):
			msg+="An increase of "
		else:
			msg+="A decrease of "
		msg+=f"${price-lastprice}"
		api.update_status(msg)
	lastprice=price
	time.sleep(300000)