import streamlit as st
import numpy as np
import pandas as pd
import pickle

model = pickle.load(open("phishing.pkl",'rb'))

# Creating the app 
st.title("Phishing Website Detector")
st.markdown("Upload the details of the website : ")


NumDots = st.number_input("Enter the number of dots in the link : ")
PathLevel = st.number_input("Enter the Path Level in the link : ")
NumDash = st.number_input("Enter the number of Dashes in the link : ")
NumSensitiveWords = st.number_input("Enter the number of Sensitive Words in the link : ")
PctExtHyperlinks = st.number_input("Enter the Extra Hyper Links : ")
PctExtResourceUrls = st.number_input("Enter the Extra Resource Urls : ")
InsecureForms = st.number_input("Enter the number of Insecure Forms : ")
PctNullSelfRedirectHyperlinks = st.number_input("Enter the Null Self Redirected Hyperlinks : ")
FrequentDomainNameMismatch = st.number_input("Enter the Frequent Domain Name Mismatch : ")
SubmitInfoToEmail = st.number_input("Is there the submit info to email : ")
IframeOrFrame = st.number_input("If I frame - 1 else 0 : ")
submit = st.button("Detect the site")

if submit :
    df = pd.DataFrame({"NumDots" : NumDots,"PathLevel": PathLevel,"NumDash" : NumDash,"NumSensitiveWords" : NumSensitiveWords,"PctExtHyperlinks" : PctExtHyperlinks,"PctExtResourceUrls" : PctExtResourceUrls,"InsecureForms" : InsecureForms,"PctNullSelfRedirectHyperlinks" : PctNullSelfRedirectHyperlinks,"FrequentDomainNameMismatch":FrequentDomainNameMismatch,"SubmitInfoToEmail":SubmitInfoToEmail,"IframeOrFrame":IframeOrFrame},index=[0])
    x = model.predict(df)
    if x == 0:
        st.title("Beware it might a Phishing Site")
    else:
        st.title("It is a good website to the max but take your privacy actions")