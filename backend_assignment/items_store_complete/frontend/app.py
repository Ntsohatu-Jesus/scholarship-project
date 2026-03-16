frontend/app.py

import streamlit as st
import requests
import pandas as pd

API = "http://127.0.0.1:8000"

st.title("Items Store Dashboard")

tab1, tab2, tab3 = st.tabs(
    ["Add Item", "Browse Items", "Statistics"]
)

# Add Item
with tab1:

    name = st.text_input("Name")
    price = st.number_input("Price", min_value=0.0)
    quantity = st.number_input("Quantity", min_value=0)
    category = st.text_input("Category")

    if st.button("Add Item"):

        item = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "category": category
        }

        requests.post(f"{API}/items", json=item)

        st.success("Item added")

# Browse Items
with tab2:

    res = requests.get(f"{API}/items")

    data = res.json()

    if data:
        st.dataframe(pd.DataFrame(data))

# Statistics
with tab3:

    res = requests.get(f"{API}/stats")

    stats = res.json()

    st.metric("Total Items", stats["total_items"])
    st.metric("Inventory Value", stats["inventory_value"])