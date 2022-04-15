import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import psycopg2
import postgreconnect

#Define a sql to fetch data from CARS table (PostgreSQL table hosted on Heroku)
sql='Select * from cars;'
#postgreconnect.runquery function is called by passing on the sql. The function runquery returns the data from the CARS table.
#The returned data is also converted into a DataFrame.
record=pd.DataFrame(postgreconnect.runquery(sql))
#The DataFrame lacked columns, hence they were added. 9 Columns. 
record.columns=['Name','Miles_Per_Gallon','Cylinders','Displacement','Horsepower','Weight_In_Lbs','Acceleration','Year','Origin']
#A title was given to the streamlit app.
st.title('Cars Data - Sourced from Heroku')
#The contents were printed on a table.
st.table(record)
