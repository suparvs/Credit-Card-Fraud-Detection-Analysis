
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os


st.set_page_config(
    page_title="FraudSense AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# ADVANCED CYBERPUNK UI
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Poppins:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: white;
}

/* MAIN BACKGROUND */
.stApp {

    background:
    radial-gradient(circle at top left, rgba(255,0,128,0.25), transparent 25%),
    radial-gradient(circle at top right, rgba(0,255,255,0.18), transparent 25%),
    radial-gradient(circle at bottom left, rgba(138,43,226,0.20), transparent 30%),
    linear-gradient(135deg, #111827 0%, #1e1b4b 40%, #0f172a 100%);

    background-attachment: fixed;
}

/* REMOVE STREAMLIT HEADER */
header {
    visibility: hidden;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        rgba(30,41,59,0.95),
        rgba(17,24,39,0.95)
    );

    border-right: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(15px);
}

/* SIDEBAR TITLE */
.sidebar-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 30px;
    font-weight: 700;

    background: linear-gradient(90deg,#ff4b4b,#00f5ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 5px;
}

/* SECTION TITLE */
.section-title {

    font-family: 'Orbitron', sans-serif;
    font-size: 40px;
    font-weight: 700;

    background: linear-gradient(
        90deg,
        #ffffff,
        #00f5ff,
        #ff4b91
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;

    margin-bottom: 20px;
}

/* LIVE STATUS */
.live-box {

    background: rgba(0,255,140,0.15);
    border: 1px solid rgba(0,255,140,0.4);

    color: #7dffb8;

    padding: 12px 18px;
    border-radius: 50px;

    font-weight: 600;
    text-align: center;

    backdrop-filter: blur(12px);

    animation: pulse 2s infinite;
}

/* ANIMATION */
@keyframes pulse {

    0% {
        box-shadow: 0 0 0px rgba(0,255,140,0.4);
    }

    50% {
        box-shadow: 0 0 30px rgba(0,255,140,0.7);
    }

    100% {
        box-shadow: 0 0 0px rgba(0,255,140,0.4);
    }
}

/* METRIC CARDS */
.metric-card {

    position: relative;
    overflow: hidden;

    background: rgba(255,255,255,0.08);

    backdrop-filter: blur(20px);

    border-radius: 24px;

    padding: 25px;

    border: 1px solid rgba(255,255,255,0.12);

    box-shadow:
        0 8px 32px rgba(0,0,0,0.25);

    transition: 0.35s ease;
}

.metric-card:hover {

    transform: translateY(-6px) scale(1.02);

    box-shadow:
        0 0 35px rgba(0,245,255,0.25),
        0 0 25px rgba(255,75,145,0.25);
}

/* CARD GLOW */
.metric-card::before {

    content: '';

    position: absolute;

    width: 200px;
    height: 200px;

    background:
    radial-gradient(circle,
    rgba(255,255,255,0.18),
    transparent 70%);

    top: -70px;
    right: -70px;
}

/* METRIC TITLE */
.metric-title {

    color: #d1d5db;

    font-size: 15px;
    font-weight: 500;

    margin-bottom: 10px;
}

/* METRIC VALUE */
.metric-value {

    font-size: 46px;

    font-weight: 700;

    font-family: 'Orbitron', sans-serif;

    color: white;
}

/* COLORS */
.metric-danger {

    color: #ff5c8a;

    text-shadow:
        0 0 12px rgba(255,92,138,0.6);
}

.metric-success {

    color: #66ffb2;

    text-shadow:
        0 0 12px rgba(102,255,178,0.5);
}

/* CHART CARDS */
.chart-card {

    background: rgba(255,255,255,0.06);

    backdrop-filter: blur(18px);

    border-radius: 24px;

    padding: 22px;

    margin-top: 20px;

    border: 1px solid rgba(255,255,255,0.10);

    box-shadow:
        0 8px 32px rgba(0,0,0,0.18);

    transition: 0.3s ease;
}

.chart-card:hover {

    transform: translateY(-3px);

    border: 1px solid rgba(255,255,255,0.18);
}

/* DATAFRAME */
[data-testid="stDataFrame"] {

    border-radius: 18px;
    overflow: hidden;
}

/* SCROLLBAR */
::-webkit-scrollbar {

    width: 10px;
}

::-webkit-scrollbar-thumb {

    background:
    linear-gradient(#00f5ff,#ff4b91);

    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================
@st.cache_data
def load_data():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    csv_path = os.path.join(
        BASE_DIR,
        "credit_card_fraud_10k.csv"
    )

    return pd.read_csv(csv_path)

df = load_data()

# =========================================================
# SIDEBAR
# =========================================================
# =========================================================
# SIDEBAR STYLING
# =========================================================

st.markdown("""
<style>

/* SIDEBAR */
section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        rgba(8,12,20,0.98),
        rgba(15,23,42,0.98)
    );

    border-right: 1px solid rgba(255,255,255,0.10);

    backdrop-filter: blur(18px);

    box-shadow:
        5px 0 25px rgba(0,0,0,0.35);
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] .stMarkdown,
section[data-testid="stSidebar"] span {

    color: #f3f4f6 !important;
    font-weight: 500;
}

/* RADIO BUTTONS */
section[data-testid="stSidebar"] .stRadio label {

    color: white !important;
}

/* SLIDER */
section[data-testid="stSidebar"] .stSlider {

    padding-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR CONTENT
# =========================================================

st.sidebar.markdown("""
<div class='sidebar-title'>🛡 FraudSense</div>
<div class='sidebar-sub'>
AI Fraud Detection & Analytics
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio(
    "Navigation",
    [
        "Overview",
        "Fraud Analysis",
        "Risk Insights",
        "AI Insights"
    ]
)

st.sidebar.markdown("---")

# =========================================================
# FILTERS
# =========================================================
st.sidebar.subheader("Filters")

min_amt, max_amt = st.sidebar.slider(
    "Transaction Amount",
    float(df["amount"].min()),
    float(df["amount"].max()),
    (
        float(df["amount"].min()),
        float(df["amount"].max())
    )
)

hour_range = st.sidebar.slider(
    "Transaction Hour",
    0, 23, (0, 23)
)

filtered_df = df[
    (df["amount"] >= min_amt) &
    (df["amount"] <= max_amt) &
    (df["transaction_hour"] >= hour_range[0]) &
    (df["transaction_hour"] <= hour_range[1])
].copy()

# =========================================================
# RISK SCORE
# =========================================================
filtered_df["risk_score"] = 0

filtered_df["risk_score"] += filtered_df["foreign_transaction"]
filtered_df["risk_score"] += filtered_df["location_mismatch"]

filtered_df["risk_score"] += (
    filtered_df["velocity_last_24h"] >
    filtered_df["velocity_last_24h"].quantile(0.90)
).astype(int)

filtered_df["risk_score"] += (
    filtered_df["device_trust_score"] <
    filtered_df["device_trust_score"].quantile(0.10)
).astype(int)

# =========================================================
# TOP HEADER
# =========================================================
colx, coly = st.columns([5,1])

with colx:
    st.markdown(
        "<div class='section-title'>Fraud Intelligence Command Center</div>",
        unsafe_allow_html=True
    )

with coly:
    st.markdown(
        "<div class='live-box'>🟢 LIVE</div>",
        unsafe_allow_html=True
    )

# =========================================================
# HERO SECTION
# =========================================================
st.markdown("""
<div style="
padding:18px;
border-radius:20px;
background:linear-gradient(90deg,#ff004c22,#00ffd522);
border:1px solid rgba(255,255,255,0.08);
margin-bottom:25px;
">

<h2 style="
margin:0;
font-family:Orbitron;
font-size:28px;
">
⚡ Real-Time Fraud Detection Intelligence
</h2>

<p style="color:#b0b0b0;">
AI-powered financial threat monitoring system with live anomaly detection
</p>

</div>
""", unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================
total_transactions = len(filtered_df)
fraud_cases = int(filtered_df["is_fraud"].sum())
legit_cases = total_transactions - fraud_cases
fraud_rate = round((fraud_cases / total_transactions) * 100, 2)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Transactions</div>
        <div class="metric-value">{total_transactions:,}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Fraud Cases</div>
        <div class="metric-value metric-danger">{fraud_cases:,}</div>
        <div style="color:#ff7b7b;">
        ↑ {fraud_rate}% suspicious
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Legitimate</div>
        <div class="metric-value metric-success">{legit_cases:,}</div>
        <div style="color:#52ff9e;">
        {(100-fraud_rate):.2f}% safe
        </div>
    </div>
    """, unsafe_allow_html=True)

peak_hour = (
    filtered_df.groupby("transaction_hour")["is_fraud"]
    .mean()
    .idxmax()
)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Peak Risk Hour</div>
        <div class="metric-value">{peak_hour}:00</div>
        <div style="color:#ff4b4b;">
        High Threat Window
        </div>
    </div>
    """, unsafe_allow_html=True)

# =========================================================
# OVERVIEW
# =========================================================
if menu == "Overview":

    left, right = st.columns([2,1])

    with left:

        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

        fraud_counts = filtered_df["is_fraud"].value_counts()

        fig = go.Figure()

        fig.add_trace(go.Bar(
            x=["Legitimate", "Fraud"],
            y=[
                fraud_counts.get(0,0),
                fraud_counts.get(1,0)
            ]
        ))

        fig.update_layout(
            title="Fraud vs Legitimate Transactions",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with right:

        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

        fig2 = px.histogram(
            filtered_df,
            x="amount",
            nbins=30,
            title="Transaction Amount Distribution"
        )

        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            height=450
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

    st.subheader("📡 Live Transaction Feed")

    st.dataframe(
        filtered_df.head(50),
        use_container_width=True
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# FRAUD ANALYSIS
# =========================================================
elif menu == "Fraud Analysis":

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

        hour_pattern = (
            filtered_df.groupby("transaction_hour")["is_fraud"]
            .mean() * 100
        )

        fig = px.line(
            x=hour_pattern.index,
            y=hour_pattern.values,
            markers=True,
            title="Fraud Trend by Hour"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

        merchant = (
            filtered_df.groupby("merchant_category")["is_fraud"]
            .mean()
            .sort_values(ascending=False)
            .head(10)
        )

        fig2 = px.bar(
            merchant,
            orientation='h',
            title="Top Fraud Merchant Categories"
        )

        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            height=450
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# RISK INSIGHTS
# =========================================================
elif menu == "Risk Insights":

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

        risk_data = (
            filtered_df.groupby("risk_score")["is_fraud"]
            .mean() * 100
        )

        fig = px.bar(
            x=risk_data.index,
            y=risk_data.values,
            title="Risk Score vs Fraud Rate"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            height=450
        )

        st.plotly_chart(fig, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

    with col2:

        st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

        fig2 = px.box(
            filtered_df,
            x="is_fraud",
            y="device_trust_score",
            title="Device Trust Score Analysis"
        )

        fig2.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            height=450
        )

        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("</div>", unsafe_allow_html=True)

# =========================================================
# AI INSIGHTS
# =========================================================
# =========================================================
# AI INSIGHTS
# =========================================================
elif menu == "AI Insights":

    st.markdown("<div class='chart-card'>", unsafe_allow_html=True)

    st.subheader("🤖 AI Fraud Intelligence Insights")

    # =====================================================
    # AI SUMMARY METRICS
    # =====================================================

    insight_col1, insight_col2, insight_col3 = st.columns(3)

    suspicious_transactions = filtered_df[
        filtered_df["risk_score"] >= 3
    ].shape[0]

    foreign_risky = filtered_df[
        (filtered_df["foreign_transaction"] == 1) &
        (filtered_df["is_fraud"] == 1)
    ].shape[0]

    low_trust_devices = filtered_df[
        filtered_df["device_trust_score"] <
        filtered_df["device_trust_score"].quantile(0.25)
    ].shape[0]

    with insight_col1:
        st.metric(
            "⚠️ Suspicious Transactions",
            suspicious_transactions
        )

    with insight_col2:
        st.metric(
            "🌍 Foreign Fraud Cases",
            foreign_risky
        )

    with insight_col3:
        st.metric(
            "📱 Low Trust Devices",
            low_trust_devices
        )

    st.markdown("---")

    # =====================================================
    # AI GENERATED INSIGHTS
    # =====================================================

    insights = []

    # FRAUD RATE ANALYSIS
    if fraud_rate < 5:
        insights.append(
            f"🟢 Fraud activity is currently low with only {fraud_rate}% suspicious transactions detected."
        )

    elif fraud_rate < 15:
        insights.append(
            f"🟠 Moderate fraud activity detected. {fraud_rate}% transactions appear suspicious."
        )

    else:
        insights.append(
            f"🔴 High fraud activity detected! {fraud_rate}% transactions flagged as suspicious."
        )

    # =====================================================
    # PEAK RISK HOUR
    # =====================================================

    insights.append(
        f"⚠️ Peak fraud activity detected around {peak_hour}:00 hours indicating elevated threat activity."
    )

    # =====================================================
    # FOREIGN TRANSACTION ANALYSIS
    # =====================================================

    if foreign_risky > 0:
        insights.append(
            "🌍 Foreign transactions show elevated fraud probability and abnormal transaction behavior."
        )

    # =====================================================
    # LOCATION MISMATCH ANALYSIS
    # =====================================================

    location_fraud = filtered_df[
        (filtered_df["location_mismatch"] == 1) &
        (filtered_df["is_fraud"] == 1)
    ].shape[0]

    if location_fraud > 0:
        insights.append(
            "📍 Transactions with location mismatch are strongly associated with suspicious behavior patterns."
        )

    # =====================================================
    # DEVICE TRUST ANALYSIS
    # =====================================================

    if low_trust_devices > 0:
        insights.append(
            "📱 Low trusted devices contribute significantly to anomaly detection alerts."
        )

    # =====================================================
    # HIGH TRANSACTION VELOCITY ANALYSIS
    # =====================================================

    high_velocity = filtered_df[
        (filtered_df["velocity_last_24h"] >
         filtered_df["velocity_last_24h"].quantile(0.90)) &
        (filtered_df["is_fraud"] == 1)
    ].shape[0]

    if high_velocity > 0:
        insights.append(
            "⚡ Rapid transaction velocity indicates possible automated or bot-driven fraud attempts."
        )

    # =====================================================
    # HIGH RISK SCORE ANALYSIS
    # =====================================================

    high_risk = filtered_df[
        (filtered_df["risk_score"] >= 3) &
        (filtered_df["is_fraud"] == 1)
    ].shape[0]

    if high_risk > 0:
        insights.append(
            "🚨 Transactions with higher risk scores show strong fraud correlation."
        )

    # =====================================================
    # MERCHANT CATEGORY ANALYSIS
    # =====================================================

    top_category = (
        filtered_df.groupby("merchant_category")["is_fraud"]
        .mean()
        .idxmax()
    )

    insights.append(
        f"🛒 '{top_category}' merchant category currently shows the highest fraud tendency."
    )

    # =====================================================
    # AVERAGE FRAUD AMOUNT ANALYSIS
    # =====================================================

    avg_fraud_amount = filtered_df[
        filtered_df["is_fraud"] == 1
    ]["amount"].mean()

    insights.append(
        f"💳 Average fraudulent transaction amount detected: ${avg_fraud_amount:.2f}"
    )

    # =====================================================
    # SAFE TRANSACTION INSIGHT
    # =====================================================

    safe_rate = 100 - fraud_rate

    insights.append(
        f"✅ {safe_rate:.2f}% transactions are currently classified as legitimate and low-risk."
    )

    # =====================================================
    # DISPLAY AI INSIGHTS
    # =====================================================

    for insight in insights:
        st.info(insight)

    st.markdown("---")

    # =====================================================
    # AI THREAT LEVEL
    # =====================================================

    if fraud_rate < 5:
        st.success("🟢 AI Threat Level: LOW RISK")

    elif fraud_rate < 15:
        st.warning("🟠 AI Threat Level: MODERATE RISK")

    else:
        st.error("🔴 AI Threat Level: HIGH RISK")
        # =====================================================
# DETAILED FRAUD INVESTIGATION PANEL
# =====================================================

st.markdown("---")

st.subheader("🚨 Detailed Fraud Investigation Panel")

fraud_only_df = filtered_df[
    filtered_df["is_fraud"] == 1
].copy()

if len(fraud_only_df) > 0:

    selected_index = st.selectbox(
        "Select Fraud Transaction ID",
        fraud_only_df.index
    )

    txn = fraud_only_df.loc[selected_index]

    # ============================================
    # DYNAMIC RISK LEVEL
    # ============================================

    risk_percent = min(
        int((txn["risk_score"] / 4) * 100),
        100
    )

    if risk_percent >= 80:
        risk_level = "CRITICAL"
        risk_color = "red"

    elif risk_percent >= 60:
        risk_level = "HIGH"
        risk_color = "orange"

    elif risk_percent >= 40:
        risk_level = "MEDIUM"
        risk_color = "yellow"

    else:
        risk_level = "LOW"
        risk_color = "green"

    # ============================================
    # MAIN METRICS
    # ============================================

    dcol1, dcol2, dcol3, dcol4 = st.columns(4)

    with dcol1:
        st.metric(
            "💳 Amount",
            f"${txn['amount']:,.2f}"
        )

    with dcol2:
        st.metric(
            "⚠️ Risk Score",
            f"{risk_percent}%"
        )

    with dcol3:
        st.metric(
            "🚨 Threat Level",
            risk_level
        )

    with dcol4:
        st.metric(
            "🕒 Hour",
            f"{int(txn['transaction_hour'])}:00"
        )

    st.markdown("---")

    # ============================================
    # RISK GAUGE
    # ============================================

    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_percent,
        title={'text': "Fraud Probability"},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': risk_color},
            'steps': [
                {'range': [0, 40], 'color': "#1f2937"},
                {'range': [40, 70], 'color': "#374151"},
                {'range': [70, 100], 'color': "#7f1d1d"}
            ]
        }
    ))

    gauge.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        height=350
    )

    st.plotly_chart(
        gauge,
        use_container_width=True
    )

    # ============================================
    # WHY FRAUD HAPPENED
    # ============================================

    st.subheader("🧠 Why This Transaction Was Flagged")

    reasons = []

    if txn["foreign_transaction"] == 1:
        reasons.append(
            "🌍 Foreign transaction detected from unusual region."
        )

    if txn["location_mismatch"] == 1:
        reasons.append(
            "📍 Location mismatch identified between card usage locations."
        )

    if txn["velocity_last_24h"] > filtered_df[
        "velocity_last_24h"
    ].quantile(0.90):

        reasons.append(
            "⚡ Extremely high transaction velocity detected in last 24 hours."
        )

    if txn["device_trust_score"] < filtered_df[
        "device_trust_score"
    ].quantile(0.10):

        reasons.append(
            "📱 Device trust score is critically low."
        )

    if txn["amount"] > filtered_df[
        "amount"
    ].quantile(0.95):

        reasons.append(
            "💰 Transaction amount significantly exceeds normal spending pattern."
        )

    if int(txn["transaction_hour"]) <= 4:
        reasons.append(
            "🌙 Transaction performed during unusual late-night hours."
        )

    if len(reasons) == 0:
        reasons.append(
            "⚠️ AI model detected abnormal behavioral anomaly patterns."
        )

    for r in reasons:
        st.error(r)

    st.markdown("---")

    # ============================================
    # COMPLETE TRANSACTION DETAILS
    # ============================================

    st.subheader("📋 Full Transaction Details")

    detail_df = pd.DataFrame({
        "Feature": txn.index,
        "Value": txn.values
    })

    st.dataframe(
        detail_df,
        use_container_width=True
    )

    # ============================================
    # RECOMMENDED ACTIONS
    # ============================================

    st.subheader("🛡 Recommended Security Actions")

    actions = [
        "Temporarily block transaction",
        "Trigger OTP verification",
        "Notify fraud monitoring team",
        "Request customer identity verification",
        "Monitor linked account activity",
        "Flag account for enhanced surveillance"
    ]

    for action in actions:
        st.warning(action)

else:

    st.success(
        "✅ No fraudulent transactions found under current filters."
    )

    # =====================================================
    # FINAL STATUS
    # =====================================================

    st.success("✅ AI behavioral fraud analysis completed successfully.")

    st.markdown("</div>", unsafe_allow_html=True)