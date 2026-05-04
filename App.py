import streamlit as st
from streamlit_option_menu import option_menu
import json
import streamlit as st  
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image
import requests

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Leela@123",
    database="phonepey",
    autocommit =True)
cursor = mydb.cursor()



def map_data(year,quarter):
    sql = """SELECT States, SUM(Transaction_amount) AS Total_Transaction_Value
             FROM aggregate_transaction
             WHERE Years =%s AND Quarter =%s
             GROUP BY States
             ORDER BY Total_Transaction_Value DESC;
           """
    cursor.execute(sql, (year,quarter))
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns =["state", "Total_Transaction_value"])
    return df

def map_data1(year,quarter):
    sql = """ SELECT States, SUM(RegisteredUser) AS Total_Registered_User
                        FROM map_user
                         WHERE Years =%s AND Quarter =%s
                        GROUP BY States
                        ORDER BY Total_Registered_User;
           """
    cursor.execute(sql, (year,quarter))
    data = cursor.fetchall()
    df = pd.DataFrame(data, columns =["state", "Total_Registered_User"])
    return df
def map_data2(year,quarter):
    sql = """ SELECT States, SUM(AppOpens) AS Opens
                        FROM map_user
                         WHERE Years =%s AND Quarter =%s
                        GROUP BY States
                        ORDER BY Opens;
           """
    cursor.execute(sql, (year,quarter))  
    data = cursor.fetchall()
    df2 = pd.DataFrame(data, columns =["state", "Opens"])
    return df2   

def map_data3(year,quarter):
    sql = """ SELECT States, SUM(Transaction_amount) AS Total_Transaction_amount
                        FROM aggregate_insurance
                         WHERE Years =%s AND Quarter =%s
                        GROUP BY States
                        ORDER BY Total_Transaction_amount;
           """
    cursor.execute(sql, (year,quarter))  
    data = cursor.fetchall()
    df2 = pd.DataFrame(data, columns =["state", "Total_Transaction_amount"])
    return df2
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
def map_data4(year,quarter):
    sql = """ SELECT States, SUM(Transaction_amount) AS Total_Transaction_amount
                        FROM map_transaction
                         WHERE Years =%s AND Quarter =%s
                        GROUP BY States
                        ORDER BY Total_Transaction_amount;
           """
    cursor.execute(sql, (year,quarter))  
    data = cursor.fetchall()
    df2 = pd.DataFrame(data, columns =["state", "Total_Transaction_amount"])
    return df2 

def map_data5(year,quarter):
    sql = """SELECT 
                States,
                SUM(RegisteredUser) AS Total_Users
                FROM top_user
                WHERE Years = %s AND Quarter = %s
                GROUP BY States
                ORDER BY Total_Users DESC
                LIMIT 10;
           """
    cursor.execute(sql, (year,quarter))  
    data = cursor.fetchall()
    df2 = pd.DataFrame(data, columns =["state", "Total_users"])
    return df2 

#streamlit part

page = st.sidebar.radio("Navigation",["Home","Data Exploration"])
if page =="Home":
    st.set_page_config(layout="wide")

    st.markdown("""
    <style>
    .stApp {
        
        background-image: url("https://www.phonepe.com/pulsestatic/847/pulse/static/49cd1894e0135924f5166e4e2e555c8a/16cfd/map.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        
       
    }
   
     </style>
    """, unsafe_allow_html=True)
    

    st.markdown("""
    <style>
    .block-container {
        background-color: rgba(0, 0, 0, 0.5);
        padding-top: 40px;
        padding: 20px;
        
        border-radius: 10px;
        color:white;
        font-weight:bold;
        text-shadow: 2px 2px 5px White;
        
    }</style>
                """, unsafe_allow_html=True)
    st.markdown("""
        <style>
        .stDownloadButton button {
            background-color: #FF4B4B;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        </style>
        """, unsafe_allow_html=True)
    st.title("PHONEPEY DATA ANALYSIS")
    col1,col2= st.columns(2)

    with col1:
        st.header("PHONEPEY")
        st.subheader("INDIA'S BEST TRANSACTION APP")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("****Credit & Debit card linking****")
        st.write("****Bank Balance check****")
        st.write("****Money Storage****")
        st.write("****PIN Authorization****")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.write("****No Wallet Top-Up Required****")
        st.write("****Pay Directly From Any Bank To Any Bank A/C****")
        st.write("****Instantly & Free****")

    with col2:
        st.image(Image.open(r"C:\Users\Welcome\Desktop\p2.jpg"),width=600)
        
        st.title("Digital payments in India: A US$10 Tn Opportunity")

        st.write("Check out the new phonepey pulse - BCG report on what the future holds for digital payments in India")

        url = "https://www.phonepe.com/pulsestatic/847/pulse/static/f555c4bfcd40323f01467e8cc1a65462/Pulse_Report_2021_L_Cr.pdf"
        response = requests.get(url)


        st.download_button(
            label=" Download the Report now",
                data=response.content,
                file_name="file.pdf",
                mime="application/pdf"
    )
 
   
elif page == "Data Exploration":
    st.header("DATA EXPLORATION")
    option = st.selectbox("Select any question",["1. Decoding Transaction Dynamics on Phonepe", 
                                                 "2. Device Dominannce and User Engagement",
                                                 "3. Insurance Penetration and Growth Potential Analysis",
                                                   "4. Transaction Analysis for Market Expansion",
                                                 "5. User Registration Analysis"])
    
    if option == "1. Decoding Transaction Dynamics on Phonepe":
        st.markdown('<h1 style ="color : red;">Total Transaction Amount Analysis</h1>', unsafe_allow_html= True)
        sql_y ="""
                 SELECT DISTINCT Years , Quarter
                    FROM aggregate_transaction
                    ORDER BY Years , Quarter;"""
        cursor.execute(sql_y) 

        data = cursor.fetchall()
        Year_quarter = pd.DataFrame(data,columns=["year","quarter"])
        col1,col2 = st.columns(2)
        with col1:
            Yr = st.selectbox("YEAR", list(Year_quarter["year"].unique()))
        with col2:
            qr = st.selectbox("QUARTER", list(Year_quarter["quarter"].unique()))


        m_data = map_data(int(Yr), int(qr))
        df = m_data
        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey="properties.ST_NM",
            locations="state",
            color="Total_Transaction_value",
            color_continuous_scale="blues"
        )
        fig.update_geos(fitbounds = "locations", visible = False)
        st.plotly_chart(fig)

        st.markdown('<h1 style ="color : red;">Distribution of Transaction Amount </h1>', unsafe_allow_html= True)
        sql ="""
                SELECT Transaction_type,
                SUM(Transaction_count) AS total_transaction_count,
                SUM(Transaction_amount) AS total_transaction_amount
                FROM aggregate_transaction
                GROUP BY Transaction_type
                ORDER BY total_transaction_count DESC;"""
        
        cursor.execute(sql)
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=["Transaction_type", "Total_Transaction_Count", "Total_Transaction_amount"])
        col1,col2 = st.columns(2)
        with col1:
            fig1 = px.pie(df,
                          names="Transaction_type",
                          values ="Total_Transaction_Count",
                          title = "Ditribution of Total Transaction Count",
                          hole = 0.4,
                          labels = {"Transaction_type":"Transaction Type"},
                           
                         )
            fig1.update_layout(
                        legend=dict(
                            x=1.2,   
                            y=0.5
                        ),
                        margin=dict(r=200) 
)
                          
            st.plotly_chart(fig1)
        
        with col2:
            fig2 = px.pie(df,
                names="Transaction_type",
                values ="Total_Transaction_amount",
                title = "Ditribution of Total Transaction Amount",
                hole = 0.4,
                labels = {"Transaction_type":"Transaction Type"},
                
                         )
            fig2.update_layout(
                        legend=dict(
                            x=1.2,   
                            y=0.5
                        ),
                        margin=dict(r=200))



       
            st.plotly_chart(fig2)

        st.markdown('<h1 style ="color : red;">Top 10 State Wise Total Transaction Amount</h1>', unsafe_allow_html= True)
        sql2 = """
                     SELECT States, SUM(Transaction_amount) AS total_transaction_amount
                        FROM aggregate_transaction
                        GROUP BY States
                        ORDER BY total_transaction_amount DESC
                        LIMIT 10;"""
            
        cursor.execute(sql2)
        data = cursor.fetchall()
        df2 = pd.DataFrame(data, columns =["state","Total_Transation_Amount"])

        fig3= px.bar(
            df2, x= "state",
            y="Total_Transation_Amount",
            text = "Total_Transation_Amount",
            title = "Total Transation Amount by State",
            labels={"state":"State","Total_Transaction_Amount":"Transaction_Amount"},

        )
        fig3.update_traces(texttemplate ='%{text:2s}',textposition="outside")

            
        st.plotly_chart(fig3)


        st.markdown('<h1 style ="color : red;">Transaction by State and Payment Category</h1>', unsafe_allow_html= True)
        sql4="""
              SELECT States,
                Transaction_type,
                SUM(Transaction_count) AS total_transactions,
                SUM(Transaction_amount) AS total_transction_amount
                FROM aggregate_transaction
                GROUP BY States, Transaction_type
                ORDER BY States, total_transactions DESC; """
        cursor.execute(sql4)
        data = cursor.fetchall()
        df3 = pd.DataFrame(data, columns =["state", "Transaction_Type", "total_transaction","Total_transaction_Amount"])
        State_options = df3["state"].unique()
        selected_State= st.selectbox("Select a State",State_options)
        filtered_df = df3[df3["state"]== selected_State]


        fig_1 = px.line(
             filtered_df,
                x="Transaction_Type",
                y="Total_transaction_Amount",
                 
                title=f"Quarterly Trend in {selected_State}",
                markers=True
            )
        fig_1.update_traces(line=dict(color="blue"))

        st.plotly_chart(fig_1)
        

        st.markdown('<h1 style ="color : red;">Trend Analysis</h1>', unsafe_allow_html= True)
        
        sql5 ="""
                 SELECT DISTINCT Years,  Quarter,SUM(Transaction_amount) AS Total_Transaction_Amount
                    FROM aggregate_transaction
                    GROUP BY Years,Quarter
                    ORDER BY  Total_Transaction_Amount ;"""
        cursor.execute(sql5)
        data= cursor.fetchall()
        df4 =pd.DataFrame(data, columns =["Year", "Quarter","Total_Transaction_Amount"])
        
       
        Year_options = df4["Year"].unique()
        selected_Year= st.selectbox("Select the Quarter",Year_options)
        filtered_df1 = df4[df4["Year"]== selected_Year]
        print(filtered_df1)

        fig5 = px.bar(
                    filtered_df1,
                    x="Quarter",
                    y="Total_Transaction_Amount",
                    orientation="v",  
                    text="Total_Transaction_Amount",
                    title=f"TRANSACTION FOR THE {selected_Year}",
                    labels={"QUARTER":"Quarter","Total_Transaction_Amount":"Transaction_Amount"},
)
        fig5.update_traces(texttemplate ='%{text:2s}',textposition="outside")

            
        st.plotly_chart(fig5)

    if option == "2. Device Dominannce and User Engagement":
        st.markdown('<h1 style ="color : red;">Brand-wise Transaction Distribution Across Top 10 States</h1>', unsafe_allow_html= True)
        sql1="""
                 select States, Brands,
                    SUM(Transaction_count) AS Total_Transaction_Count
                    FROM aggregate_user
                    GROUP BY States, Brands
                    ORDER BY Total_Transaction_Count DESC
                    LIMIT 20;"""
        cursor.execute(sql1) 

        data = cursor.fetchall()
        df1 = pd.DataFrame(data, columns=["State", "Brand", "Total_Transaction_count"])
        
        fig1=fig = px.bar(
                df1,
                x="State",
                y="Total_Transaction_count",
                color="Brand",
                title="Brand Contribution per State"
           )
        st.plotly_chart(fig1)

        st.markdown('<h1 style ="color : red;">Total Transaction Count Analysis</h1>', unsafe_allow_html= True)
        sql_2 ="""
                 SELECT DISTINCT Years , Quarter
                    FROM aggregate_transaction
                    ORDER BY Years , Quarter;"""
        cursor.execute(sql_2) 

        data = cursor.fetchall()
        print(data)
        Year_quarter = pd.DataFrame(data,columns=["year","quarter"])
        col1,col2 = st.columns(2)
        with col1:
            Yr = st.selectbox("YEAR", list(Year_quarter["year"].unique()))
        with col2:
            qr = st.selectbox("QUARTER", list(Year_quarter["quarter"].unique()))


        m_data = map_data1(int(Yr), int(qr))
        df1 = m_data
        m_data2 =map_data2(int(Yr),int(qr))
        df2= m_data2
        col1,col2 = st.columns(2)
        with col1:
                fig = px.choropleth(
                    df1,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey="properties.ST_NM",
                    locations="state",
                    color="Total_Registered_User",
                    color_continuous_scale="blues"
                )
                fig.update_geos(fitbounds = "locations", visible = False)
                st.plotly_chart(fig)
        with col2:
            fig2 = px.choropleth(
                    df2,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey="properties.ST_NM",
                    locations="state",
                    color="Opens",
                    color_continuous_scale="blues"
                )
            fig2.update_geos(fitbounds = "locations", visible = False)
            st.plotly_chart(fig2)
        
        st.markdown('<h1 style ="color : red;">Top Performing District</h1>', unsafe_allow_html= True)
        sql1="""
                 SELECT States,Quarter,District, SUM(AppOpens) AS Opens
                    FROM map_user
                    GROUP BY States, Quarter, District
                    ORDER BY Opens DESC
                    limit 20;"""
        cursor.execute(sql1) 

        data = cursor.fetchall()
        df1 = pd.DataFrame(data, columns=["State", "quarter", "District","opens"])
        
        fig = px.bar(
                df1,
                x="District",
                y="opens",
                color="State",
                title="Top 10 Districts by App Opens"
)

           
        st.plotly_chart(fig)
        st.markdown('<h1 style ="color : red;">Brand Wise Transaction Distribution</h1>', unsafe_allow_html= True)
        sql ="""
             SELECT Brands,
                SUM(Transaction_count) AS total_transaction_count
                FROM aggregate_user
                GROUP BY Brands
                ORDER BY total_transaction_count DESC;"""
        
        cursor.execute(sql)
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=["Brand", "total_transaction_count"])
        col1,col2 = st.columns(2)
        with col1:
            fig1 = px.pie(df,
                          names="Brand",
                          values ="total_transaction_count",
                          title = "Ditribution of Total Transaction Count",
                          hole = 0.4,
                          labels = {"Brand":"Transaction Brand"})
          

            fig1.update_layout(
                        legend=dict(
                            x=1.05,
                            y=0.5
                        ))
                     
                           
     
            st.plotly_chart(fig1)
    if option == "3. Insurance Penetration and Growth Potential Analysis":
        st.markdown('<h1 style ="color : red;">Total Insurance Transaction Amount by State</h1>', unsafe_allow_html= True)
        sql_y ="""
                 SELECT DISTINCT Years , Quarter
                    FROM aggregate_insurance
                    ORDER BY Years , Quarter;"""
        cursor.execute(sql_y) 

        data = cursor.fetchall()
        Year_quarter = pd.DataFrame(data,columns=["year","quarter"])
        col1,col2 = st.columns(2)
        with col1:
            Yr = st.selectbox("YEAR", list(Year_quarter["year"].unique()))
        with col2:
            qr = st.selectbox("QUARTER", list(Year_quarter["quarter"].unique()))


        m_data = map_data3(int(Yr), int(qr))
        df = m_data
        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey="properties.ST_NM",
            locations="state",
            color="Total_Transaction_amount",
            color_continuous_scale="blues"
        )
        fig.update_geos(fitbounds = "locations", visible = False)
        st.plotly_chart(fig)

        st.markdown('<h1 style ="color : red;">State-wise Transaction Distribution </h1>', unsafe_allow_html= True)
        sql1="""
                 SELECT 
                    m.States,
                    SUM(m.Transaction_count) AS Insurance_Transactions,
                    SUM(u.RegisteredUser) AS Total_Users
                    FROM map_insurance m
                    JOIN map_user u 
                    ON m.States = u.States 
                    AND m.Years = u.Years 
                    AND m.Quarter = u.Quarter
                    GROUP BY m.States
                    Order By Insurance_Transactions DESC
                    Limit 20;"""
        cursor.execute(sql1) 

        data = cursor.fetchall()
        df1 = pd.DataFrame(data, columns=["State", "Insurance_Transactions", "Total_Users"])
        
        fig = px.bar(
                df1,
                x="State",
                y="Insurance_Transactions",
                
                title="Total Transaction Amount by State"
           )
        st.plotly_chart(fig)

        st.markdown('<h1 style ="color : red;">Trend Analysis</h1>', unsafe_allow_html= True)
        sql1="""
                 SELECT 
                    m.States,
                    SUM(m.Transaction_count) AS Insurance_Transactions,
                    SUM(u.RegisteredUser) AS Total_Users
                    FROM map_insurance m
                    JOIN map_user u 
                    ON m.States = u.States 
                    AND m.Years = u.Years 
                    AND m.Quarter = u.Quarter
                    GROUP BY m.States
                    
                    """
        cursor.execute(sql1) 

        data = cursor.fetchall()
        df1 = pd.DataFrame(data, columns=["State", "Insurance_Transactions", "Total_Users"])
        fig = px.line(df1,
              x="State",
              y=["Total_Users","Insurance_Transactions"],
              markers = True,
              title="Users vs Insurance Transactions")
        
        
        st.plotly_chart(fig)
    if option == "4. Transaction Analysis for Market Expansion":
        st.markdown('<h1 style ="color : red;">Total Insurance Transaction Amount by State</h1>', unsafe_allow_html= True)
        sql ="""
             SELECT 
                States,
                SUM(Transaction_count) AS Total_Transactions
                FROM map_transaction
                GROUP BY States
                ORDER BY Total_Transactions DESC;"""
        
        cursor.execute(sql)
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=["state", "total_transaction_count"])
        
        fig1 = px.bar(df,
                          x="state",
                          y ="total_transaction_count",
                          title = "Ditribution of Total Transaction Count",)
                          
          

        st.plotly_chart(fig1)

        st.markdown('<h1 style ="color : red;">State Wise Transaction Amount</h1>', unsafe_allow_html= True)
        sql_y ="""
                 SELECT DISTINCT Years , Quarter
                    FROM top_transaction
                    ORDER BY Years , Quarter;"""
        cursor.execute(sql_y) 

        data = cursor.fetchall()
        Year_quarter = pd.DataFrame(data,columns=["year","quarter"])
        col1,col2 = st.columns(2)
        with col1:
            Yr = st.selectbox("YEAR", list(Year_quarter["year"].unique()))
        with col2:
            qr = st.selectbox("QUARTER", list(Year_quarter["quarter"].unique()))


        m_data = map_data4(int(Yr), int(qr))
        df = m_data
        fig = px.choropleth(
            df,
            geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
            featureidkey="properties.ST_NM",
            locations="state",
            color="Total_Transaction_amount",
            color_continuous_scale="blues"
        )
        fig.update_geos(fitbounds = "locations", visible = False)
        st.plotly_chart(fig)

        st.markdown('<h1 style ="color : red;">Pincode wise Transaction Analysis</h1>', unsafe_allow_html= True)
        sql1="""
                 SELECT 
                    Pincodes,
                    SUM(Transaction_count) AS Total_Transactions
                    FROM top_transaction
                    GROUP BY Pincodes
                    ORDER BY Total_Transactions DESC
                    Limit 10;
                    
                    """
        cursor.execute(sql1) 

        data = cursor.fetchall()
        df1 = pd.DataFrame(data, columns=["pincode", "Total_Transactions"])
        fig = px.pie(df1,
             names="pincode",
             values="Total_Transactions",
             hole=0.4,
             title="Top 10 Pincode-wise Transaction Share")
        st.plotly_chart(fig)

    if option == "5. User Registration Analysis":
       
        st.markdown('<h1 style ="color : red;">District Wise Registered User</h1>', unsafe_allow_html= True)
        sql2 = """
                    SELECT 
                    District,
                    SUM(RegisteredUser) AS Total_Users
                    FROM map_user
                    
                    GROUP BY District
                    ORDER BY Total_Users DESC
                    Limit 20;"""
            
        cursor.execute(sql2)
        data = cursor.fetchall()
        df2 = pd.DataFrame(data, columns =["District","Total_user"])

        
        fig_5= px.bar(df2,
             x="District",
             y="Total_user",
             orientation='v',
             title="Top Districts by Registered Users")

        st.plotly_chart(fig_5)
        st.markdown('<h1 style ="color : red;">State Wise Regisered User</h1>', unsafe_allow_html= True)
        sql2 = """
                   SELECT 
                    States,
                    District,
                    SUM(RegisteredUser) AS Total_Users
                FROM map_user
                
                GROUP BY States, District
                ORDER BY Total_Users DESC
                Limit 20;
                    """
    
            
        cursor.execute(sql2)
        data = cursor.fetchall()
        df2 = pd.DataFrame(data, columns =["states","District","Total_user"])

        
        fig_4 = px.bar(df2,
             x="states",
             y="Total_user",
             color="District",
             title="District-wise Users per State")



        st.plotly_chart(fig_4)
        



        st.markdown('<h1 style ="color : red;">Active Registered users per state</h1>', unsafe_allow_html= True)
        sql_1="""
                SELECT 
                States,
                SUM(RegisteredUser) AS Users,
                SUM(AppOpens) AS App_Opens
                FROM map_user
                GROUP BY States;
                    
                    """
        cursor.execute(sql_1) 

        data = cursor.fetchall()
        df_1 = pd.DataFrame(data, columns=["State", "user", "App_opens"])
        fig_2 = px.line(df_1,
              x="State",
              y=["user","App_opens"],
              markers = True,
              title="Users vs opens per state")
        
        
        st.plotly_chart(fig_2,key="active_user_Line_Chart")

