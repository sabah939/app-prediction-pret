# -*- coding: utf-8 -*-
# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# import pickle
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.preprocessing import StandardScaler
# from sklearn import preprocessing
# import streamlit as st
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os
# 
# 
# 
# primaryColor="#2214c7"
# backgroundColor="#ffffff"
# secondaryBackgroundColor="#e8eef9"
# textColor="#000000"
# font="sans serif"
# st.set_page_config(page_title="application de prediction de pret", page_icon=":smiley:", layout="centered")
# st.write("Cette application analyse les données d'un client qui souhaite demander un pret bancaire et predit si le prêt peut lui etre accordé ou pas par la banque")
# 
# st.sidebar.header("Veuillez saisir les valeurs :")
# credit_history = st.sidebar.slider('antedecedent de credit' , 0, 1)
# loan_amount = st.sidebar.slider('montant du pret', 0, 100000)
# ApplicantIncome = st.sidebar.slider('revenues du demandeurs', 0, 25000)
# CoapplicantIncome = st.sidebar.slider('revenues du codemandeur', 0, 25000)
# Loan_Amount_Term = st.sidebar.slider('durée du montant (en jours)', 0, 720)
# Dependents = st.sidebar.slider('personnes à charge', 0, 3)
# def user_input():
#   data = {
#     'credit_history' : credit_history,
#     'loan_amount' : loan_amount,
#     'ApplicantIncome' : ApplicantIncome,
#     'CoapplicantIncome' : CoapplicantIncome,
#     'Loan_Amount_Term' : Loan_Amount_Term,
#     'Dependents' : Dependents
#          }
#   parametres_pret =pd.DataFrame(data,index=[0])
#   return parametres_pret
# 
# 
# 
# scaler=pickle.load(open('scaler.pkl','rb'))
# 
# df=user_input()
# nmp=df.to_numpy()
# print(df)
# st.write(df)
# 
# 
# df_scaled = scaler.transform(df.to_numpy())
# 
# print(df_scaled)
# model_pret=pickle.load(open('model1.pkl','rb'))
# res = model_pret.predict(df_scaled)
# #st.subheader(res)
# st.write("devrait-on accorder un pret à ce client ?")
# bouton = st.button("simuler")
# if bouton:
#   if res == [1]:
#     st.write("Oui, le pret est accordé")
#   else: 
#     st.write("Non, on ne peut pas accorder le pret à ce client")
#



#!nohub streamlit run app.py &
!streamlit run app.py &>/dev/null&
