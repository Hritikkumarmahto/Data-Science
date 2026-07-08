import streamlit as st
import random

# -----------------------------
# Function to Generate Coupon
# -----------------------------
def generate_coupon():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"

    coupon = ''.join(random.choices(letters, k=4))
    coupon += ''.join(random.choices(numbers, k=4))

    return coupon


# -----------------------------
# Generate Coupons Once
# -----------------------------
if "coupons" not in st.session_state:

    coupons = []

    while len(coupons) < 4:
        code = generate_coupon()
        if code not in coupons:
            coupons.append(code)

    st.session_state.coupons = coupons
    st.session_state.winning_coupon = random.choice(coupons)
    st.session_state.checked = False


# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="Coupon Lucky Draw", page_icon="🎁")

st.title("🎁 Lucky Coupon Draw")

st.write("Select **one coupon** from the list below.")

selected_coupon = st.radio(
    "Choose your coupon",
    st.session_state.coupons
)

if st.button("Check Result"):

    st.session_state.checked = True

    if selected_coupon == st.session_state.winning_coupon:
        st.success("🎉 Congratulations! You won a prize!")
        st.balloons()
    else:
        st.error("😔 Better luck next time!")
        st.info(f"Winning Coupon was: **{st.session_state.winning_coupon}**")


# -----------------------------
# Play Again
# -----------------------------
if st.button("Generate New Coupons"):

    coupons = []

    while len(coupons) < 4:
        code = generate_coupon()
        if code not in coupons:
            coupons.append(code)

    st.session_state.coupons = coupons
    st.session_state.winning_coupon = random.choice(coupons)
    st.rerun()