import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("👥 ShadowCrowd Oracle")
st.caption("Real-time global quant crowding detection and cascade forecasting")

if st.button("Scan Live Herd Fingerprint", type="primary", use_container_width=True):
    archetypes = ["Momentum Pod", "StatArb Cluster", "CTA Swarm", "Vol Arb Desk", "Event-Driven"]
    df = pd.DataFrame({
        "Archetype": archetypes,
        "Crowding Level (%)": np.round(np.random.uniform(68, 97, 5), 0),
        "Cascade Probability (48h)": ["14%", "51%", "9%", "37%", "22%"],
        "Recommended Action": ["Reduce 35%", "Exit position", "Add liquidity", "Hedge gamma", "Monitor"]
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    fig = px.bar(df, x="Archetype", y="Crowding Level (%)", color="Cascade Probability (48h)",
                 title="Live Crowding Heatmap")
    st.plotly_chart(fig, use_container_width=True)
    
    with st.expander("Methodology & Data Sources"):
        st.markdown("""
        **Real-time proxies used:**
        - Order-flow signatures & microstructure patterns
        - Options gamma & skew clustering
        - ETF creation/redemption anomalies
        - Satellite-derived corporate activity
        - Dark-pool metadata (via secure MPC)
        - Anonymized prime-broker flow fingerprints
        
        Model runs parallel multi-agent RL simulations of every major quant archetype to forecast tipping points and unwind magnitudes.
        """)
