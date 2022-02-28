import pickle
import streamlit as st
import pandas as pd

st.set_page_config(
     page_title="Ex-stream-ly Cool App",
     layout="centered",
 )

def recommend(x):
    index=drama[drama['Title'] == x ].index[0]
    distances=similarity[index]
    drama_list   = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])[1:6]

    recommend_drama_list=[]
    for i in drama_list:
        recommend_drama_list.append(drama.iloc[i[0]].Title)
    return recommend_drama_list

model=pickle.load(open('kdramas_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

drama=pd.DataFrame(model)
st.image("kdrama21.jpg",use_column_width=True)
st.title("Welcome to Korean drama recommendation ")


selecter_drama_name=st.selectbox(" ",drama['Title'].values)

if st.button('Recommend'):
    output=recommend(selecter_drama_name)
    for i in output:
        st.write(i)
st.image("king2.jpg",use_column_width=True)