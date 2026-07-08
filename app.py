import streamlit as st
import random
import time

st.set_page_config(page_title="Real-Time Dashboard", page_icon="📊")

st.title("📊 Real-Time Dashboard")
st.write("This dashboard displays randomly generated live data.")

placeholder = st.empty()

for i in range(10):
    value = random.randint(1, 100)

    with placeholder.container():
        st.metric(label="Current Value", value=value)
        st.progress(value)

    time.sleep(1)
