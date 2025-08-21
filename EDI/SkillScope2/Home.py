# import streamlit as st
# import plotly.express as px
# import numpy as np
# import pandas as pd
# from datetime import datetime
# import os, sys



# from models import insert_sample_job, fetch_jobs

# # Insert a new job (only if you want demo data)
# insert_sample_job()

# # Fetch and display jobs
# fetch_jobs()




# # Import configuration
# try:
#     import config
# except ImportError:
#     st.warning("Config file not found. Using default settings.")

# # Add utils/data to path
# sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
# sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))

# from data_loader import DataLoader
# from nlp_processor import NLPProcessor
# from mock_job_data import MockJobData
# try:
#     from auth_manager import AuthManager
# except ImportError:
#     from simple_auth import SimpleAuthManager as AuthManager
# from api_integrator import JobAPIIntegrator, SalaryPredictor

# # Page config
# st.set_page_config(page_title="SkillScope - Home", page_icon="🎯", layout="wide")

# # --- Authentication Gate ---
# def check_authentication():
#     if not st.session_state.get("authenticated", False):
#         st.switch_page("login.py")

# check_authentication()
# # ----------------------------

# # Initialize session state
# if 'data_loader' not in st.session_state:
#     st.session_state.data_loader = DataLoader()
# if 'nlp_processor' not in st.session_state:
#     st.session_state.nlp_processor = NLPProcessor()
# if 'api_integrator' not in st.session_state:
#     st.session_state.api_integrator = JobAPIIntegrator()
# if 'salary_predictor' not in st.session_state:
#     st.session_state.salary_predictor = SalaryPredictor()

# def main():
#     user = st.session_state.get('user', {})
#     st.sidebar.title(f"Welcome, {user.get('name', 'User')}!")
#     st.sidebar.markdown("---")

#     # Logout button
#     if st.sidebar.button("Logout", use_container_width=True):
#         for key in list(st.session_state.keys()):
#             del st.session_state[key]
#         st.switch_page("login.py")

#     st.sidebar.markdown("---")

#     # API Status
#     st.sidebar.subheader("Data Sources")
#     if st.sidebar.button("Refresh Live Data", type="secondary"):
#         st.session_state.refresh_data = True

#     st.title("🎯 SkillScope - Job Market Analyzer")
#     st.markdown("### Discover trending skills and optimize your career path")

#     # Load mock + API data
#     mock_data = MockJobData()
#     mock_job_data = mock_data.get_job_postings()

#     api_integrator = st.session_state.api_integrator
#     job_data = mock_job_data

#     # If refresh_data is True, attempt API fetch
#     if st.session_state.get('refresh_data', False):
#         live_jobs = []
#         trending_queries = ["software engineer", "data scientist", "product manager", "devops engineer"]
#         for query in trending_queries[:2]:
#             jobs = api_integrator.search_all_sources(query, max_results_per_source=10)
#             live_jobs.extend(jobs)
#         if live_jobs:
#             live_df = pd.DataFrame(live_jobs)
#             if not live_df.empty:
#                 live_df['required_skills'] = live_df.apply(
#                     lambda x: api_integrator.extract_skills_from_job_data([x.to_dict()]), axis=1
#                 )
#                 live_df['industry'] = live_df.get('category', 'Technology')
#                 live_df['experience_level'] = 'Mid Level'
#                 job_data = pd.concat([mock_job_data.head(1000), live_df], ignore_index=True)
#         else:
#             st.sidebar.info("📊 Using comprehensive mock data")

#     # --- Dashboard content (same as before) ---
#     col1, col2, col3, col4 = st.columns(4)
#     with col1: st.metric("Total Job Postings", f"{len(job_data):,}")
#     with col2: st.metric("Unique Skills Tracked", len(set(sum(job_data['required_skills'], []))))
#     with col3: st.metric("Industries Covered", job_data['industry'].nunique())
#     with col4: st.metric("Avg. Max Salary", f"${job_data['salary_max'].mean():,.0f}")

#     st.markdown("---")
#     st.subheader("📊 Quick Market Insights")
#     col1, col2 = st.columns(2)
#     with col1:
#         industry_counts = job_data['industry'].value_counts()
#         st.plotly_chart(
#             px.bar(x=industry_counts.index, y=industry_counts.values,
#                    title="Job Postings by Industry",
#                    labels={'x': 'Industry', 'y': 'Jobs'}),
#             use_container_width=True
#         )
#     with col2:
#         fig_salary = px.box(job_data, x='industry', y='salary_max', title="Salary Distribution by Industry")
#         fig_salary.update_xaxes(tickangle=45)
#         st.plotly_chart(fig_salary, use_container_width=True)

#     st.subheader("🔥 Trending Skills Across All Industries")
#     all_skills = sum(job_data['required_skills'], [])
#     skill_counts = pd.Series(all_skills).value_counts().head(20)

#     col1, col2 = st.columns([2, 1])
#     with col1:
#         st.plotly_chart(
#             px.bar(x=skill_counts.values, y=skill_counts.index, orientation='h',
#                    title="Top 20 Most Demanded Skills",
#                    labels={'x': 'Job Postings', 'y': 'Skills'}),
#             use_container_width=True
#         )
#     with col2:
#         st.subheader("Skills Growth")
#         growth_data = pd.DataFrame({
#             'skill': skill_counts.head(10).index,
#             'growth': np.random.uniform(5, 25, 10)
#         })
#         for _, row in growth_data.iterrows():
#             st.metric(label=row['skill'], value=f"+{row['growth']:.1f}%",
#                       delta=f"{row['growth']:.1f}% vs last quarter")

#     st.subheader("📋 Recent Job Postings")
#     recent_jobs = job_data.head(10)[['title', 'company', 'industry', 'location', 'salary_max']]
#     recent_jobs['salary_max'] = recent_jobs['salary_max'].apply(lambda x: f"${x:,.0f}")
#     st.dataframe(recent_jobs, use_container_width=True)

#     st.markdown("---")
#     st.markdown("""
#     ### 🚀 Explore More Features:
#     - Industry Trends  
#     - Resume Analyzer  
#     - Career Recommendations  
#     Use the sidebar navigation to explore!
#     """)

# if __name__ == "__main__":
#     main()






import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
from datetime import datetime
import os, sys
import psycopg2   # ✅ Added for PostgreSQL

# ------------------- PostgreSQL CONNECTION -------------------

# Function to connect to PostgreSQL
def get_connection():
    return psycopg2.connect(
        host="localhost",       
        database="job_data",        # ⚠️ replace with your database name (you created "skillscope", so change to "skillscope" if that's correct)
        user="postgres",           
        password="your_password",   # 🔑 replace with your actual PostgreSQL password
        port="5432"             
    )

# Function to fetch job data from DB
def fetch_jobs():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT job_title, company, location, skills, posted_date FROM jobs;")
    rows = cursor.fetchall()
    conn.close()
    return rows

# --------------------------------------------------------------

# Import configuration
try:
    import config
except ImportError:
    st.warning("Config file not found. Using default settings.")

# Add utils/data to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))

from data_loader import DataLoader
from nlp_processor import NLPProcessor
from mock_job_data import MockJobData
try:
    from auth_manager import AuthManager
except ImportError:
    from simple_auth import SimpleAuthManager as AuthManager
from api_integrator import JobAPIIntegrator, SalaryPredictor

# Page config
st.set_page_config(page_title="SkillScope - Home", page_icon="🎯", layout="wide")

# --- Authentication Gate ---
def check_authentication():
    if not st.session_state.get("authenticated", False):
        st.switch_page("login.py")

check_authentication()
# ----------------------------

# Initialize session state
if 'data_loader' not in st.session_state:
    st.session_state.data_loader = DataLoader()
if 'nlp_processor' not in st.session_state:
    st.session_state.nlp_processor = NLPProcessor()
if 'api_integrator' not in st.session_state:
    st.session_state.api_integrator = JobAPIIntegrator()
if 'salary_predictor' not in st.session_state:
    st.session_state.salary_predictor = SalaryPredictor()

def main():
    user = st.session_state.get('user', {})
    st.sidebar.title(f"Welcome, {user.get('name', 'User')}!")
    st.sidebar.markdown("---")

    # Logout button
    if st.sidebar.button("Logout", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.switch_page("login.py")

    st.sidebar.markdown("---")

    # API Status
    st.sidebar.subheader("Data Sources")
    if st.sidebar.button("Refresh Live Data", type="secondary"):
        st.session_state.refresh_data = True

    st.title("🎯 SkillScope - Job Market Analyzer")
    st.markdown("### Discover trending skills and optimize your career path")

    # --- Fetch Jobs from Database ---
    jobs = fetch_jobs()
    if jobs:
        db_df = pd.DataFrame(jobs, columns=["Job Title", "Company", "Location", "Skills", "Posted Date"])
        st.subheader("📋 Jobs from Database")
        st.dataframe(db_df, use_container_width=True)
    else:
        st.info("No job data found in PostgreSQL database. Using mock/API data instead.")

    # Load mock + API data
    mock_data = MockJobData()
    mock_job_data = mock_data.get_job_postings()

    api_integrator = st.session_state.api_integrator
    job_data = mock_job_data

    # If refresh_data is True, attempt API fetch
    if st.session_state.get('refresh_data', False):
        live_jobs = []
        trending_queries = ["software engineer", "data scientist", "product manager", "devops engineer"]
        for query in trending_queries[:2]:
            jobs = api_integrator.search_all_sources(query, max_results_per_source=10)
            live_jobs.extend(jobs)
        if live_jobs:
            live_df = pd.DataFrame(live_jobs)
            if not live_df.empty:
                live_df['required_skills'] = live_df.apply(
                    lambda x: api_integrator.extract_skills_from_job_data([x.to_dict()]), axis=1
                )
                live_df['industry'] = live_df.get('category', 'Technology')
                live_df['experience_level'] = 'Mid Level'
                job_data = pd.concat([mock_job_data.head(1000), live_df], ignore_index=True)
        else:
            st.sidebar.info("📊 Using comprehensive mock data")

    # --- Dashboard content (same as before) ---
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Job Postings", f"{len(job_data):,}")
    with col2: st.metric("Unique Skills Tracked", len(set(sum(job_data['required_skills'], []))))
    with col3: st.metric("Industries Covered", job_data['industry'].nunique())
    with col4: st.metric("Avg. Max Salary", f"${job_data['salary_max'].mean():,.0f}")

    st.markdown("---")
    st.subheader("📊 Quick Market Insights")
    col1, col2 = st.columns(2)
    with col1:
        industry_counts = job_data['industry'].value_counts()
        st.plotly_chart(
            px.bar(x=industry_counts.index, y=industry_counts.values,
                   title="Job Postings by Industry",
                   labels={'x': 'Industry', 'y': 'Jobs'}),
            use_container_width=True
        )
    with col2:
        fig_salary = px.box(job_data, x='industry', y='salary_max', title="Salary Distribution by Industry")
        fig_salary.update_xaxes(tickangle=45)
        st.plotly_chart(fig_salary, use_container_width=True)

    st.subheader("🔥 Trending Skills Across All Industries")
    all_skills = sum(job_data['required_skills'], [])
    skill_counts = pd.Series(all_skills).value_counts().head(20)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(
            px.bar(x=skill_counts.values, y=skill_counts.index, orientation='h',
                   title="Top 20 Most Demanded Skills",
                   labels={'x': 'Job Postings', 'y': 'Skills'}),
            use_container_width=True
        )
    with col2:
        st.subheader("Skills Growth")
        growth_data = pd.DataFrame({
            'skill': skill_counts.head(10).index,
            'growth': np.random.uniform(5, 25, 10)
        })
        for _, row in growth_data.iterrows():
            st.metric(label=row['skill'], value=f"+{row['growth']:.1f}%",
                      delta=f"{row['growth']:.1f}% vs last quarter")

    st.subheader("📋 Recent Job Postings")
    recent_jobs = job_data.head(10)[['title', 'company', 'industry', 'location', 'salary_max']]
    recent_jobs['salary_max'] = recent_jobs['salary_max'].apply(lambda x: f"${x:,.0f}")
    st.dataframe(recent_jobs, use_container_width=True)

    st.markdown("---")
    st.markdown("""
    ### 🚀 Explore More Features:
    - Industry Trends  
    - Resume Analyzer  
    - Career Recommendations  
    Use the sidebar navigation to explore!
    """)

if __name__ == "__main__":
    main()
