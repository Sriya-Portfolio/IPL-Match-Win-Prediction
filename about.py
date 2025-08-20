import streamlit as st

def about_page():
    st.title("🏏 About IPL Win Predictor")

    st.markdown("""
    ## **Overview**
    The **IPL Win Predictor** is a machine learning-inspired tool designed to estimate the probability of a team's victory in an ongoing IPL match. It considers various in-game factors, such as score, wickets lost, required run rate, recent momentum, and the impact of the toss decision, to provide a dynamic prediction.

    ## **Key Features**
    - 🏆 **Real-time Win Probability Calculation**: Predicts win chances based on match progress.
    - 📊 **Data-Driven Analysis**: Factors in momentum, required run rate, and top batsmen's performance.
    - 🏟️ **Venue & Toss Impact**: Adjusts calculations based on venue-specific trends.
    - 🔮 **Interactive UI**: Users can input match details to get instant predictions.

    ## **How It Works**
    The prediction is computed using a formula that evaluates:
    - **Current Score & Overs Completed**: Determines the current run rate.
    - **Required Run Rate (RRR) vs. Current Run Rate (CRR)**: Assesses the batting team's position.
    - **Momentum Factor**: Analyzes runs scored/conceded in the last 5 overs.
    - **Wicket Factor**: Accounts for the number of wickets lost.
    - **Top Batsmen’s Impact**: Weighs the contribution of the best-performing batsmen.
    - **Toss & Venue Influence**: Adjusts the prediction based on historical trends.

    ## **Why This Matters?**
    In the fast-paced world of **T20 cricket**, a single over can change the game’s outcome. This predictor helps fans, analysts, and fantasy league players get **data-backed insights** into match probabilities.

    ## **Disclaimer**
    This tool is a statistical estimator and does **not guarantee actual match outcomes**. Cricket is an unpredictable sport where external factors like weather, injuries, and individual performances play a huge role.

    """)