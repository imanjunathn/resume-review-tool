# Resume Review Tool

## Overview
The **Resume Review Tool** is a web application designed to analyze a user's resume against a job description (JD) using advanced language models. It provides insights into the compatibility of the resume with the JD, highlights matching and missing skills, and offers actionable suggestions for improvement.

## Features
- Analyzes the provided resume against the job description.
- Calculates the resume compatibility score.
- Identifies matching and missing skills.
- Provides detailed suggestions for enhancing the resume.
- Visualizes skills in a clear and informative manner.

## Technologies Used
- **Python**: Main programming language.
- **Streamlit**: For building the web interface.
- **LangChain Groq**: To leverage advanced language models for analysis.
- **Matplotlib**: For visualizing skills.
- **dotenv**: For loading environment variables.
- **CrewAI Framework Usage**: The **CrewAI** framework is utilized to manage the analysis process in the Resume Review Tool. It allows for the creation and orchestration of custom agents and tasks that enhance the resume evaluation.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/resume-review-tool.git
   cd resume-review-tool
   
2. Create a virtual environment and activate it:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
4. Install the required packages:
   pip install -r requirements.txt

5. Run the application:
   1. streamlit run main.py
   2. Open your web browser and go to http://localhost:8501.
   3. Input your resume and the job description in the provided text areas and click the Analyze Resume button to get insights and suggestions.
  
## How It Works
 1. The application uses the ChatGroq language model to analyze the resume and job description.
 2. It calculates the resume compatibility score based on the analysis of skills, years of experience, and designation.
 3. It visually represents the matching and missing skills using a horizontal bar chart.
 4. The tool provides a breakdown of suggestions for improving the resume to better match the job requirements.

**Example Output**

When analyzing a resume, the tool will output metrics such as:
1. Resume Compatibility (Before)
2. Resume Compatibility (After)
3. Chances of Selection
4. A visual representation of matching vs. missing skills
5. Detailed suggestions for improvement
  
**Contributing**
  Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.





