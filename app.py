import streamlit as st
import pandas as pd
import json
import os
import random
from datetime import datetime

# ==============================================================================
# CONSTANTS, KNOWLEDGE BASE MATRIX & PROPOSITIONAL SCHEMAS
# ==============================================================================
APP_NAME = "Career Choice"
CURRENT_YEAR = 2026

# Production Rules / Inference Matrix Framework (Knowledge Base)
KNOWLEDGE_BASE = {
    "software_engineering": {
        "title": "Software Engineering & Distributed Systems",
        "logic_expression": "Coding AND Analytical_Thinking AND (NOT Visual_Art_Focus)",
        "prereqs": ["Object-Oriented Languages (Python/Java)", "Data Structures", "Design Patterns"],
        "consequence_if_taken": "High structural logic throughput, rapid engineering scalability, and intense immersion within core optimization paradigms.",
        "consequence_if_avoided": "Isolation from baseline architectural engineering systems, forcing dependency on third-party logic templates, but freeing time for client-facing execution.",
        "market_trend_now": "Rapid structural expansion of automated infrastructure engines, cloud pipeline configurations, and generative orchestration layers.",
        "market_trend_10y": "AI multi-agent swarms compile routine code units autonomously. Professional engineers shift heavily to high-assurance verification, prompt design architecture, and complex safety validation systems."
    },
    "data_science_ai": {
        "title": "Data Science & Quantum Artificial Intelligence",
        "logic_expression": "Coding AND Advanced_Mathematical_Logic AND High_Analytics_Interest",
        "prereqs": ["Linear Algebra & Bayesian Stats", "Python (Pandas/NumPy/Scikit)", "Neural Network Principles"],
        "consequence_if_taken": "Unlocks predictive automation capabilities, data mining infrastructure mastery, and optimization algorithms optimization vectors.",
        "consequence_if_avoided": "Lack of capacity to navigate massive statistical patterns, forcing a reliance on rigid, traditional software logic matrices.",
        "market_trend_now": "Widespread deployment of Fine-Tuning pipelines, Retrieval-Augmented Generation (RAG) structures, and vector indexing operations.",
        "market_trend_10y": "Fully autonomous agent ecosystems computing on specialized edge processors, utilizing localized contextual logic loops with zero latency."
    },
    "ui_ux_design": {
        "title": "Multimodal UI/UX & Spatial Product Design",
        "logic_expression": "Visual_Art_Focus AND Structural_Empathy AND (NOT Advanced_Mathematical_Logic)",
        "prereqs": ["Design Systems & Tooling (Figma)", "User Cognitive Psychology", "Interactive Prototyping"],
        "consequence_if_taken": "High creative autonomy, complete control over conversion interfaces, and direct optimization of customer product interaction metrics.",
        "consequence_if_avoided": "Total technical detachment from client-facing visual logic, restricting your role to hidden back-end engineering databases.",
        "market_trend_now": "Cross-device responsive design language components, voice-guided interactive layouts, and high-fidelity wireframes.",
        "market_trend_10y": "Dynamic interfaces that regenerate color configurations and structural layouts on-the-fly based on immediate eye-tracking feedback and neural signals."
    },
    "product_management": {
        "title": "Technical Product Management & Strategy",
        "logic_expression": "High_Communication AND Strategy_Interest AND (NOT Deep_Coding)",
        "prereqs": ["Agile Framework Methodologies", "Market Fit Analysis", "Cross-Functional Collaboration Protocols"],
        "consequence_if_taken": "High cross-departmental leverage, immediate commercial ownership, and strategic influence on engineering product direction.",
        "consequence_if_avoided": "Restricts personal operational trajectory strictly to technical task execution pipelines with minimal voice in product roadmap definitions.",
        "market_trend_now": "Data-backed lifecycle optimization metrics, product-led growth experiments, and automated scrum telemetry reporting tools.",
        "market_trend_10y": "Generative agents manage resource scheduling and roadmap documentation logs. Human leads focus fully on cross-entity ethics, venture positioning, and systemic innovation management."
    }
}

INSPIRATIONAL_QUOTES = [
    {"quote": "The best way to predict the future is to invent it systematically.", "author": "Alan Kay"},
    {"quote": "The mind is not a vessel to be filled, but a fire to be kindled with logic.", "author": "Plutarch"},
    {"quote": "Quality means executing precision architectures correctly even when no entity is auditing you.", "author": "Henry Ford"},
    {"quote": "Your training determines your operational rules; your vision determines your final global impact.", "author": "Expert System Axiom"}
]

# Configure Streamlit Display Space
st.set_page_config(
    page_title=APP_NAME,
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Vibrant & Peaceful UI Styling Interface via CSS Injection
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #020617 100%);
        color: #f8fafc;
    }
    h1, h2, h3 {
        color: #38bdf8 !important;
        font-family: 'Inter', system-ui, sans-serif;
        font-weight: 700;
    }
    .quote-box {
        background: rgba(255, 255, 255, 0.03);
        border-left: 4px solid #f43f5e;
        padding: 24px;
        border-radius: 8px;
        margin-bottom: 24px;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.05);
    }
    .card {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(56, 189, 248, 0.2);
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 24px;
        backdrop-filter: blur(12px);
    }
    code {
        color: #f43f5e !important;
        background-color: rgba(0,0,0,0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

USER_DB_FILE = "users_database.json"

def load_users():
    if not os.path.exists(USER_DB_FILE):
        default_data = {"student_alpha": {"password": "securePass123", "created": str(datetime.now())}}
        with open(USER_DB_FILE, "w") as f:
            json.dump(default_data, f)
        return default_data
    try:
        with open(USER_DB_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_user(username, password):
    users = load_users()
    users[username] = {"password": password, "created": str(datetime.now())}
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

# Initialize Session States Safely
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "username" not in st.session_state:
    st.session_state.username = None
if "dialogue_step" not in st.session_state:
    st.session_state.dialogue_step = 0
if "user_responses" not in st.session_state:
    st.session_state.user_responses = {}
if "selected_quote" not in st.session_state:
    st.session_state.selected_quote = random.choice(INSPIRATIONAL_QUOTES)

# ==============================================================================
# SECURE DISCRETE ADMINISTRATIVE ROUTING BACKDOOR
# ==============================================================================
query_params = st.query_params
is_creator_mode = query_params.get("access_scope") == "creator_admin_override"

# Administrative Matrix View
if is_creator_mode:
    st.title("🛡️ Creator Administrative Matrix & Account Controller")
    st.markdown("---")
    st.subheader("👥 Registered Global User Credentials Workspace (Protected Audit)")
    
    users_data = load_users()
    df_users = [{"Profile Name / Username": k, "Password Value": v["password"], "Creation Date": v.get("created", "N/A")} for k, v in users_data.items()]
    
    st.dataframe(pd.DataFrame(df_users), use_container_width=True)
    st.info("💡 Developer Access Active: Use this administrative zone to safely audit profiles without public visibility options.") 
    
    if st.button("Exit Controller Space & View Public Interface"):
        st.query_params.clear()
        st.rerun()
    st.stop()

# ==============================================================================
# PUBLIC APPLICATION FLOW SECTION
# ==============================================================================
if not st.session_state.authenticated:
    col_left, col_right = st.columns([1.3, 1])
    
    with col_left:
        st.markdown(f"# Welcome to {APP_NAME} Platform")
        st.markdown("### *A production rule engine processing career trajectories using logical deduction.*")
        
        # Peaceful Aesthetic Visual Graphic Panel
        st.markdown("""
            <div style="background: linear-gradient(135deg, #0284c7 0%, #0f766e 100%); height: 260px; border-radius: 16px; display: flex; align-items: center; justify-content: center; margin-top: 24px; color: #f8fafc; font-size: 1.25rem; font-weight: 300; padding: 30px; text-align: center; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.3);">
                "True career optimization requires quiet reflection, logical analysis of operational constraints, and decisive alignment with industry growth trends."
            </div>
        """, unsafe_allow_html=True)
        
        # Rotational Quote Generator Hook
        active_quote = st.session_state.selected_quote
        st.markdown(f"""
        <div class="quote-box" style="margin-top: 32px;">
            <div style="font-size: 1.25rem; font-style: italic; color: #f8fafc;">"{active_quote['quote']}"</div>
            <div style="text-align: right; font-weight: bold; color: #38bdf8; margin-top: 8px;">— {active_quote['author']}</div>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
Use code with caution.st.markdown("", unsafe_allow_html=True)st.subheader("🔐 Access Control System")auth_action = st.radio("Choose Gateway Option", ["Access Existing Profile", "Provision New Profile"])username_input = st.text_input("Enter Profile Name")password_input = st.text_input("Enter Profile Password Token", type="password")if auth_action == "Access Existing Profile":if st.button("Verify Verification Credentials ➔"):users_database = load_users()if username_input in users_database and users_database[username_input]["password"] == password_input:st.session_state.authenticated = Truest.session_state.username = username_inputst.success("Access tokens confirmed successfully.")st.rerun()else:st.error("Authentication check failed. Confirm spelling or password fields.")else:if st.button("Initialize Structural Profile ➔"):users_database = load_users()if username_input in users_database:st.error("Profile label already allocated in user records.")elif len(username_input) < 3 or len(password_input) < 4:st.warning("Username must exceed 2 characters; password must exceed 3 characters.")else:save_user(username_input, password_input)st.success("Account provisioned! Please shift options to 'Access Existing Profile' above to sign in.")st.markdown("", unsafe_allow_html=True)else:# ==============================================================================# SECURED REGION: LOGGED IN WORKSPACE DASHBOARD# ==============================================================================st.sidebar.markdown(f"### 🔮 Dashboard Controller")st.sidebar.markdown(f"User Stance: {st.session_state.username}")st.sidebar.markdown("---")st.sidebar.caption("🔧 Platform Administrator Note: To check real-time global login rosters without building standard input boxes, pass ?access_scope=creator_admin_override parameter through your active address line.")if st.sidebar.button("De-authenticate Session (Sign Out)"):st.session_state.authenticated = Falsest.session_state.username = Nonest.session_state.dialogue_step = 0st.session_state.user_responses = {}st.rerun()st.title("🧭 Intelligent Trajectory Inference Dashboard")# 2-Step Clarifying Questions Processing Enginest.markdown("### 🤖 Diagnostic Dialogue Analysis")dialogue_flow = {0: {"question": "Which domain core matches your instinctual capability matrix?","key": "logic_vs_visual","options": ["Systematic coding, logic automation, and back-end algorithm design", "Visual arts, user journey crafting, and creative application architecture"]},1: {"question": "What is your comfort framework regarding heavy statistical analysis and analytical models?","key": "math_comfort","options": ["High performance comfort with math models and data sorting matrices", "Low comfort boundaries with mathematics; preference for business strategy or interface structure"]}}step_pointer = st.session_state.dialogue_stepif step_pointer < len(dialogue_flow):st.info(f"AI Clarifying Evaluation Query - Phase {step_pointer + 1} of {len(dialogue_flow)}:")st.markdown(f"#### {dialogue_flow[step_pointer]['question']}")user_pick = st.radio("Assert your preference:", dialogue_flow[step_pointer]['options'])if st.button("Register Inference Fact ➔"):st.session_state.user_responses[dialogue_flow[step_pointer]['key']] = user_pickst.session_state.dialogue_step += 1st.rerun()else:st.success("✅ Dialogue profile parameters locked into system Working Memory successfully.")if st.button("🔄 Reset Conversational Engine"):st.session_state.dialogue_step = 0st.session_state.user_responses = {}st.rerun()# Parse logic tokens from runtime dictionary metricsuser_facts = st.session_state.user_responsesAtom_Coding = "systematic coding" in user_facts.get("logic_vs_visual", "").lower()Atom_Art = not Atom_CodingAtom_Math = "high performance" in user_facts.get("math_comfort", "").lower()Atom_Strategy = not Atom_Math# Inference Engine: Resolve logical paths matching production matrix conditionsif Atom_Coding and Atom_Math:target_key = "data_science_ai"elif Atom_Coding and not Atom_Math:target_key = "software_engineering"elif Atom_Art and Atom_Strategy:target_key = "product_management"else:target_key = "ui_ux_design"record = KNOWLEDGE_BASE[target_key]st.markdown("---")st.subheader("🧠 Knowledge Base Logical Resolution Results")st.markdown(f"""🎯 Deduced Path Target: {record['title']}Propositional Logic Statement Evaluated: {record['logic_expression']}💡 Conditional Justification Architecture: If you proceed down this target trajectory, the following framework occurs: {record['consequence_if_taken']}⚠️ Counterfactual Alternative Reality: Conversely, if you choose to avoid this logical path, you must accept these constraints: {record['consequence_if_avoided']}""", unsafe_allow_html=True)# Skill gaps matrix and structural suggestions modulest.markdown("### 📊 Live Matrix Capability Evaluation")left_p, right_p = st.columns(2)with left_p:input_grade = st.slider("State current quantitative assessment performance marks (%)", 10, 100, 75)# Actionable contextual rules engine recommendations matching performance data inputif input_grade < 60:st.warning("⚠️ Optimization Required: High foundational gaps detected. System recommends focus on basic programming loops, algorithm principles, and structured textbooks before seeking complex frameworks.")elif input_grade < 85:st.info("📈 Growth Matrix Running: Moderate skills detected. System recommendation details focus on working open-source repos, executing build architectures, and pipeline setups.")else:st.success("🌟 High proficiency verified: Advanced capability matrix detected. Transition directly toward advanced microservice layout frameworks, technical documentation production, and logic system research.")with right_p:st.markdown("Core Skill Set Roadmap Requirements for Perfection:")for core_skill in record['prereqs']:st.markdown(f"- 🛠️ Mandatory Target Cluster: {core_skill}")# Macro forecast time horizon dashboard modulesst.markdown("### ⏳ Macro-Horizon Economic Paradigm Forecasting Matrix")col_now, col_future = st.columns(2)with col_now:st.info(f"Current Real-Time Global Structural Trend ({CURRENT_YEAR}): {record['market_trend_now']}")with col_future:st.success(f"10-Year Forward Looking Technology Shift Strategy ({CURRENT_YEAR + 10}): {record['market_trend_10y']}")st.markdown("---")st.caption(f"{APP_NAME} Framework Engine v1.1.0 • Formulated under B.Tech AI Production Principles.")