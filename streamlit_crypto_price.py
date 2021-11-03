import streamlit as st
import pandas as pd

import yfinance as yf
import datetime
import time

st.title(f'Crypto Live Price App')

if 'now_plus_5' not in st.session_state:
    st.session_state['now_plus_5'] = str(datetime.datetime.now() + datetime.timedelta(minutes = 10))[11:-10]

interval = '1m'

period = '5m'

while True:
    
    if str(datetime.datetime.now())[11:-10] >= st.session_state.now_plus_5:

        st.error("Application timed out. Refresh to continue.")
        
    else:
        ticker_option = st.selectbox(
         'Select a crypto ticker to monitor.',
         ('BTC-USD', 'ETH-USD', 'DOGE-USD', 'BNB-USD'))
    
        input_data = yf.download(tickers = ticker_option, period = period, interval = interval, progress = False)[-1:]

        last_update = str(input_data.index[0])[11:-6]

        close = input_data['Close'][0]

        current_time = str(datetime.datetime.utcnow())[11:-7]

        st.text(f'Current Time (UTC): {current_time}')

        st.header(f'{ticker_option} Close: ${close}')

        st.header(f'Close Updated (UTC): {last_update}')

    time.sleep(.3)

    st.experimental_rerun()

