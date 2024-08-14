

# Resume ATS Scorer

## Overview

The **Resume ATS Scorer** is a web application designed to analyze resumes by comparing them with job descriptions, providing valuable insights such as strengths, weaknesses, and an overall ATS (Applicant Tracking System) score. The application leverages advanced machine learning models and natural language processing techniques to ensure that your resume stands out to potential employers.

## Features

- **ATS Scoring:** Evaluates your resume based on common ATS criteria and provides an overall score.
- **Strengths & Weaknesses Identification:** Highlights key strengths and areas of improvement in your resume.
- **Resume vs. Job Description Comparison:** Analyzes the alignment between your resume and the job description, ensuring that your skills and experiences match the job requirements.
- **Streamlit-Based Interface:** User-friendly and interactive web application interface.
- **Google Gemini 1.5 Flash Integration:** Utilizes advanced language models for accurate and insightful resume analysis.
- **PDF Handling with PyPDF:** Seamlessly extracts and processes resume content from PDF files.

## Technologies Used

- **Google Gemini 1.5 Flash:** Provides advanced language processing capabilities.
- **Streamlit:** For building an interactive and user-friendly web interface.
- **PyPDF:** For handling PDF files and extracting content from resumes.
- **Python:** Core programming language for application logic and data processing.

## Deployment

The application is deployed and can be accessed through the provided web link. The deployment ensures that users can easily upload their resumes, provide job descriptions, and receive detailed analysis and feedback in real time.

## Installation

To set up the Resume ATS Scorer locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/CoderOMaster/Resume_ATS.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Resume_ATS
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```
5. You can also use the app directly from the deployed link:
   ```bash
   https://resumeatsscore.streamlit.app/
   ```

## Usage

1. Open the application in your web browser.
2. Upload your resume in PDF format.
3. Paste the job description or upload it as a file.
4. Click on the "Compare Resume with Job Description" button to get your strengths, weaknesses, and a detailed comparison report.
5. Click on "Percentage match" for ATS score.
6. Review the feedback and make improvements to your resume.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---
