
from crewai import Crew, Process # type: ignore

from textwrap import dedent
from agents import ReviewerAgents
from tasks import ReviewerTasks
# from file_loader import read_file

from dotenv import load_dotenv # type: ignore
load_dotenv()

from langchain_groq  import ChatGroq    
import json
import streamlit as st
import matplotlib.pyplot as plt
    

class ResumeReviewerCrew():
    def __init__(self, resume, jd):
        # Initialize LLM
        self.GroqAI = ChatGroq(model="llama3-8b-8192", temperature=0)
        self.resume = resume
        self.jd = jd

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ReviewerAgents()
        tasks = ReviewerTasks()

        # Define your custom agents and tasks here
        expert_resume_reviewer_agent = agents.expert_resume_reviewer()

        # Custom tasks include agent name and variables as input
        resume_reviewer_task = tasks.expert_resume_reviewer(
            expert_resume_reviewer_agent,
            self.resume,
            self.jd
        )
        
        # Define your custom crew here
        crew = Crew(
            agents=[expert_resume_reviewer_agent],
            tasks=[resume_reviewer_task],
            Process=Process.sequential,
            Cache=False,
            verbose=True,
            max_rpm=10
        )

        result = crew.kickoff()
        if isinstance(result, str):
            return result
        else:
            return result.raw


def visualize_skills(skills_match, missing_skills):
    # Combine matching and missing skills
    skills = skills_match + missing_skills
    categories = ['Matching'] * len(skills_match) + ['Missing'] * len(missing_skills)
    
    # Color coding for bars
    colors = ['green' if cat == 'Matching' else 'red' for cat in categories]

    # Create horizontal bar chart
    plt.figure(figsize=(8, 6))
    plt.barh(skills, [1]*len(skills), color=colors, edgecolor='black')

    # Add title and labels
    plt.title('Resume Skills: Matching vs Missing', fontsize=16)
    plt.xlabel('Skills Presence', fontsize=12)
    plt.ylabel('Skills', fontsize=12)
    
    # Add grid and remove y-axis ticks
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.xticks([])  # No values needed on the x-axis
    plt.yticks(fontsize=10)

    # Add legend
    matching_patch = plt.Line2D([0], [0], color='green', lw=6)
    missing_patch = plt.Line2D([0], [0], color='red', lw=6)
    plt.legend([matching_patch, missing_patch], ['Matching Skills', 'Missing Skills'], loc='lower right')

    return plt


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
     # Streamlit app layout
    st.title("Resume Review Tool")

    # Resume and Job Description Inputs
    st.subheader("Input your Resume and Job Description")
    resume_text = st.text_area("Resume:", height=200)
    jd_text = st.text_area("Job Description:", height=200)
    
    custom_crew = ResumeReviewerCrew(resume_text,jd=jd_text)
    try:
        # Simulate button click to process input
        if st.button("Analyze Resume"):
            with st.spinner("Analyzing..."):
                result = custom_crew.run()
        
            with open('resume_jd_comparison_report.txt', 'r') as file:
                resume_data = file.read()
            resume_data = resume_data.split('Note')[0]
            resume_data = json.loads(resume_data)
            
            st.header("Key Metrics")
            col1, col2, col3 = st.columns([1.25,1.25,2])
            
            # Resume Compatibility Score before and after suggestions
            col1.metric(label="Resume Compatibility (Before)", value=f"{resume_data['resume_compatibility_score_before']}%")
            col2.metric(label="Resume Compatibility (After)", value=f"{resume_data['resume_compatibility_score_after']}%")
            col3.metric(label="Based on current resume 'Chances of Selection'", value=resume_data['chances_of_selection'])

            # Skill analysis section
            st.header("Skills Matching Overview")

            # Split dashboard layout into two sections: Left for skills chart, Right for suggestions
            col_left, col_right = st.columns([2, 3])
            col_left.pyplot(visualize_skills(resume_data['matching_skills'], resume_data['missing_skills']))
            
            # Suggestions section on the right
            # col_right.subheader("Detailed Suggestions for Improvement")
            with col_right.expander("Detailed Suggestions for Improvement", expanded=True):
                for suggestion in resume_data['suggestions']:
                    st.write(f"- **Section:** {suggestion['resume_section']}")
                    st.write(f"  - **Suggested Modifications:** {suggestion['suggested_modifications']}")
                    st.write(f"  - **Reason:** {suggestion['reason']}")

    except Exception as e:
        st.error(f"Error occurred: {str(e)}")