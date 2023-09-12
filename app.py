# import streamlit as st 

# st.title("Machine Learning project")
# st.header("Creating a UI")
# st.subheader("a small UI")
# st.text("Bhag jao sab")
# st.markdown("#This is first markdown")
# st.markdown("####This is second markdown")
# st.success("Successful done")
# st.info("Information")
# st.warning("This is a warning")
# st.error("This is an error")
# st.exception("Name error('name pd is not defined')")
# with st.sidebar:
#     st.title("This is Shikha")
#     if st.button("Issue resolved"):
#         st.write("Yes my issue is resolved")
# col1,col2=st.columns(2)
# with col1:
#     st.write("Names")
# with col2:
#     st.write("Issues")
# with col2:
#     some=st.text_input("Write something")
# if st.button("Submit"):
#     st.header(some)
# var =st.button("Are you in a mood to work now")
# if var:
#     st.write("Obviously i want to work")
#     st.title ("dot")
# import pandas
# st.help("pandas")
# from PIL import Image
# img=Image.open("tanu.jpg")
# st.image(img,width=300,caption="Simple Image")
# vid_file=open("videomovie1.mp4","rb")
# vid_bytes=vid_file.read()
# st.video(vid_bytes)
# #checkbox
# if st.checkbox("Show/Hide"):
#     st.text("Showing or Hiding widget")
# #Radiobutton
# status = st.radio("What is your status",("Active","Inactive"))


# #Link with some function
# if status=="Active":
#     st.success("You are active")
# else:
#     st.warning("Inactive,Activate it")

# #selectbox

# occupation=st.selectbox("Your occupation",["Programmer","Data Scientist","Doctor","Businessman"])
# st.write("You selected this option",occupation)

# #multiselect

# location=st.multiselect("Where have you worked",("Delhi","Mumbai","Karnataka","Pune"))
# st.write("You selected",len(location),"locations")
# #slider
# level=st.slider("What is your level",1,5)

# #Button
# st.button("Simple button")   
# if st.button("About"):
#     st.text("Streamlit is cool")    
# if st.button("Submit",key="1"):
#     st.text("Successfully submitted")

# #text input
# first_name=st.text_input("Enter your first name","Type here...") 
# if st.button("Submit",key="2"):
#     result=first_name.title()
#     st.success(result) 
# #textarea
# message=st.text_area("Enter your message","Type here...")  
# if st.button("Submit",key="3"):
#     result=message.title()
#     st.success(result) 

# #dateinput
# import datetime
# today=st.date_input("Today is",datetime.datetime.now())

# #time
# the_time=st.time_input("The time is",datetime.time())

# #display json function

# st.text("Display json data")
# st.json({"Name":"Tanu","Gender":"Female"})

# #import numpy as np

# st.text("Display raw code")
# st.code("import numpy as np")

# #display raw code with dataframe

# with st.echo():
#     import pandas as pd
#     df=pd.DataFrame()
# #progress bar
# import time
# my_bar=st.progress(0)
# for p in range(10):
#     my_bar.progress(p+10)

# #spinner
# with st.spinner("Waiting..."):
#     time.sleep(5)
# st.success("Finished")
# st.number_input("Give a number input")




import openai

import config

import streamlit as st

import markdown




openai.api_key = config.api




messages = [

    {'role': 'system', 'content': 'You are a Chatbot assistant Storyteller.Provide users with good story,You have to be Friendly to the user, solve all the queries user has, ask followup questions, explain the user as he is 18 year old'},

    {'role': 'user', 'content': 'I am Phoboe,Write a movie story for me'},

    {'role': 'assistant', 'content': 'Hello,Phoboe thats awesome,what type of story are you interested for'}

]





def format_messages(messages):

    formatted_messages = []

    for message in messages:

        formatted_messages.append(f"{message['role']}: {message['content']}")

    return '\n'.join(formatted_messages)





def get_response(messages):

    prompt = format_messages(messages)

    response = openai.Completion.create(

        engine='davinci',

        prompt=prompt,

        max_tokens=100

    )

    return response.choices[0].text.strip()





def update_chat(messages, role, content):

    messages.append({'role': role, 'content': content})

    return messages





st.title("Storyteller Bot")

user_input = st.text_input("User Input", "")




if st.button("Send"):

    messages = update_chat(messages, 'user', user_input)

    response = get_response(messages)

    messages = update_chat(messages, 'assistant', response)




    st.subheader("Chat History:")

    for message in messages:

        role = message['role']

        content = message['content']

        if role == 'user':

            st.markdown(f'**User:** {content}')

        elif role == 'assistant':

            st.markdown(f'**Assistant:** {content}')

        else:

            st.markdown(content)




    st.subheader("Response:")

    st.markdown(f'<div style="background-color: #f5f5f5; padding: 10px;">'

                f'<strong>Assistant:</strong> {response}</div>',

                unsafe_allow_html=True)



