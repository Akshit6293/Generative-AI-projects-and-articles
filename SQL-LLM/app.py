#!/usr/bin/env python
# coding: utf-8

# # SQL-LLM APP
# 

# In[ ]:


from dotenv import load_dotenv
load_dotenv() ## load all the enviornment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#configure our API key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

#Function to load google gemini model and provide sql query as response

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

## Function to retrieve query from the sql database

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
        
    return rows

## Define your prompt

prompt = [""" 
You are an expert in converting English questions to SQL query!
The SQL database has the name student and has the following columns - NAME, CLASS, SECTION, MARKS
For example:
Example 1- How many entries of records are present?, 
The SQL command willbe something like this- count(*) from student;
Example 2 - Tell me all the students studying in the data science class?
the sql command will be something like this- select * from students where class = "Data Science";
also the sql code should not have ''' in beginning or the end and sql word in the output
""" 
]


## streamlit app

st.set_page_config(page_title = "I can retrieve any SQL query")
st.header("Gemini app to retrieve SQL Data")
question = st.text_input("Input:", key ="input")
submit = st.button("Ask the question")

#if submit is clicked

if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, student.db)
    st.subheader("The response is")
    for row in response:
        print(row)
        st.header(row)

