#!/usr/bin/env python
# coding: utf-8

# # Resume ATS Matching 

# In[ ]:


from dotenv import load_dotenv

load_dotenv()
import streamlit as st
import os
from PIL import Image
import pdf2image
import google.generativeai as genai
import io
import base64

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## convert the pdf to image
        images = pdf2image.convert_from_bytes(uploaded_file.read())

        first_page = imaged[0]

        #convert to bytes
        img_arr_byte = io.BytesIO()
        first_page.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        pdf_parts = [
            {
                "mime_type":"image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()  
            } 
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("no file uploaded")
        
        
#streamlit app

st.set_page_config(page_title = "ATS Resume Expert")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description:", key = "input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type = ["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded successfull")
    
submit1 = st.button("Tell Me About The Resume")
#submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("What Are The Keywords That Are Missing")

input_prompt_1 = """
You are an experienced Technical Human Resource Manager with experience in the field of Data Science, Devops, Web Developer,
DEVOPS, Data Analyst, Full stack development, Backend Devlopement, Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidte's profile aligns with the Job Description 
and highlight the strength and weaknesses of the applicant in relation to the specified job."""

input_prompt_2 = """
You are a skilled ATS(Applicant Tracking System) with a deep understanding in the field of Data Science, Devops, Web Developer,
DEVOPS, Data Analyst, Full stack development, Backend Devlopement and Deep ATS Functionality. Your task is to evaluate the resume against the provided job description.
First the output should come as a percentage match if the resume matches the job description and then the missing keywords.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt_1, pdf_content, input_text)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload a PDF")
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt_2, pdf_content, input_text)
        st.subheader("The response is")
        st.write(response)
    else:
        st.write("Please upload a PDF")
    
        
        
    
    


# In[ ]:





# In[ ]:




