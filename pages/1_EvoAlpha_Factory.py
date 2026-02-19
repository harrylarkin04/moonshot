import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import random

st.title("🧬 EvoAlpha Factory")
st.caption("Autonomous multi-agent strategy evolution laboratory")

st.sidebar.header("Evolution Controls")
pop_size = st.sidebar.slider("Population Size", 200, 10000, 3500, 100)
gens = st.sidebar.slider("Generations", 5, 300, 120)
mut_rate = st.sidebar.slider("Mutation Rate", 0.01, 0.40, 0.18, 0.01)

if 'strategies' not in st.session_state:
    st.session_state.strategies = pd.DataFrame({
        "ID": [f"EA-{i:05d}" for i in range(1, 21)],
        "Causal Edge": ["AI Capex Shock", "Satellite Inventory", "Dark Pool Momentum", "Options Skew Term", 
                        "Geopolitical Delta", "Credit Card Proxy", "Shipping + Earnings", "Quantum Vol Surface"] * 2 + ["Multi-Modal News"] * 4,
        "Sharpe (Omni OOS)": np.round(np.random.uniform(2.4, 6.1, 20), 2),
        "Capacity ($B)": np.round(np.random.uniform(0.4, 18.0, 20), 1),
        "Decay Resistance": np.random.choice(["Extreme", "Very High", "High"], 20),
        "Age (days)": np.random.randint(1, 45, 20),
        "Status": np.random.choice(["Live", "Staging", "Breeding"], 20)
    })

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Control Room", "Evolution Lab", "Strategy Zoo", "Agent Activity", "OOS Performance Lab"])

# ====================== TAB 1: CONTROL ROOM ======================
with tab1:
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Strategies in Zoo", len(st.session_state.strategies), "↑47 today")
    with col2: st.metric("Avg Omni Sharpe", "4.12", "↑0.31")
    with col3: st.metric("New Causal Alphas", "18", "🔥")
    
    if st.button("Run Full Evolution Cycle", type="primary", use_container_width=True):
        with st.spinner("Researcher swarm mining literature → Coder agents generating code → CausalForge validating → Omniverse stress-testing..."):
            progress = st.progress(0)
            logs = [
                "Researcher agents scanning arXiv + SSRN + proprietary alt-data...",
                "Inverse RL extracting fund reward functions...",
                "Coder agents generating 3,472 new hypotheses...",
                "CausalForge testing 12,000 interventions...",
                "Omniverse running 2.4 million counterfactual paths...",
                "Evolutionary selection complete. 47 winners."
            ]
            for i, msg in enumerate(logs):
                time.sleep(0.55)
                progress.progress((i+1)/len(logs))
                st.info(msg)
        
        st.success("Evolution cycle completed. 47 new regime-robust strategies added.")
        
        new = pd.DataFrame({
            "ID": [f"EA-{i:05d}" for i in range(10000, 10047)],
            "Causal Edge": ["Novel " + x for x in ["Supply Chain Causality", "Sentiment Regime Switch", "Liquidity Teleport Beta", "Quantum-Inspired Carry", "Multi-Modal News Causality"] * 9 + ["Dark Pool Acceleration"] * 2],
            "Sharpe (Omni OOS)": np.round(np.random.uniform(3.1, 7.8, 47), 2),
            "Capacity ($B)": np.round(np.random.uniform(2.0, 25.0, 47), 1),
            "Decay Resistance": np.random.choice(["Extreme", "Very High"], 47),
            "Age (days)": 1,
            "Status": "Staging"
        })
        st.session_state.strategies = pd.concat([st.session_state.strategies, new], ignore_index=True)

# ====================== TAB 2: EVOLUTION LAB ======================
with tab2:
    fig_data = pd.DataFrame({
        "Generation": list(range(gens+1)),
        "Best Sharpe": 1.8 + np.cumsum(np.random.normal(0.045, 0.008, gens+1)),
        "Mean Sharpe": 1.4 + np.cumsum(np.random.normal(0.022, 0.006, gens+1)),
        "Population Diversity": np.linspace
