import streamlit as st
import database as db
from pandas import DataFrame

st.set_page_config(page_title="Travel Manager", page_icon="🚌", layout="centered")

st.title("🚌 Travel Manager!")

form = st.form(key="annotation")

name = st.text_input(label="Enter your name: ")
mode = st.selectbox("Mode of transport: ", ["Car", "Bus"])
if mode == "Bus":
    routes = db.read_routes().keys()
    route = st.selectbox("Select route: ", routes)

    stops = db.read_routes()[route]
    stop = st.selectbox("Select stop: ", stops)
else:
    route = "None"
    stop = "None"

submit = st.button("Submit")


if submit:
    if not name:
        st.error("Please enter your name..!")
    elif name in db.fetch_users().keys():
        st.error("You have already submitted your data. Please contact the admin to reset your data..!")
    else:
        db.add_user(name, mode, route, stop)
        st.success("Successfully submitted your data..!")

st.write("### Admin Only: ")
key = st.text_input("Enter admin key: ")
if st.button("Show data"):
    if key.lower() == "admin":
        with st.spinner("Loading data..."):
            users = db.fetch_users()
            raw = []
            for user in users.keys():
                raw.append((user, users[user]["mode"], users[user]["route"], users[user]["stop"]))
            df = DataFrame(raw, columns=("Name", "Mode", "Route", "Stop"))
            df.index += 1
            st.dataframe(df)
    else:
        st.error("Verification failed...!")