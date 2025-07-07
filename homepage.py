import streamlit as st

st.set_page_config(page_title="Restaurant Dashboard", layout="centered")

st.title("🍽️ Restaurant Projects Homepage")
st.markdown("Welcome! Choose a project to explore:")

st.markdown("---")

st.subheader("📋 Billing App")
st.write("Track orders and generate receipts.")
st.link_button("Open Billing App", "https://restaurant-billing-web-itj8iuswgm5r5l7wsbvpyh.streamlit.app/", type="primary")

st.subheader("📅 Reservation App")
st.write("Manage customer reservations and available slots.")
st.link_button("Open Reservation App", "https://restaurant-reservation-web-2ncchdrb5agdghq8nyd8od.streamlit.app/")

st.subheader("📦 Inventory App")
st.write("Track kitchen stock levels and view usage reports.")
st.link_button("Open Inventory App", "https://restaurant-inventory-web-a4rz7obrp58krj7hhewslk.streamlit.app/")
