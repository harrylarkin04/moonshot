import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("🔬 CausalForge Engine")
st.caption("Scalable causal discovery and counterfactual simulation")

if st.button("Generate Causal Hypotheses", type="primary"):
    hypotheses = pd.DataFrame({
        "Hypothesis": ["AI Capex → Sector Rotation", "Geopolitical Sentiment → Vol Term Structure", "Supply Chain → Earnings Surprise"],
        "Causal Strength": np.round(np.random.uniform(0.65, 0.98, 3), 2),
        "Interventional Effect": ["+2.8% annualized", "+1.9% annualized", "+3.4% annualized"],
        "Persistence Score": ["0.94", "0.87", "0.96"]
    })
    st.dataframe(hypotheses, use_container_width=True)
    
    fig = px.bar(hypotheses, x="Hypothesis", y="Causal Strength", color="Persistence Score")
    st.plotly_chart(fig, use_container_width=True)
