# Phishing_Website_Detector_Using_ML_Using_Streamlit

By taking a dataset that contains meta data about 5000 legitimate and 5000 phishing sites. 
Phishing is a type of semantic attack, often used to steal user sensitive information including login credentials and credit card numbers by masquerading as a trusted entity, enticing a victim into clicking on link or opening an attachment in an email or instant message.

This is a large dataset with much better meta data information, for which you might have to understand the meaning of the meta data before working on the dataset.

![download](https://user-images.githubusercontent.com/82018631/212736363-f449ee2e-7e69-4e42-8958-00ffba5f4625.png)

# Details of the project

The project is divided into 3 parts:
-> Reading and understanding the data set<br \>
-> Building a machine learning model to predict the site is a phishing site or not <br \>
-> Get a pickle file from the machine leanring model <br \>
-> Create a UI and combine the pickle file with the UI

![what-is-phishing-in-cyber-security-scaled](https://user-images.githubusercontent.com/82018631/212736500-cdff43d5-7b84-4bbc-aaec-a06a38d257a3.jpg)


#About the model

So we start off with building machine learning model - we use a RandomForest Classifier model and train that model using phishing site datapoints There is abundant information - meta data of the sites which helps in recognizing the phishing sites In this particular project we will learn how to select features that we can use to train the model

