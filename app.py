import streamlit as st
import google.generativeai as genai
import os
import pypdf as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
genai.configure(api_key='AIzaSyC_i-2d1ZWhHDyeYKTqjLLqNRjOPVCiAu8')


def get_gemini_response(input_text, pdf_content, prompt):
    """Generate a response using Google Generative AI."""
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, pdf_content, prompt])
    return response.text

def input_pdf_text(uploaded_file):
    """Extract text from the uploaded PDF file."""
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ''  # Ensure no NoneType error
    return text

# Streamlit app configuration
st.set_page_config(page_title="ATS Resume Expert")
st.header("ATS Tracking System")

# Input fields for job description and resume upload
input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

# Display a message if the file is uploaded successfully
if uploaded_file:
    st.write("PDF Uploaded Successfully")

# Define button triggers
submit1 = st.button("Compare Resume with Job Description")
submit3 = st.button("Percentage Match")

# Input prompts for generating responses
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. You have to be a critical Human Resource manager who doesnt shy away from telling weakness and where applicant is lacking in skills
make sure to criticize and provide constructive feedback.Also tell whether you want to hire or not for this role depending purely upon his skills and experience in the resume with regard to given job description. Use logic to filter best candidates from their resume.
Highlight the strengths and weaknesses briefly of the applicant in relation to the specified job requirements.Make a strong opinion.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Provide the percentage of match between the resume and the job description. 
First, the output should come as a percentage, followed by the missing keywords, and finally, your final thoughts.You should be highly critical and logical while evaluating
resume and give tough scores. Percentages should be carefully calculated keeping in mind missing skills and all criterias
"""

# Generate and display the response based on the button pressed
if submit1 or submit3:
    if uploaded_file:
        pdf_content = input_pdf_text(uploaded_file)
        prompt = input_prompt1 if submit1 else input_prompt3
        response = get_gemini_response(input_text, pdf_content, prompt)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.warning("Please upload the resume.")
