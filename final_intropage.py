# -*- coding: utf-8 -*-
"""Final_IntroPage

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZmKs_QWzptZDa01JMTDeZyzuxf4XNH03
"""

!pip install streamlit --quiet
!pip install pyngrok --quiet
!pip freeze > requirements.txt

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import streamlit as st
# import pandas as pd
# from PIL import Image
# 
# ## image_pregnant = Image.open('pregnant.jpeg')
# st.image(image_pregnant, width=100)
# 
# 
# st.title("How do symptoms of maternal physical health impact pregnancy risks?")
# 
# st.sidebar.header("Dashboard")
# st.sidebar.markdown("---")
# app_mode = st.sidebar.selectbox('Select Page',['Introduction'])
# 
# st.markdown("##### Objectives")
# st.markdown("We aim to see what indicators of physical health in pregnant women are most associated with high risk pregnancies.")
# 
# st.markdown("Gestastional diabetes (high blood glucose levels in pregnant people) affects 2%-10% of pregnancies for women in the U.S")
# st.markdown("Hypertention occurs in 1 out of every 12-17 pregnacies in women in the U.S. and is only increasing with time.")
# 
# df = pd.read_csv("Maternal Health Risk Data Set.csv")
# 
# num = st.number_input('No. of Rows', 5, 10)
# 
# head = st.radio('View from top (head) or bottom (tail)', ('Head', 'Tail'))
# if head == 'Head': 
#   st.dataframe(df.head(num))
# else:
#   st.dataframe(df.tail(num))
# 
# st.text('(Rows,Columns)')
# st.write(df.shape)
# 
# st.markdown("##### Key Variables")
# st.markdown("- Age of patient")
# st.markdown("- Systolic Blood Pressure")
# st.markdown("- Diastolic Blood Pressure")
# st.markdown("- Blood Glucose Levels")
# st.markdown("- Body Temperature")
# st.markdown("- Heart Rate")
# st.markdown("- Risk Level (High, Medium, Low")
# 
# st.markdown("*Systolic blood pressure indicates how much pressure your blood is exerting against your artery walls when the heart beats")
# st.markdown("*Diastolic blood pressure indicates how much pressure your blood is exerting against your artery walls while the heart is resting between beats")
# st.markdown("Both are equally important indicators in diagnosing hypertension. The chance of experiencing hypertension increases during pregnancy and can lead to strokes, immediate labor inductions and eclampsia.")
# 
# st.markdown("High blood glucose levels increases the chance of the baby being born too early, weigh too much, or with breathing problems.")
# 
# st.markdown("Over the course of pregnancy your blood volume increases by nearly 50%, so your heart rate speeds up significantly to account for the extra blood flow. So generally having a high heart rate is normal, but in rare cases can lead to  ")
# 
# st.markdown("### Description of Data")
# st.dataframe(df.describe())
# st.markdown("Descriptions for all quantitative data **(rank and streams)** by:")
# 
# st.markdown("Count")
# st.markdown("Mean")
# st.markdown("Standard Deviation")
# st.markdown("Minimum")
# st.markdown("Quartiles")
# st.markdown("Maximum")
# 
# st.markdown("### Missing Values")
# st.markdown("Null or NaN values.")
# 
# dfnull = df.isnull().sum()/len(df)*100
# totalmiss = dfnull.sum().round(2)
# st.write("Percentage of total missing values:",totalmiss)
# st.write(dfnull)
# if totalmiss <= 30:
#   st.success("We have less then 30 percent of missing values, which is good. This provides us with more accurate data as the null values will not significantly affect the outcomes of our conclusions. And no bias will steer towards misleading results. ")
# else:
#   st.warning("Poor data quality due to greater than 30 percent of missing value.")
#   st.markdown(" > Theoretically, 25 to 30 percent is the maximum missing values are allowed, there's no hard and fast rule to decide this threshold. It can vary from problem to problem.")
# 
# st.markdown("### Completeness")
# st.markdown(" The ratio of non-missing values to total records in dataset and how comprehensive the data is.")
# 
# st.write("Total data length:", len(df))
# nonmissing = (df.notnull().sum().round(2))
# completeness= round(sum(nonmissing)/len(df),2)
# 
# st.write("Completeness ratio:",completeness)
# st.write(nonmissing)
# if completeness >= 0.80:
#   st.success("We have completeness ratio greater than 0.85, which is good. It shows that the vast majority of the data is available for us to use and analyze. ")    
# else:
#   st.success("Poor data quality due to low completeness ratio( less than 0.85).")

!streamlit run app.py & npx localtunnel --port 8501