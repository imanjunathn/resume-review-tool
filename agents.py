from crewai import Agent
from textwrap import dedent
from langchain_groq  import ChatGroq



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class ReviewerAgents:
    def __init__(self):
        self.GroqAI70 = ChatGroq(model="llama-3.1-70b-versatile", temperature=0)

    def expert_resume_reviewer(self,):
         return Agent(
            role="Expert Resume Reviewer and JD Comparator",
            backstory=dedent(f"""
                            I possess deep expertise in the fields of recruitment, 
                            resume optimization, and job-market trends. My experience allows me to accurately evaluate resumes 
                            and ensure they match the skills, responsibilities, and qualifications highlighted in any JD. 
                            With my background, I can also provide actionable feedback to enhance the resume's relevance to the job posting.
                            """),
            goal=dedent(f"""
                        Review the provided resume and compare it with the given job description. 
                        Identify areas where the resume can be improved to better align with the JD. 
                        Provide suggestions for modifications, such as emphasizing relevant skills, adjusting wording, or reordering sections. 
                        The feedback should be in a structured and actionable format, listing specific changes to make for a more tailored fit.
                        """),
            allow_delegation=False,
            verbose=True,
            llm=self.GroqAI70,
            # max_iter=10,
            max_rpm=5
        )