import streamlit as st
import qrcode
from io import BytesIO
import uuid

def generate_qr(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    return qr.make_image(fill_color="black", back_color="white")

st.title("Metro & Cab Booking")
stations = ["ameerpet", "kphb", "jntu", "balanagar", "jubliee hills"]

name = st.text_input("Name")
source = st.selectbox("From station", stations)
destination = st.selectbox("To station", stations)
tickets = st.number_input("Tickets", min_value=1, value=1)
need_cab = st.radio("Do you need Cab?", ("Yes", "No"), index=1)
drop_loc = st.text_input("Enter Drop location") if need_cab == "Yes" else ""

if st.button("Book"):
    if not name or (need_cab == "Yes" and not drop_loc) or source == destination:
        st.error("Check inputs: Name, Drop Location, or Stations.")
    else:
        bid = str(uuid.uuid4())[:8]
        st.success(f"Booked! ID: {bid}")
        st.write(f"Name: {name} | From: {source} To: {destination} | Paid: {tickets * 30}")
        
        buf = BytesIO()
        generate_qr(f"ID:{bid}\n{name}").save(buf, format="PNG")
        st.image(buf.getvalue(), width=200)
