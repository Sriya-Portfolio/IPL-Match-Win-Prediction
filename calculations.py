import streamlit as st

def calculation_page():
    st.title("📘 IPL Win Probability Predictor - How It Works")

    st.markdown("## 🔍 **Understanding the Win Probability Calculation**")
    st.write("The IPL Win Predictor calculates the probability of a team winning based on various match factors.")

    st.markdown("### **1️⃣ Current Run Rate (CRR)**")
    st.write("**Definition:** Measures the batting team's scoring rate per over.")
    st.latex(r"CRR = \frac{\text{Current Score}}{\text{Overs Completed}}")

    st.markdown("**Example:**")
    st.write("Current Score = **100 runs**")
    st.write("Overs Completed = **10 overs**")
    st.latex(r"CRR = \frac{100}{10} = 10.00")

    st.markdown("---")

    st.markdown("### **2️⃣ Required Run Rate (RRR)**")
    st.write("**Definition:** The minimum scoring rate needed to achieve the target.")
    st.latex(r"RRR = \frac{\text{Target Score} - \text{Current Score}}{\text{Remaining Overs}}")

    st.markdown("**Example:**")
    st.write("Target Score = **180 runs**")
    st.write("Current Score = **100 runs**")
    st.write("Overs Completed = **10 overs**")
    st.write("Remaining Overs = **20 - 10 = 10**")
    st.latex(r"RRR = \frac{180 - 100}{10} = 8.00")

    st.markdown("---")

    st.markdown("### **3️⃣ Wicket Impact Factor**")
    st.write("**Definition:** Represents how much losing wickets affects the team's stability.")
    st.latex(r"Wicket Factor = 1 - \left( \frac{\text{Wickets Lost}}{10} \right)")

    st.markdown("**Example:**")
    st.write("Wickets Lost = **3**")
    st.latex(r"Wicket Factor = 1 - \left(\frac{3}{10}\right) = 0.70")

    st.markdown("---")

    st.markdown("### **4️⃣ Momentum Factor (Last 5 Overs Impact)**")
    st.write("**Definition:** Determines how well the team is performing in recent overs.")
    st.latex(r"Momentum Factor = \frac{\text{Runs Last 5 Overs} - \text{Runs Conceded Last 5 Overs}}{\text{Runs Last 5 Overs} + \text{Runs Conceded Last 5 Overs}}")

    st.markdown("**Example:**")
    st.write("Runs Scored in Last 5 Overs = **40**")
    st.write("Runs Conceded in Last 5 Overs = **30**")
    st.latex(r"Momentum Factor = \frac{40 - 30}{40 + 30} = 0.14")

    st.markdown("---")

    st.markdown("### **5️⃣ Batsmen Contribution Factor**")
    st.write("**Definition:** Measures how much the top two batsmen have contributed.")
    st.latex(r"Batsmen Factor = \frac{\text{Top 2 Batsmen Runs}}{\text{Current Score}}")

    st.markdown("**Example:**")
    st.write("Top 2 Batsmen Runs = **80**")
    st.write("Current Score = **100**")
    st.latex(r"Batsmen Factor = \frac{80}{100} = 0.80")

    st.markdown("---")

    st.markdown("### **7️⃣ Final Win Probability Calculation**")
    st.latex(r"""
    \text{Win Probability} = 50 + (\text{Momentum Weight} \times \text{Momentum Factor}) + 
    (10 \times \text{Batsmen Factor}) + (15 \times \text{Wicket Factor}) - 
    (10 \times \text{RRR Factor}) + \text{Toss Advantage}
    """)

    st.markdown("**Example Calculation:**")
    st.latex(r"""
    \text{Win Probability} = 50 + (15 \times 0.14) + (10 \times 0.80) + 
    (15 \times 0.70) - (10 \times (-0.25)) + 5
    """)
    st.latex(r"= 50 + 2.1 + 8 + 10.5 + 2.5 + 5 = 78.1\%")

    st.write("The batting team has a **78.1% probability of winning**, while the bowling team has **21.9% probability**.")

if __name__ == "__main__":
    calculation_page()
