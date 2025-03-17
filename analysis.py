import yfinance as yf
import streamlit as st
from datetime import datetime
import plotly.graph_objects as go


end_date = datetime.today().strftime('%Y-%m-%d')

st.write("""
# 📈 Stock Price Viewer

Shown are the stock **closing price** and ***volume*** of Google!

""")

st.markdown(
    """
    <style>
    div[data-baseweb="select"] > div {
        cursor: pointer !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("Sidebar Menu")
selected_stock = st.sidebar.selectbox("**Famous Stock:**", ["AAPL", "TSLA", "GOOGL", "MSFT", 'AMZN', 'META', 'NFLX', 'NVDA'])

ticker_dict = {
    "AAPL": "Apple Inc.",
    "TSLA": "Tesla, Inc.",
    "GOOGL": "Alphabet Inc.",
    "MSFT": "Microsoft Corp.",
    "AMZN": "Amazon.com, Inc.",
    "META": "Meta Platforms, Inc.",
    "NFLX": "Netflix, Inc.",
    "NVDA": "NVIDIA Corporation",
}
st.sidebar.title("Available Stocks")

for ticker, name in ticker_dict.items():
    st.sidebar.write(f"**{ticker}** - {name}")

ticker = yf.Ticker(selected_stock)

print(ticker.info)

tickerDf = ticker.history(period='1d', start='2015-1-1', end=end_date)

st.line_chart(tickerDf.Close)
st.write(f"""
**Company** : {ticker.info.get('longName', 'N/A')}
""")

st.write(f"**Sector:** {ticker.info.get('sector', 'N/A')}")
st.write(f"**Market Cap:** {ticker.info.get('marketCap', 'N/A')}")
st.write(f"**Website:** {ticker.info.get('website', 'N/A')}")
st.write(f"**Region:** {ticker.info.get('region', 'N/A')}")