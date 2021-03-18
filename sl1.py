import yfinance as yf
import streamlit as st

from yahoo_fin import stock_info




st.sidebar.header("User input bar")

tickerSymbol = st.sidebar.selectbox(
    "Which Ticker would you like to see?",
    stock_info.tickers_sp500())


st.write(
    "# Simple Stock Price App\n"
    f"Shown are the stock closing price and volume of {tickerSymbol}"
    )

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")

st.line_chart(tickerDf.Close)

st.write("""
## Closing Volume
""")
st.line_chart(tickerDf.Volume)
