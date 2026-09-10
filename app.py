import streamlit as st

st.set_page_config(
    page_title="Mini Business Management System",
    page_icon="🛍️"
)

st.title("🛍️ Mini Business Management System")
st.write("Welcome! Choose how you want to use the system.")

option = st.radio(
    "Main Menu",
    ["Seller", "Buyer"]
)

if option == "Seller":
    st.subheader("👩🏽‍💼 Seller Menu")

    st.write("Seller features:")
    st.write("• Add products")
    st.write("• Update products")
    st.write("• Remove products")
    st.write("• Restock products")
    st.write("• View current stock")
    st.write("• Manage expenses")
    st.write("• View sales/business summary")

elif option == "Buyer":
    st.subheader("🛒 Buyer Menu")

    st.write("Buyer features:")
    st.write("• View available products")
    st.write("• Add to cart")
    st.write("• View cart")
    st.write("• Remove from cart")
    st.write("• Checkout")