import streamlit as st
import random

def main():
    st.title("Guess the Number Game")
    
    if "target_number" not in st.session_state:
        st.session_state.target_number = random.randint(1, 100)
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    
    st.write("I've selected a number between 1 and 100. Try to guess it!")
    
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)
    
    if st.button("Check Guess"):
        st.session_state.attempts += 1
        
        if guess < st.session_state.target_number:
            st.warning("Too low! Try again.")
        elif guess > st.session_state.target_number:
            st.warning("Too high! Try again.")
        else:
            st.success(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            if st.button("Play Again"):
                st.session_state.target_number = random.randint(1, 100)
                st.session_state.attempts = 0
                st.experimental_rerun()

if __name__ == "__main__":
    main()
