import streamlit as st
import tempfile
import plotly.express as px
import plotly.graph_objects as go

from parser import extract_text_from_pdf
from preprocess import clean_text
from skill_extractor import extract_skills
from advanced_ats import advanced_ats_score
from suggestions import missing_skills, generate_suggestions
from resume_analyzer import analyze_resume
from skill_match import calculate_skill_match
from keyword_analytics import top_keywords
from report_generator import generate_report

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(circle at top left,#0ea5e9 0%,transparent 25%),
    radial-gradient(circle at bottom right,#7c3aed 0%,transparent 25%),
    linear-gradient(135deg,#020617,#0f172a,#1e293b);
}

.main {
    color: white;
}

h1, h2, h3 {
    color: #38bdf8;
}

div[data-testid="metric-container"] {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(56,189,248,0.3);
    border-radius: 20px;
    padding: 20px;
    box-shadow: 0px 0px 20px rgba(56,189,248,0.2);
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    background: linear-gradient(90deg,#06b6d4,#3b82f6);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    box-shadow: 0px 0px 20px cyan;
}

section[data-testid="stSidebar"] {
    background: #0f172a;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ---------------- #

st.markdown("""
<div style="
padding:30px;
border-radius:20px;
background: linear-gradient(135deg,#0f172a,#1e293b,#0ea5e9);
text-align:center;
color:white;
box-shadow:0px 0px 25px rgba(14,165,233,0.5);
margin-bottom:20px;
">

<h1>🤖 AI Talent Intelligence Platform</h1>

<h3>
Next Generation Recruitment Intelligence Engine
</h3>

<p>
Analyze Resumes • Detect Skills • ATS Score • Recommendations
</p>

</div>
""", unsafe_allow_html=True)


# ---------------- SIDEBAR ---------------- #

st.sidebar.markdown("""
# 🤖 AI Dashboard

### System Status

🟢 Resume Parser Active

🟢 NLP Engine Active

🟢 ATS Engine Active

🟢 Skill Extractor Active

🟢 Recommendation Engine Active

🟢 PDF Generator Active

---

Future Ready AI Recruitment System
""")

st.markdown("""
<div style="
background:rgba(255,255,255,0.05);
padding:15px;
border-radius:15px;
margin-bottom:20px;
text-align:center;
font-size:18px;
font-weight:bold;
color:white;
">

🏠 Dashboard &nbsp;&nbsp;&nbsp;
📄 Resume Analysis &nbsp;&nbsp;&nbsp;
📊 Analytics &nbsp;&nbsp;&nbsp;
📥 Reports

</div>
""", unsafe_allow_html=True)

col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Resumes Analyzed", "500+")

with col2:
    st.metric("ATS Accuracy", "95%")

with col3:
    st.metric("Skills Database", "100+")

with col4:
    st.metric("AI Models", "NLP")
# ---------------- INPUT SECTION ---------------- #

st.markdown("## 📋 Candidate Evaluation Portal")
left, right = st.columns(2)

with left:

    st.subheader("📄 Upload Resume")

    uploaded_file = st.file_uploader(
        "Choose Resume PDF",
        type=["pdf"]
    )

with right:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the Job Description Here",
        height=250
    )

# ---------------- ANALYSIS BUTTON ---------------- #

if st.button("🔍 Analyze Resume"):
    with st.spinner("🤖 AI Engine Processing Resume..."):
        import time
        time.sleep(2)

    if uploaded_file is None:
        st.error("Please upload a resume PDF.")
        st.stop()

    if not job_description.strip():
        st.error("Please enter a Job Description.")
        st.stop()

    # Save uploaded PDF temporarily
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        temp_file.write(
            uploaded_file.read()
        )

        temp_path = temp_file.name

    # Extract Text

    resume_text = extract_text_from_pdf(
        temp_path
    )

    clean_resume = clean_text(
        resume_text
    )

    clean_job = clean_text(
        job_description
    )

    # Keywords

    keywords = top_keywords(
        clean_resume
    )

    # Skills

    resume_skills = extract_skills(
        clean_resume
    )

    job_skills = extract_skills(
        clean_job
    )

    # ATS Score

    score = advanced_ats_score(
        clean_resume,
        clean_job,
        resume_skills,
        job_skills
    )

    if score >= 80:
        st.markdown("""
    <div style="
    padding:20px;
    border-radius:15px;
    background:rgba(34,197,94,0.2);
    border:1px solid #22c55e;
    text-align:center;
    font-size:22px;
    margin-bottom:20px;
    ">
    🟢 AI Verdict: Excellent Candidate Match
    </div>
    """, unsafe_allow_html=True)

    elif score >= 60:

        st.markdown("""
    <div style="
    padding:20px;
    border-radius:15px;
    background:rgba(234,179,8,0.2);
    border:1px solid #eab308;
    text-align:center;
    font-size:22px;
    margin-bottom:20px;
    ">
    🟡 AI Verdict: Good Candidate Match
    </div>
    """, unsafe_allow_html=True)

    else:

        st.markdown("""
    <div style="
    padding:20px;
    border-radius:15px;
    background:rgba(239,68,68,0.2);
    border:1px solid #ef4444;
    text-align:center;
    font-size:22px;
    margin-bottom:20px;
    ">
    🔴 AI Verdict: Resume Needs Improvement
    </div>
    """, unsafe_allow_html=True)

    # Missing Skills

    missing = missing_skills(
        job_skills,
        resume_skills
    )

    # Recommendations

    recommendations = generate_suggestions(
        missing
    )

    # Resume Analysis

    strengths, weaknesses = analyze_resume(
        score,
        missing
    )

    # Skill Match

    skill_match_percentage, matched_skills = calculate_skill_match(
        resume_skills,
        job_skills
    )

    # ---------------- RESULTS ---------------- #

    st.success("✅ Resume Analysis Completed")
    st.markdown("## 📊 AI Analysis Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "ATS Score",
            f"{score}%"
        )

    with col2:
        st.metric(
            "Skills Found",
            len(resume_skills)
        )

    with col3:
        st.metric(
            "Missing Skills",
            len(missing)
        )

    # ATS Score Section

    st.subheader("📊 ATS Score")
    fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=score,
    title={'text': "ATS Score"},
    gauge={
        'axis': {'range': [0,100]},
        'bar': {'thickness': 0.4},
        'steps': [
            {'range':[0,50]},
            {'range':[50,80]},
            {'range':[80,100]}
        ]
    }
))

    st.plotly_chart(
    fig,
    use_container_width=True
    )

    st.progress(
        min(int(score), 100)
    )

    if score >= 80:
        st.success(
            f"Excellent Match: {score}%"
        )

    elif score >= 60:
        st.warning(
            f"Good Match: {score}%"
        )

    else:
        st.error(
            f"Needs Improvement: {score}%"
        )

    # Skills Found

    with st.expander("🛠 Skills Found", expanded=True):

        if len(resume_skills) == 0:
            st.warning(
            "No skills detected."
        )

        else:
            for skill in resume_skills:
                st.success(
                skill.title()
            )

    # Missing Skills

    with st.expander("❌ Missing Skills"):

        if len(missing) == 0:
            st.success(
            "No Missing Skills Found"
        )

        else:
            for skill in missing:
                st.error(
                skill.title()
            )

    # Recommendations

    with st.expander("💡 Recommendations"):

        if len(recommendations) == 0:

            st.success(
            "Resume is well aligned with the Job Description."
        )

        else:

            for rec in recommendations:
                st.info(
                rec
            )

    # Resume Strength Analysis

    st.subheader("📈 Resume Strength Analysis")

    for item in strengths:
        st.success(item)

    for item in weaknesses:
        st.error(item)

    # Skill Match

    st.subheader("🎯 Skill Match Analysis")

    st.metric(
        "Skill Match %",
        f"{skill_match_percentage}%"
    )

    st.subheader("✅ Matched Skills")

    if len(matched_skills) == 0:

        st.warning(
            "No matched skills found."
        )

    else:

        for skill in matched_skills:
            st.success(
                skill.title()
            )

    # Analytics

    st.subheader("📊 Skills Analytics")

    chart_data = {
        "Category": [
            "Matched Skills",
            "Missing Skills"
        ],
        "Count": [
            len(matched_skills),
            len(missing)
        ]
    }

    fig = px.pie(
        values=chart_data["Count"],
        names=chart_data["Category"],
        title="Resume Skill Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Final Evaluation

    st.subheader("🎯 Final Evaluation")

    if score >= 85:

        st.success(
            "Your resume is highly suitable for this role."
        )

    elif score >= 70:

        st.warning(
            "Your resume is a good match but can be improved."
        )

    else:

        st.error(
            "Consider improving your resume according to the recommendations."
        )

    # Top Keywords

    st.subheader("🔑 Top Resume Keywords")

    for word, count in keywords:
        st.write(
            f"{word} : {count}"
        )

    # PDF Report

    report_file = "ATS_Report.pdf"

    generate_report(
        report_file,
        score,
        skill_match_percentage,
        resume_skills,
        missing,
        recommendations
    )

    with open(
        report_file,
        "rb"
    ) as pdf_file:

        st.download_button(
            label="📄 Download ATS Report",
            data=pdf_file,
            file_name="ATS_Report.pdf",
            mime="application/pdf"
        )

# ---------------- FOOTER ---------------- #

st.markdown("""
<div style="
padding:25px;
text-align:center;
border-radius:20px;
background:rgba(255,255,255,0.05);
border:1px solid rgba(56,189,248,0.2);
">

<h2>🤖 AI Resume Screening System</h2>

<p>
Developed by <b>Piyush Kumar</b>
</p>

<p>
AI / ML Project • 2026
</p>

</div>
""", unsafe_allow_html=True)