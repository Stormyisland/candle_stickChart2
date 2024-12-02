from tradingview_ta import TA_Handler, Exchange, Interval

BTC = TA_Handler(
    symbol="BTCUSDT",
    screener="crypto",
    exchange="binance",
    interval=Interval.INTERVAL_1_MINUTE,
    
)

price = BTC.get_analysis().indicators['high']
rsi = BTC.get_analysis().indicators['RSI']
print("BTC price is ", price,  "The RSI is ",rsi)