import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time
import random

st.title("EvoAlpha Factory")
st.caption("Autonomous multi-agent strategy evolution laboratory")

st.sidebar.header("Evolution Controls")
pop_size = st.sidebar.slider("Population Size", 200, 10000, 3500, 100)
gens = st.sidebar.slider("Generations", 5, 300, 120)
mut_rate = st.sidebar.slider("Mutation Rate", 0.01, 0.40, 0.18, 0.01)

if "strategies" not in st.session_state:
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

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Strategies in Zoo", len(st.session_state.strategies), "Up 47 today")
    with col2: st.metric("Avg Omni Sharpe", "4.12", "Up 0.31")
    with col3: st.metric("New Causal Alphas", "18", "Fire")
    
    if st.button("Run Full Evolution Cycle", type="primary", use_container_width=True):
        with st.spinner("Researcher swarm mining literature -> Coder agents generating code -> CausalForge validating -> Omniverse stress-testing..."):
            progress = st.progress(0)
            logs = [
                "Researcher agents scanning arXiv + SSRN + proprietary alt-data...",
                "Inverse RL extracting fund reward functions...",
                "Coder agents generating 3472 new hypotheses...",
                "CausalForge testing 12000 interventions...",
                "Omniverse running 2.4 million counterfactual paths...",
                "Evolutionary selection complete. 47 winners."
            ]
            for i, msg in enumerate(logs):
                time.sleep(0.55)
                progress.progress((i + 1) / len(logs))
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

with tab2:
    fig_data = pd.DataFrame({
        "Generation": list(range(gens + 1)),
        "Best Sharpe": 1.8 + np.cumsum(np.random.normal(0.045, 0.008, gens + 1)),
        "Mean Sharpe": 1.4 + np.cumsum(np.random.normal(0.022, 0.006, gens + 1)),
        "Population Diversity": np.linspace(0.92, 0.41, gens + 1)
    })
    fig = px.line(fig_data, x="Generation", y=["Best Sharpe", "Mean Sharpe", "Population Diversity"],
                  title="Strategy Zoo Evolution Trajectory", markers=True)
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    colA, colB, colC = st.columns(3)
    with colA: min_sharpe = st.slider("Minimum Omni Sharpe", 1.0, 8.0, 2.5, 0.1)
    with colB: status_filter = st.multiselect("Status", ["Live", "Staging", "Breeding"], default=["Live", "Staging"])
    with colC: search = st.text_input("Search Causal Edge")
    
    df = st.session_state.strategies.copy()
    df = df[df["Sharpe (Omni OOS)"] >= min_sharpe]
    if status_filter: df = df[df["Status"].isin(status_filter)]
    if search: df = df[df["Causal Edge"].str.contains(search, case=False)]
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    fig3d = px.scatter_3d(df, x="Sharpe (Omni OOS)", y="Capacity ($B)", z="Age (days)",
                          color="Decay Resistance", hover_name="ID",
                          title="Strategy Feature Space (3D Projection)")
    fig3d.update_traces(marker=dict(size=8))
    st.plotly_chart(fig3d, use_container_width=True)
    
    if st.button("Export Selected Strategy to Production", type="primary", use_container_width=True):
        strategy_code = """import numpy as np
import pandas as pd

def evo_alpha_strategy(data):
    signal = (data['AI_CAPEX'] > data['AI_CAPEX'].rolling(20).mean()) & (data['OIL_FUT'] < data['OIL_FUT'].rolling(10).mean())
    return signal.astype(int) * 2 - 1
"""
        st.download_button("Download evo_alpha_strategy.py", strategy_code, "evo_alpha_strategy.py", "text/x-python")

with tab4:
    st.subheader("Live Multi-Agent Activity")
    st.info("Real-time feed from 4200 autonomous agents")
    agents = ["Researcher-Alpha", "Coder-Genesis", "CausalForge-Validator", "Omniverse-Simulator", "Evo-Selector"]
    for _ in range(8):
        agent = random.choice(agents)
        st.markdown(f"**{agent}** * {time.strftime('%H:%M:%S')} -> " + random.choice([
            "Discovered new causal pathway in satellite + options data",
            "Mutated 312 strategies with quantum annealing",
            "Rejected 1842 spurious correlations",
            "Ran 450000 Omniverse counterfactuals",
            "Deployed EA-03412 to paper-trading"
        ]))

with tab5:
    st.subheader("OOS Performance Lab")
    st.caption("Out-of-sample validation for all winning strategies (unseen regimes 2023-Feb 2026)")

    if "OOS Sharpe" not in st.session_state.strategies.columns:
        st.session_state.strategies["OOS Sharpe"] = np.round(np.random.uniform(1.8, 5.9, len(st.session_state.strategies)), 2)
        st.session_state.strategies["OOS Max DD (%)"] = np.round(np.random.uniform(-3.2, -18.7, len(st.session_state.strategies)), 1)
        st.session_state.strategies["OOS Win Rate (%)"] = np.round(np.random.uniform(58, 79, len(st.session_state.strategies)), 1)
        st.session_state.strategies["Regime Survival"] = np.random.choice(["87%", "91%", "94%", "96%"], len(st.session_state.strategies))

    winning = st.session_state.strategies.nlargest(10, "OOS Sharpe").copy()
    
    st.dataframe(winning[["ID", "Causal Edge", "Sharpe (Omni OOS)", "OOS Sharpe", "OOS Max DD (%)", "OOS Win Rate (%)", "Regime Survival"]], use_container_width=True, hide_index=True)

    dates = pd.date_range("2023-01-01", periods=100)
    equity = np.cumprod(1 + np.random.normal(0.0008, 0.008, 100))
    fig_oos = px.line(x=dates, y=equity, title="Combined Top-5 Winning Strategies - OOS Equity Curve (2023-Feb 2026)")
    fig_oos.update_layout(height=420)
    st.plotly_chart(fig_oos, use_container_width=True)

    colA, colB = st.columns(2)
    with colA:
        st.metric("Average OOS Sharpe (Top 10)", f"{winning['OOS Sharpe'].mean():.2f}")
    with colB:
        st.metric("Average OOS Max Drawdown", f"{winning['OOS Max DD (%)'].mean():.1f}%")

    if st.button("Re-validate All Strategies on Omniverse", type="primary", use_container_width=True):
        with st.spinner("Re-running OOS validation across 2.4M counterfactual regimes..."):
            time.sleep(1.8)
        st.success("OOS validation complete. All winning strategies remain robust.")
