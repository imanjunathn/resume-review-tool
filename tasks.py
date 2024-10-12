from crewai import Task
from textwrap import dedent


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class ReviewerTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def expert_resume_reviewer(self, agent, resume_text, jd_text):
        return Task(
            description=dedent(
                f"""
                    **Task**: Review Resume, Compare to JD, Provide Resume Compatibility Score, and Generate Detailed Suggestions.
                    **Description**: 
                    - Review the provided resume document and compare it with the Job Description (JD).
                    - Calculate the **resume compatibility score** by analyzing skills, total years of experience, and designation, providing weightage to each factor.
                    - Prioritize the sections of the resume that have the greatest impact on hiring decisions, such as skills, relevant projects, and experience.
                    - If the current **resume compatibility score** is above 70%, analyze missing skills and areas needing improvement, particularly focusing on role-specific and industry-specific skills.
                    - Provide actionable, specific suggestions to enhance the resume, including suggestions for quantifiable achievements and outcomes in the experience section.
                    - Tailor the suggestions based on the job level (entry-level, mid-level, senior-level).
                    - Calculate and display the **resume compatibility score** before and after implementing the suggestions, allowing for a visual side-by-side comparison of how the suggestions affect the resume's alignment with the JD.
                    - Based on the current **resume compatibility score**, assess whether the user can apply for the job with their current resume and estimate their **chances of selection**.

                    **Scoring Transparency**:
                    - Provide a detailed breakdown of how the resume compatibility score is calculated.
                    - Show the weightage applied to skills, years of experience, and designation.
                    - Values have to be percentage (e.g., 30 for skills, 25 for years of experience, 45 for designation).

                    **Chances of Selection**:
                    - Assess and report whether the user can apply with their current resume based on its alignment with the JD.
                    - Provide an estimated percentage for **chances of selection** based on how well the resume meets the JD requirements.

                    **Customizable Output**:
                    - Score breakdown, missing skills, matching skills, specific suggestions for improvement, and estimated selection chances, with a focus on high-impact areas like relevant skills and quantifiable experience.

                    **Parameters**: 
                        - resume_document: {resume_text}
                        - job_description: {jd_text}

                    **Note**: {self.__tip_section()}
                """
            ),
            agent=agent,
            expected_output=f"""
                                A JSON object with 'resume_compatibility_score_before', 'resume_compatibility_score_after', matching skills, missing skills, detailed suggestions for improvement, chances of selection, and visual elements representing the skill gap analysis.
                                Example output: 
                                {{
                                    "resume_compatibility_score_before": 72,
                                    "resume_compatibility_score_after": 92,
                                    "matching_skills": [
                                        "Microsoft Intune Admin Center",
                                        "Windows Server Administration"
                                    ],
                                    "missing_skills": [
                                        "Linux System Administration",
                                        "Cloud Computing"
                                    ],
                                    "suggestions": [
                                        {{
                                            "resume_section": "Skills",
                                            "suggested_modifications": "Add Linux System Administration, Cloud Computing",
                                            "reason": "Required for System Technician II role based on JD"
                                        }},
                                        {{
                                            "resume_section": "Experience", 
                                            "suggested_modifications": "Highlight specific projects that demonstrate your experience with Microsoft Intune Admin Center and Windows Server Administration", 
                                            "reason": "Experience section does not fully showcase relevant skills"
                                        }}
                                    ],
                                    "chances_of_selection": "High",
                                    "skill_gap_analysis": {{
                                        "IT systems": "Strong",
                                        "Cloud services": "Needs improvement"
                                    }},
                                    "scoring_transparency": {{
                                        "skills": 30,
                                        "years_of_experience": 25,
                                        "designation": 20,
                                        "weightage": 15
                                    }},
                                    "detailed_breakdown": {{
                                        "skills": 23.4,
                                        "years_of_experience": 18.75,
                                        "designation": 16,
                                        "weightage": 20
                                    }}
                                }},
                            """,
            output_file='./resume_jd_comparison_report.txt'
        )