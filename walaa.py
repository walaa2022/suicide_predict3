import streamlit as st
import pickle as pkl
import base64
import pandas as pd

from sklearn.preprocessing import StandardScaler
scal=StandardScaler()

st.title ('Suicide prediction App')
st.image ('https://www.chathamsafetynet.org/wp-content/uploads/2021/08/Copy-of-Copy-of-PST-Logo-background-e1628697628477.png')

# front end elements of the web page 
html_temp = """ 
    <div style ="background-color:skyblue;padding:13px"> 
    <h1 style ="color:black;text-align:center;">suicide prediction App</h1> 
    </div> 
    """
      # display the front end aspect
st.markdown(html_temp, unsafe_allow_html = True) 
st.subheader('by Dr.Walaa Nasr')

st.write('The goal of this project is to gather data about people that might think of suicide attempts, to predict the suicide rates using Machine Learning algorithms and analyzing them to find correlated factors causing increase in suicide rates globally')

Age=st.selectbox ("Age",range(18,121,1))
              
Sex = st.radio("Select Gender: ", ('male', 'female'))              

Race = st.radio("Select Race: ", ('White', 'African_American', 'Hispanic', 'Asian', 'Native_American', 'Other'))  
         
Education = st.slider("Select education: ", 1, 6,20)

score = st.selectbox(" score of ADHD & MD: ", range(0,200,1))

subs = st.selectbox(" substance abuse: ", range(0,200,1))

legal = st.selectbox(" Legal issues: ", range(0,20,1))

Abuse = st.selectbox(" Abuse history: ", ('No', 'Physical', 'Sexual', 'Emotional', 'Physical&Sexual', 'Physical&Emotional', 'Sexual&Emotional', 'Physical&Sexual&Emotional'))

non_Subst_Dx = st.selectbox("non_substance_diagnosis:", ('none','one','more_than_one'))

Subst_Dx = st.selectbox("substance diagnosis:", ('none','one_Substance_related', 'two_substance_related', 'three_or_more_substance_related'))


df_new = {'Age': [Age], 'Sex':[Sex], "Race": [Race], 'Education': [Education], 'score':[score], 'subs':[subs], 'legal': [legal], 'Abuse': [Abuse], 'Non_Subs_Dx':[Non_Subs_Dx], 'Subs_Dx': [Subs_Dx]}

# Pre-processing user input  # convert inputs to DataFrame

if Sex=="male":
    male=1 
elif Sex=="female":
    female=2 
    
if Race=="white":
    white=1
elif Race=="African_American":
    African_American=2
elif Race=="Haspanic":
    Haspanic=3
elif Race=="Asian":
    Asian=4
elif Race=="Native_American":
    Native_American=5
elif Race=="Other":
    Other=6
        
if non_Subst_Dx=="none":
    none=0
elif non_Subst_Dx=="one":
    one =1
elif non_Subst_Dx=="more_than_one":
    more_than_one=2

if Subst_Dx=="none":
    none=0
elif Subst_Dx=="one_Substance_related":
    one_Substance_related=1
elif Subst_Dx=="two_substance_related":
    two_substance_related=2
elif Subst_Dx=="three_or_more_substance_related":
    three_or_more_substance_related=3

if Abuse=="No":
    No =0
elif Abuse=="Physical":
    Physical=1
elif Abuse=="Sexual":
    Sexual=2
elif Abuse=="Emotional":
    Emotional=3
elif Abuse=="Physical&Sexual":
    Physical&Sexual=4
elif Abuse=="Physical&Emotional":
    Physical&Emotional=5
elif Abuse=="Sexual&Emotional":
    Sexual&Emotional= 6       
else:
    Physical&Sexual&Emotional= 7 
               

features = pd.DataFrame(df_new, index=[0])
        
user_input=[Age,Sex,Race, Education, score, subs, legal, Abuse, Non_Subs_Dx, Subst_Dx]
user_input=user_input.split(",")
user_input=np.array(user_input)
user_input=user_input.reshape(1,-1)

user_input=scal.fit_transform(features)

predictx = xgb.predict(user_input)

if st.button("Predict"): 
    if(predictx[0]==1):
        st.error("Warning! this patient has chances of attempting suicide")
    else:
        st.success("this patient is healthy and are less likely to attempt suicide!")

# load transformer
#transformer = pkl.load(open('transformer.pk1','rb'))

#apply transformer on inputs
#x_new = transformer.transform (df_new)

# load model                      
#model = pkl.load(open('model.pkl' ,'rb'))


#predict the output
#suicide_predict= model.predict_proba(x_new)[0][1]

#st.markdown(f'## probability of suicidal attempts: {round(suicidal_predict, 2)}%')

#pred = preprocess(age,sex,cp,trestbps,restecg,chol,fbs,thalach,exang,oldpeak,slope,ca,thal)

#if st.button("Predict"):   
    
    
st.sidebar.subheader("About App")

st.sidebar.info("This web app is helps doctors to find out whether patients are at a risk of commiting suicidal attempts or not")
st.sidebar.info("Enter the required fields and click on the 'Predict' button to check whether your patient has risk for suicidal attempt")
st.sidebar.info("Don't forget to rate this app")

feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=5,step=1)

if feedback:
    st.header("Thank you for rating the app!")
    st.info("Caution: This is just a prediction and can't gaurantee that your patient will not try to suicide.") 

