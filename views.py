from django.shortcuts import render

# Create your views here.
def home(request):
	import requests
	import json
	#cryptonewsdata
	api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api=json.loads(api_request.content)
	#cryptopricedata
	api_request_other=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,TRX &tsyms=USD")
	api_other=json.loads(api_request_other.content)
	return render(request,"home.html",{'api':api,'api_other':api_other})

def prices(request):
	flag=False
	if  request.method == "POST":
		import requests
		import json
		quote=request.POST['quote']
		quote=quote.upper()
		crypto_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+quote+"&tsyms=USD")
		crypto=json.loads(crypto_request.content)
		return render(request,'prices.html',{'quote':quote,'crypto':crypto})
	else:
		flag=True
		return render(request,"prices.html",{'flag':flag})