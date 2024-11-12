from langchain_huggingface import HuggingFaceEndpoint  # type: ignore
from api_key import hugging_face_api_key
from langchain.prompts import PromptTemplate  # type: ignore 

import os 
import re  
import streamlit as st  # type: ignore


os.environ['HUGGINGFACEHUB_API_TOKEN'] = hugging_face_api_key


repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"


llm = HuggingFaceEndpoint(
    repo_id=repo_id, 
    temperature=0.6,
    token=hugging_face_api_key, 
)


prompt_template_for_title_suggestion = PromptTemplate(
    input_variables=['topic'],
    template =  
    '''
    I'm planning a blog post on topic : {topic}.
    The title is informative, or humorous, or persuasive. 
    The target audience is beginners, tech enthusiasts.  
    Suggest a list of ten creative and attention-grabbing titles for this blog post. 
    Don't give any explanation or overview to each title.
    '''
)

title_suggestion_chain = prompt_template_for_title_suggestion | llm 


prompt_template_for_title = PromptTemplate(
    input_variables=['title', 'keywords', 'blog_length'],  
    template=  
    '''Write a high-quality, informative, and plagiarism-free blog post on the topic: "{title}". 
    Target the content towards a beginner audience. 
    Use a conversational writing style and structure the content with an introduction, body paragraphs, and a conclusion. 
    Try to incorporate these keywords: {keywords}. 
    Aim for a content length of {blog_length} words. 
    Make the content engaging and capture the reader's attention.'''
)

title_chain = prompt_template_for_title | llm 


st.title("AI Blog Content Generator")
st.header("User Friendly Blog Creator")

st.subheader('Title Generation') 
topic_expander = st.expander("Input the topic") 


with topic_expander:
    topic_name = st.text_input("", key="topic_name") 
    submit_topic = st.button('Submit topic') 

if submit_topic: 
    title_selection_text = '' 
    title_suggestion_str = title_suggestion_chain.invoke({topic_name})
    for sentence in title_suggestion_str.split('\n'): 
        title_selection_text += (sentence.strip() + '\n') 
    st.text(title_selection_text) 


st.subheader('Blog Generation') 
title_expander = st.expander("Input the title")


with title_expander: 
    title_of_the_blog = st.text_input("", key="title_of_the_blog") 
    num_of_words = st.slider('Number of Words', min_value=100, max_value=1000, step=50) 


    if 'keywords' not in st.session_state: 
        st.session_state['keywords'] = [] 
    keyword_input = st.text_input("Enter a keyword:") 
    keyword_button = st.button("Add Keyword") 
    if keyword_button: 
        st.session_state['keywords'].append(keyword_input) 
        st.session_state['keyword_input'] = "" 
        for keyword in st.session_state['keywords']:  
            st.write(f"<div style='display: inline-block; background-color: lightgray; padding: 5px; margin: 5px;'>{keyword}</div>", unsafe_allow_html=True)

   
    submit_title = st.button('Submit Info')

if submit_title: 
    formatted_keywords = []
    for i in st.session_state['keywords']: 
        if len(i) > 0:
            formatted_keywords.append(i.lstrip('0123456789 : ').strip('"').strip("'"))  
    formatted_keywords = ', '.join(formatted_keywords)

    st.subheader(title_of_the_blog) 
    st.write(title_chain.invoke({'title': title_of_the_blog, 'keywords': formatted_keywords, 'blog_length':num_of_words})) # Generate and display the blog content using the title chain
