import streamlit as st

st.set_page_config(page_title="Quant Moonshot Platform", page_icon="📈", layout="wide")

st.markdown("""
<style>
.big-button {
    background-color: #00ff9d;
    color: black;
    font-size: 22px;
    font-weight: bold;
    padding: 30px;
    border-radius: 12px;
    text-align: center;
    margin: 15px 0;
}
.big-button:hover {
    background-color: #00cc7a;
}
</style>
""", unsafe_allow_html=True)

st.title("Quant Moonshot Platform")
st.caption("Autonomous quantitative systems • February 2026 • Public prototype demo")

st.markdown("### Choose a system to explore")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🧬 EvoAlpha Factory", key="btn1", use_container_width=True):
        st.switch_page("pages/1_EvoAlpha_Factory.py")
    st.caption("Autonomous strategy evolution lab")

with col2:
    if st.button("⚡ Liquidity Teleporter", key="btn2", use_container_width=True):
        st.switch_page("pages/2_Liquidity_Teleporter.py")
    st.caption("Zero-footprint execution engine")

with col3:
    if st.button("🔬 CausalForge Engine", key="btn3", use_container_width=True):
        st.switch_page("pages/3_CausalForge_Engine.py")
    st.caption("Causal discovery & counterfactuals")

col4, col5, _ = st.columns(3)

with col4:
    if st.button("🌌 Financial Omniverse", key="btn4", use_container_width=True):
        st.switch_page("pages/4_Financial_Omniverse.py")
    st.caption("Market world model simulator")

with col5:
    if st.button("👥 ShadowCrowd Oracle", key="btn5", use_container_width=True):
        st.switch_page("pages/5_ShadowCrowd_Oracle.py")
    st.caption("Real-time crowding & cascade predictor")

st.divider()
st.caption("**Prototype only** • Built as a personal demonstration • Code is proprietary and not for redistribution")
