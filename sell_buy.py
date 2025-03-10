import os
import python_bithumb


result = {}
coin = "ONDO"
price = 1530
amount = 100
result["decision"] = "buy"

access = os.getenv("BITHUMB_ACCESS_KEY")
secret = os.getenv("BITHUMB_SECRET_KEY")

bithumb = python_bithumb.Bithumb(access, secret)
my_coin = bithumb.get_balance(coin)

print(result["decision"])

if result["decision"] == "buy":
    # print(bithumb.buy_market_order("KRW-"+coin, 550_000))
    print(bithumb.buy_limit_order("KRW-"+coin, price, amount))
elif result["decision"] == "sell":
    # print(bithumb.sell_market_order("KRW-"+coin,my_coin-300))
    print(bithumb.sell_limit_order("KRW-"+coin, price, amount))