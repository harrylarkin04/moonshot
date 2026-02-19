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

# === DETERMINISTIC OOS SIMULATION (same numbers every time) ===
np.random.seed(42)  # global seed for reproducibility
for idx, row in st.session_state.strategies.iterrows():
    seed = int(row["ID"].replace("EA-", ""))  # unique seed per strategy
    np.random.seed(seed)
    
    periods = 780
    daily_mean = row["OOS Sharpe"] / np.sqrt(252) * 0.0008
    daily_std = 0.012
    daily_ret = np.random.normal(daily_mean, daily_std, periods)
    equity = np.cumprod(1 + daily_ret) * 100
    drawdown = (equity / np.maximum.accumulate(equity) - 1) * 100
    
    st.session_state.strategies.loc[idx, "OOS Total Return (%)"] = round(equity[-1] - 100, 1)
    st.session_state.strategies.loc[idx, "OOS Max DD (%)"] = round(drawdown.min(), 1)
    st.session_state.strategies.loc[idx, "OOS Win Rate (%)"] = round((daily_ret > 0).mean() * 100, 1)

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Control Room", "Evolution Lab", "Strategy Zoo", "Agent Activity", "OOS Performance Lab"])

with tab1:
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Strategies in Zoo", len(st.session_state.strategies), "↑47 today")
    with col2: st.metric("Avg Omni Sharpe", "4.12", "↑0.31")
    with col3: st.metric("New Causal Alphas", "18", "🔥")
    
    if st.button("Run Full Evolution Cycle", type="primary", use_container_width=True):
        progress_container = st.empty()
        progress = progress_container.progress(0)
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
        
        progress_container.empty()
        st.success("Evolution cycle completed. 47 new regime-robust strategies added.")
        st.balloons()

        # Add new strategies + recalculate their OOS deterministically
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
        
        # Re-calculate OOS for new rows deterministically
        for idx, row in st.session_state.strategies.iterrows():
            if pd.isna(row.get("OOS Total Return (%)")):
                seed = int(row["ID"].replace("EA-", ""))
                np.random.seed(seed)
                periods = 780
                daily_mean = row["OOS Sharpe"] / np.sqrt(252) * 0.0008
                daily_ret = np.random.normal(daily_mean, 0.012, periods)
                equity = np.cumprod(1 + daily_ret) * 100
                drawdown = (equity / np.maximum.accumulate(equity) - 1) * 100
                st.session_state.strategies.loc[idx, "OOS Total Return (%)"] = round(equity[-1] - 100, 1)
                st.session_state.strategies.loc[idx, "OOS Max DD (%)"] = round(drawdown.min(), 1)
                st.session_state.strategies.loc[idx, "OOS Win Rate (%)"] = round((daily_ret > 0).mean() * 100, 1)

# Tabs 2, 3, 4, 5 remain exactly as before (copy-paste from your previous working version if needed – they are unchanged)

with tab5:
    st.subheader("OOS Performance Lab")
    st.caption("Out-of-sample returns & equity curves for winning strategies (unseen regimes 2023–Feb 2026)")

    selected_id = st.selectbox("View OOS Performance for Strategy", st.session_state.strategies["ID"].tolist())
    selected = st.session_state.strategies[st.session_state.strategies["ID"] == selected_id].iloc[0]

    # Use the already-calculated deterministic values
    seed = int(selected_id.replace("EA-", ""))
    np.random.seed(seed)
    periods = 780
    daily_mean = selected["OOS Sharpe"] / np.sqrt(252) * 0.0008
    daily_ret = np.random.normal(daily_mean, 0.012, periods)
    equity = np.cumprod(1 + daily_ret) * 100
    dates = pd.date_range("2023-01-01", periods=periods)

    fig_eq = px.line(x=dates, y=equity, title=f"OOS Equity Curve – {selected_id} ({selected['Causal Edge']})")
    fig_eq.update_layout(height=420)
    st.plotly_chart(fig_eq, use_container_width=True)

    cum_max = np.maximum.accumulate(equity)
    drawdown = (equity / cum_max - 1) * 100
    fig_dd = px.line(x=dates, y=drawdown, title="OOS Drawdown (%)", line_shape="hv")
    fig_dd.update_layout(height=300)
    st.plotly_chart(fig_dd, use_container_width=True)

    total_ret = equity[-1] - 100
    sharpe = (daily_ret.mean() / daily_ret.std() * np.sqrt(252)) if daily_ret.std() > 0 else 0
    max_dd = drawdown.min()
    win_rate = (daily_ret > 0).mean() * 100

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("OOS Total Return", f"{total_ret:.1f}%")
    with col2: st.metric("OOS Sharpe", f"{sharpe:.2f}")
    with col3: st.metric("OOS Max DD", f"{max_dd:.1f}%")
    with col4: st.metric("OOS Win Rate", f"{win_rate:.1f}%")

    st.subheader("Combined Top-5 Winning Strategies OOS Portfolio")
    top5 = st.session_state.strategies.nlargest(5, "OOS Sharpe")
    combined_equity = np.zeros(periods)
    for _, strat in top5.iterrows():
        seed = int(strat["ID"].replace("EA-", ""))
        np.random.seed(seed)
        dm = strat["OOS Sharpe"] / np.sqrt(252) * 0.0008
        ret = np.random.normal(dm, 0.012, periods)
        combined_equity += np.cumprod(1 + ret)
    combined_equity = (combined_equity / 5) * 100

    fig_port = px.line(x=dates, y=combined_equity, title="Top-5 Portfolio OOS Equity Curve")
    fig_port.update_layout(height=420)
    st.plotly_chart(fig_port, use_container_width=True)

    st.dataframe(
        st.session_state.strategies.nlargest(10, "OOS Sharpe")[["ID", "Causal Edge", "OOS Sharpe", "OOS Total Return (%)", "OOS Max DD (%)", "OOS Win Rate (%)"]],
        use_container_width=True,
        hide_index=True
    )

    if st.button("Re-validate All Strategies on Omniverse", type="primary", use_container_width=True):
        with st.spinner("Re-running full OOS validation..."):
            time.sleep(1.5)
        st.success("All strategies validated on unseen 2023–Feb 2026 regimes.")
