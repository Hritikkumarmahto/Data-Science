import streamlit as st
import random

st.title("Rock Paper Scissor Game")

game_items = ["rock", "paper", "scissors"]
TOTAL_ROUNDS = 3

st.markdown("""
<style>
div.stButton > button {
    height: 60px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "round" not in st.session_state:
    st.session_state.round = 0
if "match_over" not in st.session_state:
    st.session_state.match_over = False
if "last_user" not in st.session_state:
    st.session_state.last_user = None
if "last_computer" not in st.session_state:
    st.session_state.last_computer = None
if "last_result" not in st.session_state:
    st.session_state.last_result = None


def winner(user, computer):
    if user == computer:
        return "Tie"
    elif user == "rock" and computer == "scissors":
        return "You Won"
    elif user == "paper" and computer == "rock":
        return "You Won"
    elif user == "scissors" and computer == "paper":
        return "You Won"
    else:
        return "Computer Won"


def play(user):
    computer = random.choice(game_items)
    result = winner(user, computer)

    st.session_state.last_user = user
    st.session_state.last_computer = computer
    st.session_state.last_result = result

    if result == "You Won":
        st.session_state.user_score += 1
    elif result == "Computer Won":
        st.session_state.computer_score += 1

    st.session_state.round += 1

    if st.session_state.round >= TOTAL_ROUNDS:
        st.session_state.match_over = True


main_col, score_col = st.columns([2, 1])

with main_col:
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Rock", disabled=st.session_state.match_over):
            play("rock")
    with col2:
        if st.button("Paper", disabled=st.session_state.match_over):
            play("paper")
    with col3:
        if st.button("Scissors", disabled=st.session_state.match_over):
            play("scissors")

    left, middle, right = st.columns([1, 2, 1])
    with middle:
        if st.session_state.last_result is not None:
            st.write("You selected:", st.session_state.last_user)
            st.write("Computer selected:", st.session_state.last_computer)
            st.write("Result:", st.session_state.last_result)

        if st.session_state.match_over:
            if st.session_state.user_score >= 2:
                st.success("You Won the Match!")
            elif st.session_state.computer_score >= 2:
                st.success("Computer Won the Match!")
            else:
                st.success("Match Tied!")

with score_col:
    st.write("Round:", st.session_state.round, "/", TOTAL_ROUNDS)
    c1, c2 = st.columns(2)
    c1.metric("You Won", st.session_state.user_score)
    c2.metric("Computer Won", st.session_state.computer_score)

if st.button("Restart"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.round = 0
    st.session_state.match_over = False
    st.session_state.last_user = None
    st.session_state.last_computer = None
    st.session_state.last_result = None
    st.rerun()