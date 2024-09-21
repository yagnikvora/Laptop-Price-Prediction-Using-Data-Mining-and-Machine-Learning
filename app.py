import  streamlit as st
import pickle
import numpy as np

#import model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

#set the title of page
st.title("Laptop Price Predector")

#Laptop Brand
compony = st.selectbox('Brand',df['Company'].unique())

#Laptop type
type = st.selectbox('Type',df['TypeName'].unique())

#Ram of Laptop
ram = st.selectbox('Ram(in GBs)',[2,4,6,8,12,16,24,32,64])

#Weight of Laptop
weight = st.number_input("Weight of laptop")

#Touchscree
touchscreen = st.selectbox('Touchscreen',['Yes','No'])

#IPS
ips = st.selectbox('IPS',['Yes','No'])

#scree size
screen_size =  st.number_input("Screen Size")

#resolution
resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#CPU
cpu = st.selectbox('CPU Brand',df['Cpu Barnd'].unique())

#Hard Drive
hdd = st.selectbox('HDD(in GBs)',[0,128,256,512,1024,2048])

#SSD
ssd = st.selectbox('ssd(in GBs)',[0,128,256,512,1024])

#GPU
gpu = st.selectbox('GPU Brand',df['Gpu Brand'].unique())

#OS
os = st.selectbox('Operation System',df['OS'].unique())

if st.button('Predict the price'):
    try:
        if touchscreen == 'Yes':
            touchscreen = 1
        else:
            touchscreen = 0

        if ips == 'Yes':
            ips = 1
        else:
            ips = 0

        X_res = int(resolution.split('x')[0])
        Y_res = int(resolution.split('x')[1])

        ppi = (((X_res**2)+(Y_res**2))**0.5)/screen_size
        query = np.array([compony,type,ram,weight,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])

        query = query.reshape(1,12)
        st.title("Price of Laptop is : "+str(int(np.exp(pipe.predict(query))[0])))
    except ZeroDivisionError:
        st.title("Please enter all data")
