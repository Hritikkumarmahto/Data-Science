# Introduction to numpy
# motivation 
# essential fro working on machine learning and data science project 
# required when writing custom loss function building ml models from scratch without libraries like(sckit learn , tensor flow)


#-----------------------------Introduction to numpy----------------------------------------------

# Numpy ( Numerical python ) is a python library that is the core library for scientific computation in python

# it contains a collection of tools and techniques that can be use to solve mathematical models of problem in science and engineering 

# one of these tools is high performance multidimentional-array object that is a powerful data structure for the effecient computation of array and matrices 

# to work with these arrays, there is vast amount of high level mathematical function operate on these matrices and arrays

# numpy function much way faster like 10x or 20x compare to the code from scratch or custom code 


# ------------------------------------------ Why NUMMPY is importaint -------------------------------------

# 1. Model input need numpy array 
# - ML libraries like scikit-learn , Tensorflow, Pytorch , etc expect data in numpy array formate
# - even pandas and Opencv internally rely on Numpy arrays 

# 2. Numpy is much faster for latge Nmerical computation 
# - Numpy is written in optimized c code under the hood
# - It supports :
#          - Matrix multiplication
#          - Dot products
#          - Broadcasting ( auto expedning arrays in operations)
# - Much faster then native loops or list in python

# 3. NUMPY handles N dimentiona arrays 
#  - NUMPY can create and operate on arrays of any dimention (1D, 2D, 3D, ...,nD).
#  - Useful for scientific computation 
#  - Deep learning tensor 
#  - Image preprocessing



# 4. You need Numpy to build cutstom Algorithms   
#  - for hands on ML model from scratch , Numpy is essential 
#  - we will use it for 
#           - Linear regression 
#           - Gradient Decent
#           - Backpropagation
#           - Activation Function 



# -------------------------- NUMPY VS PANDAS -------------------

# use pandas to prepare data and use numpy to power th math behind ML.

# Feature     |      NUMPY                 |       Pandas                           |
#-----------------------------------------------------------------------------------|
# Focus       |-Numerical computation      | - Tebular data analysis                |
#-----------------------------------------------------------------------------------|
# structure   |- N dimentional arrays      | - Leveled 1D/2D tables (series or data)|
#-----------------------------------------------------------------------------------|
# performance |- very fast, low level      | - Build in the top of numpy            |
#-----------------------------------------------------------------------------------|
# Use case    |- Math behind ML            | - EDA , Data wargling preprocessing    |
# ----------------------------------------------------------------------------------|


# --------------------- Why Numpy is more memory efficient then python list ------------------------

# Python list memory model 
# 1. stores reference( pointer ) to a seprate python int object
# 2. Each int object has metadata
#       . Type information
#       . Reference count
#       . Value
# 3. High overhead, especially for large arrays.
# 4. Not cache friendly- Elements are scattered in the memory 

# NumPy Array Memory Model
# 1. Store data in contigeous memory C style memory block
# 2. Only stores raw values (eg. int32, float64 ) - no per element metadata
# 3. very compact : no need to store Python object info for each element 
# 4. cache friendly and cpu efficient 
# 5. Enables vectorized operations, SIMD, and Broadcasting 


# Result :
# 1. Numpy array uses signlificantly less memory then python list 
# 2. Ideal for large scale numerical data , specially in machine learning and scientific computing
 


import random

game_items = ["rock", "paper", "scissors"]

def play_game():
    print("""
Enter your selection
      1. rock
      2. paper
      3. scissors
      """)
    
    user_choice = input("Enter your choice by typing (rock/paper/scissors): ").lower()
    
    computer_choice = random.choice(game_items)
    print(f"Computer chose: {computer_choice}")

    if computer_choice == user_choice:
        print("Tie!")
    elif computer_choice == "scissors" and user_choice == "rock":
        print("You won!")
    elif computer_choice == "scissors" and user_choice == "paper":
        print("Better luck next time.")
    elif computer_choice == "rock" and user_choice == "paper":
        print("You won!")
    elif computer_choice == "rock" and user_choice == "scissors":
        print("Better luck next time.")
    elif computer_choice == "paper" and user_choice == "rock":
        print("Better luck next time.")
    elif computer_choice == "paper" and user_choice == "scissors":
        print("You won!")
    else:
        print("Invalid choice! Go play cricket.")

while True:
    play_game()
    retry = input("\nDo you want to play again? (y/n): ").lower()
    if retry != 'y':
        print("Thank you for playing!")
        break
