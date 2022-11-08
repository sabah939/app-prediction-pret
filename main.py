import pickle
import pandas as pd
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing
import streamlit as st
import numpy as np
import pandas as pd

primaryColor="#2214c7"
backgroundColor="#ffffff"
secondaryBackgroundColor="#e8eef9"
textColor="#000000"
font="sans serif"
st.set_page_config(page_title="application de prediction de pret", page_icon=":smiley:", layout="centered")
st.write("Cette application analyse les données d'un client qui souhaite demander un pret bancaire et predit si le prêt peut lui etre accordé ou pas par la banque")
 
st.sidebar.header("Veuillez saisir les valeurs :")
credit_history = st.sidebar.slider('antedecedent de credit' , 0, 1)
loan_amount = st.sidebar.slider('montant du pret', 0, 100000)
ApplicantIncome = st.sidebar.slider('revenues du demandeurs', 0, 25000)
CoapplicantIncome = st.sidebar.slider('revenues du codemandeur', 0, 25000)
Loan_Amount_Term = st.sidebar.slider('durée du montant (en jours)', 0, 720)
Dependents = st.sidebar.slider('personnes à charge', 0, 3)
def user_input():
   data = {
     'credit_history' : credit_history,
     'loan_amount' : loan_amount,
     'ApplicantIncome' : ApplicantIncome,
     'CoapplicantIncome' : CoapplicantIncome,
     'Loan_Amount_Term' : Loan_Amount_Term,
     'Dependents' : Dependents
          }
   parametres_pret =pd.DataFrame(data,index=[0])
   return parametres_pret
 
 
 
scaler=pickle.load(open('scaler.pkl','rb'))
 
df=user_input()
nmp=df.to_numpy()
print(df)
st.write(df)
 
 
df_scaled = scaler.transform(df.to_numpy())
 
print(df_scaled)
model_pret=pickle.load(open('model1.pkl','rb'))
res = model_pret.predict(df_scaled)
#st.subheader(res)
st.write("devrait-on accorder un pret à ce client ?")
bouton = st.button("simuler")
if bouton:
   if res == [1]:
     st.write("Oui, le pret est accordé")
   else: 
     st.write("Non, on ne peut pas accorder le pret à ce client")
 
 #Sauvegarde de données sur AWS
import boto3

def putNewRes(credit_history, loan_amount, ApplicantIncome, CoapplicantIncome, Loan_Amount_Term, Dependents, dynamodb=None):

  if not dynamodb:
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-3', aws_access_key_id='AKIAQ5AG5VAP52K4XJFY',
     aws_secret_access_key='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')
  newid = getNewId()
  id = str(newid)
  table = dynamodb.Table('prediction_pret_results')
  response = table.put_item(
    Item={
      'id': id,
      'credit_history': credit_history,
      'loan_amount': loan_amount,
      'ApplicantIncome': ApplicantIncome,
      'CoapplicantIncome': CoapplicantIncome,
      'Loan_Amount_Term': Loan_Amount_Term,
      'Dependents':Dependents 
    } )
  return response

def getNewId(dynamodb=None):
  if not dynamodb:
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-3', aws_access_key_id='AKIAQ5AG5VAP52K4XJFY',
     aws_secret_access_key='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')
  table = dynamodb.Table('prediction_pret_results')
  response = table.scan()
  return response['Count']
putNewRes(credit_history, loan_amount, ApplicantIncome, CoapplicantIncome, Loan_Amount_Term, Dependents)


