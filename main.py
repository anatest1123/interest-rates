import streamlit as st
import numpy as np
from equations import interest_equation

u_optimal = st.sidebar.number_input("Optimal utilization rate",0,100,80)
r_v0 = st.sidebar.number_input("Base variable borrow rate",0,100,10)
r_s1 = st.sidebar.number_input("Rslope1",0,100,30)
r_s2 = st.sidebar.number_input("Rslope2",0,200,100)
y_axes = np.array(range(100))
for i in range(100):
    y_axes[i] = interest_equation(i,u_optimal,r_v0,r_s1,r_s2)
st.title("Interest calculator")
st.header("Interest Equation:" )
st.latex('R_{v} = R_{v0} + (U_{t} \div U_{optimal}) \\times R_{slope1} \: \\textrm{if} \: U_{t} \le \: U_{optimal}')
st.latex('R_{v} = R_{v0} + R_{slope1} + (U_{t} - U_{optimal}) \div (1 - U_{optimal}) \\times R_{slope2} \: \\textrm{if} \: U_{t} \ge \: U_{optimal}')

st.header("Interest graph")
st.line_chart(y_axes)
st.header("Input Utilisation rate")
input = st.number_input("Utilisation rate in %",0,100,0)
slider = st.slider('Get interest rate from Utilisation rate', min_value=0, max_value=100, value=input)
st.header("Interest rate:")
st.write(interest_equation(slider,u_optimal,r_v0,r_s1,r_s2))