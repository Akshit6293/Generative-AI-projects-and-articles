import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input_prompt,image[0]])
    return response.text


def input_image_setup(uploaded_file):
    #check if the file is uploaded
    if uploaded_file is not None:
        ## read the file in bytes
        bytes_data = uploaded_file.get_value()

        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data   
        }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")
        
        
#streamlit app

st.set_page_config(page_title = "Calories Advisor App")
st.header("Gemini Health App")
uploaded_file = st.file_uploader("Choose an image...", type = ["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image.", use_column_width=True)
    
submit = st.button("Tell Me About Total Calories")

input_prompt_1 = """
    You are an expert nutritionist where you need to see the food items from the image and calculate the total calories,
    also provide the details of every food items with calories intake in below format:
    1. Item 1 - no. of calories
    2. item 2 - no. of claories
    ----
    ----
    finally you can also mention whether food is healthy or not and also mention
    percentage split of the ratio of carbohydrates, fats, fibers, sugar and other important
    things required in our diet

"""

if submit:
    image_data= input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt_1, image_data)
    st.subheader("The response is")
    st.write(response)
else:
    st.write("Please upload a image")
        
        
    
    