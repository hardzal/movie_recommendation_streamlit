# Importing the necessary libraries
import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Adding an appropriate title for the test website
st.title("Streamlit For Model Deployment")

# Creating a side bar radio option for selecting the required elements
_radio = st.sidebar.radio("",
                          ("Fundamentals of streamlit", "Model Deployment using streamlit"))

if _radio == "Fundamentals of streamlit":
    # Creating a header in the fundamentals section
    st.header("Fundamental components of Streamlit")

    # Creating an appropriate subheader and looking at some of the basic elements
    st.subheader("Writing Elements")

    # Writing information
    st.write("Write Command: Writing details with the write command and the subheaders")

    # Creating a text box
    st.text("Text Component: This is a text box")

    # Display code
    with st.echo():
        import streamlit as st
        st.write("Writing Code")

    # Creating a button widget
    button1 = st.button("Click Here")

    # Creating additional text boxes
    if button1:
        st.markdown("*You clicked the button and the markdown is displayed*")

elif _radio == "Model Deployment using streamlit":
    # Creating a header in the model deployment section
    st.header("Deployment of Machine Learning Models with Streamlit")

    # Loading the model
    model_path = "model_test.h5"
    model = load_model(model_path, compile = False)
    
    # Uploading an image
    img_data = st.file_uploader(label="Image", accept_multiple_files=True)

    # Making the required prediction
    if img_data is not None and len(img_data) > 0:
        # Assigning a random count
        count = 0

        # Opening and displaying the image
        img = Image.open(img_data[count]) 
        st.image(img)

        # Converting into a numpy array
        img = np.array(img)
        img = np.expand_dims(img, 0)

        # Making the appropriate prediction
        prediction = model.predict(img)
        output = np.argmax(prediction)

        # Displaying the prediction
        st.write("The Predicted Result is: ", output)
        print(output)

    # While no image is uploaded
    else:
        st.write("Waiting For Upload of Image...")