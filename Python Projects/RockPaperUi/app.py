import streamlit as st
import random

st.title("Rock Paper Scissor Game")

game_items = ["rock", "paper", "scissors"]
TOTAL_ROUNDS = 3

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0
if "round" not in st.session_state:
    st.session_state.round = 0
if "match_over" not in st.session_state:
    st.session_state.match_over = False


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

    st.write("You selected:", user)
    st.write("Computer selected:", computer)
    st.write("Result:", result)

    if result == "You Won":
        st.session_state.user_score += 1
    elif result == "Computer Won":
        st.session_state.computer_score += 1

    st.session_state.round += 1

    if st.session_state.round >= TOTAL_ROUNDS:
        st.session_state.match_over = True


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

st.divider()

st.write("Round:", st.session_state.round, "/", TOTAL_ROUNDS)

col1, col2 = st.columns(2)
col1.metric("Your Score", st.session_state.user_score)
col2.metric("Computer Score", st.session_state.computer_score)

if st.session_state.match_over:
    if st.session_state.user_score >= 2:
        st.success("You Won the Match!")
    elif st.session_state.computer_score >= 2:
        st.success("Computer Won the Match!")
    else:
        st.success("Match Tied!")

if st.button("Restart"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.session_state.round = 0
    st.session_state.match_over = False
    st.rerun()