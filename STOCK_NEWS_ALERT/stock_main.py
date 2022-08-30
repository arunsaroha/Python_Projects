import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
# stock
STOCK_API = "https://www.alphavantage.co/query"
STOCK_API_KEY = "CFZMBRI8939NE67B"
# news
NEWS_API = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "c492872b88d14dfe9b4352ff1bcd0ac1"
# twilio
ACCOUNT_SID = "AC4d7e9677916f84410cf37539fe2706b4"
AUTH_TOKEN = "5eb45760bad527247f269d6bb0ecb906"

PERCENT = 0.05

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol"  : STOCK_NAME,
    "apikey"  : STOCK_API_KEY,
}

stock_response = requests.get(url=STOCK_API, params=stock_parameters)
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_price = float(data_list[0]["4. close"])
yesyesterday_price = float(data_list[1]["4. close"])
diff = abs(yesterday_price - yesyesterday_price)

if diff >= PERCENT*yesterday_price:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    news_response = requests.get(url=NEWS_API_KEY, params=news_parameters)
    articles = news_response.json()["articles"][0:3]

    articles_list = [f"Headline: {item['title']}\n Brief: {item['description']}" for item in articles]
    print(articles_list)

    for article in articles_list:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=article,
            from_ = "***********",
            to = "***********",
        )

