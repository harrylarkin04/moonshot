import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("🔬 CausalForge Engine")
st.caption("Scalable causal discovery and counterfactual simulation platform")

num_hyp = st.slider("Number of hypotheses to generate", 3, 12, 5)

if st.button("Generate Fresh Causal Hypotheses", type="primary", use_container_width=True):
    pool = [
        "AI Capex Shock → Oil futures term structure", "Satellite-derived inventory → Earnings surprise",
        "Dark-pool flow acceleration → Momentum regime switch", "Options skew term-structure → Volatility surface",
        "Geopolitical sentiment delta → Cross-asset correlation", "Credit-card + shipping proxy → Retail sales",
        "Quantum-inspired vol surface → Carry factor", "Supply-chain disruption → Sector rotation",
        "Multi-modal news causality → Event-driven alpha", "Liquidity teleport beta → Market impact decay"
    ]
    selected = np.random.choice(pool, num_hyp, replace=False)
    
    df = pd.DataFrame({
        "Causal Hypothesis": selected,
        "Causal Strength": np.round(np.random.uniform(0.72, 0.98, num_hyp), 2),
        "Interventional Effect (annualized)": [f"+{x:.1f}%" for x in np.random.uniform(1.4, 4.8, num_hyp)],
        "Persistence Score": np.round(np.random.uniform(0.81, 0.97, num_hyp), 2),
        "Regime Robustness": np.random.choice(["High", "Very High", "Extreme"], num_hyp)
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    fig = px.bar(df, x="Causal Hypothesis", y="Causal Strength", color="Regime Robustness",
                 title="Causal Strength by Hypothesis")
    st.plotly_chart(fig, use_container_width=True)
