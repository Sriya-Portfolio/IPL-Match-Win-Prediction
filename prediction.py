import streamlit as st


teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore',
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings',
         'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

def calculate_toss_advantage(host_city, toss_decision):
    # City-wise preferred toss decision (bat first or chase (bowling))
    city_trends = {
        'Hyderabad': 'Chase', 'Bangalore': 'Chase', 'Mumbai': 'Chase', 'Indore': 'Bat', 'Kolkata': 'Bat',
        'Delhi': 'Bat', 'Chandigarh': 'Bat', 'Jaipur': 'Bat', 'Chennai': 'Bat', 'Cape Town': 'Chase',
        'Port Elizabeth': 'Bat', 'Durban': 'Chase', 'Centurion': 'Chase', 'East London': 'Bat',
        'Johannesburg': 'Chase', 'Kimberley': 'Bat', 'Bloemfontein': 'Bat', 'Ahmedabad': 'Bat',
        'Cuttack': 'Bat', 'Nagpur': 'Bat', 'Dharamsala': 'Chase', 'Visakhapatnam': 'Bat', 'Pune': 'Bat',
        'Raipur': 'Bat', 'Ranchi': 'Bat', 'Abu Dhabi': 'Chase', 'Sharjah': 'Chase', 'Mohali': 'Bat',
        'Bengaluru': 'Chase'
    }
    
    expected_decision = city_trends.get(host_city, None)
    if expected_decision is None:
        return 0
    
    toss_weight = 5 if host_city in ["Mumbai", "Bangalore", "Chennai", "Kolkata"] else 2
    
    return toss_weight if toss_decision == expected_decision else -toss_weight

def calculate_win_probability(target, current_score, overs_completed, wickets_lost, 
                              runs_last_5, conceded_last_5, top_batsmen_runs, 
                              selected_city, bat_first):
    # Required Run Rate (rrr) & Current Run Rate (CRR)
    crr = current_score / overs_completed if overs_completed != 0 else 0
    total_over = 20  # since it is a T20 match
    remaining_overs = total_over - overs_completed if total_over - overs_completed != 0 else 1
    rrr = (target - current_score) / remaining_overs
    rrr_factor = 1 - (crr / rrr) if rrr != 0 else 0

    # Wicket impact factor
    total_wickets = 10
    wicket_factor = 1 - (wickets_lost / total_wickets)

    # Last 5 overs impact (Momentum Factor)
    if (runs_last_5 + conceded_last_5) != 0:
        momentum_factor = (runs_last_5 - conceded_last_5) / (runs_last_5 + conceded_last_5)
    else:
        momentum_factor = 0
   
    # Adjusting momentum factor weight based on match conditions
    momentum_weight = 15 if target >= 180 or overs_completed >= 15 else 10
    
    # Top 2 batsmen contribution
    batsmen_factor = (top_batsmen_runs / current_score) if current_score != 0 else 0

    # Toss & Venue impact
    host_city = selected_city
    toss_decision = bat_first
    toss_advantage = calculate_toss_advantage(host_city, toss_decision)

    # Final win probability formula
    win_percent = 50 + (momentum_weight * momentum_factor) + (10 * batsmen_factor) \
                  + (15 * wicket_factor) - (10 * rrr_factor) + (toss_advantage)

    batting_win_probability = max(0, min(100, win_percent))  # Ensuring probability is within [0,100]
    bowling_win_probability = 100 - batting_win_probability

    return batting_win_probability, bowling_win_probability

def prediction_page():

    st.title('🏏 IPL Win Predictor')

    col1, col2 = st.columns(2)
    with col1:
        batting_team = st.selectbox('Select the batting team', sorted(teams))
    with col2:
        bowling_team = st.selectbox('Select the bowling team', sorted(teams))

    selected_city = st.selectbox('Select host city', sorted(cities))
    target = st.number_input('🎯 Target Score', min_value=1)

    col3, col4, col5 = st.columns(3)
    with col3:
        score = st.number_input('🏆 Current Score', min_value=0)
    with col4:
        overs = st.number_input('🔄 Overs Completed', min_value=0, max_value=20)
    with col5:
        wickets = st.number_input('❌ Wickets Lost', min_value=0, max_value=10)

    runs_last_5 = st.number_input('🔥 Runs in Last 5 Overs', min_value=0)
    conceded_last_5 = st.number_input('🛡️ Runs Conceded in Last 5 Overs', min_value=0)
    top_batsmen_runs = st.number_input('🏏 Top 2 Batsmen Runs', min_value=0)
    toss_winner = st.selectbox('🪙 Toss Winner', ['Batting Team', 'Bowling Team', 'Other'])
    bat_first = st.radio("🏏 Toss Decision?", ["Bat", "Bowl"])

    if st.button('🔮 Predict Probability'):
        # Process Toss Decision
        toss_winner_decision_matches_batting_order = (
            (toss_winner == 'Batting Team' and bat_first == 'Bat') or
            (toss_winner == 'Bowling Team' and bat_first == 'Bowl')
        )

        if toss_winner_decision_matches_batting_order:
            st.info("✅ The toss winner's decision aligns with their batting order strategy.")
        else:
            st.warning("⚠️ The toss winner's decision does not match the usual pattern.")

        # **Make predictions using fully dynamic formula**
        win_prob, loss_prob = calculate_win_probability(
            target, score, overs, wickets, 
            runs_last_5, conceded_last_5, top_batsmen_runs, 
            selected_city, bat_first
        )

        # **Display results**
        st.header(f"🏆 {batting_team} Win Probability: {round(win_prob, 2)}%")
        st.header(f"⚡ {bowling_team} Win Probability: {round(loss_prob, 2)}%")