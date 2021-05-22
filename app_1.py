import streamlit as st
import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
import base64

st.write("Hello, upload CSV dataset")
st.write("---------------------------------------")

data_csv = st.file_uploader("Upload CSV", type=["csv"])

if(data_csv is not None):
	st.write(type(data_csv))
	data = pd.read_csv(data_csv)
	st.write(data.head())


	st.write("---------------------------------------")

	st.write("What needs to be removed?")
	c_names = list(data.columns.values)
	cToD = []
	for i in c_names:
		cToD.append(st.checkbox(i))
	# st.write(cToD)

	for i in range(len(cToD)):
		if(cToD[i]):

			data = data.drop(columns=[c_names[i]])

	st.write(data.head())

	st.write("---------------------------------------")
	st.write("Enter target class:")

	lc = []
	for i in c_names:
		lc.append(i)
	lc = tuple(lc)
	tc = st.radio("Target Class", lc, index=len(lc)-1)
	st.write(tc)

	st.write("---------------------------------------")
	c_names = list(data.columns.values)
	y_n0 = st.radio("Remove Nan value rows?", ("Yes", "No"), index=1)

	if(y_n0 == "Yes"):
		for i in range(len(c_names)):
			data = data.dropna()
		st.write(data.head())
	elif(y_n0 == "No"):
		st.write(data.head())


	st.write("---------------------------------------")

	y = data[tc]
	x = data.drop(columns=tc)

	st.write("X:")
	st.write(x.head())
	st.write("Y:")
	st.write(y.head())

	x = x.values
	y = y.values


	y_n1 = st.radio("Would u like to split it into train and test data?", ("Yes", "No"), index=1)
	if(y_n1 == "Yes"):
		test_sz = st.slider("Test size(in %)", 0.00, 1.00, value = 0.2, step = 0.01)
		rs = st.number_input("Random State", 1, value=1234, step=1)
		x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=test_sz, random_state=rs)

		# st.write(x_train)
		# st.write(y_train)
		# st.write(x_test)
		# st.write(y_test)
		c_names.remove(tc)

		x_trainDF = pd.DataFrame(x_train, columns=c_names)
		x_testDF  = pd.DataFrame(x_test , columns=c_names)

		y_trainDF = pd.DataFrame(y_train, columns=[tc])
		y_testDF  = pd.DataFrame(y_test , columns=[tc])

		# st.write(x_trainDF)
		# st.write(y_trainDF)
		# st.write(x_testDF)
		# st.write(y_testDF)

		# csv = x_trainDF.to_csv().encode()
		# b64 = base64.b64encode(csv).decode()
		# href = f'Download CSV File'

		csv = x_trainDF.to_csv().encode()
		b64 = base64.b64encode(csv).decode()
		href = f'<a href="data:file/csv;base64,{b64}" download="x_train.csv" target="_blank">Download <b>x_train</b></a>'
		st.markdown(href, unsafe_allow_html=True)

		csv = x_testDF.to_csv().encode()
		b64 = base64.b64encode(csv).decode()
		href = f'<a href="data:file/csv;base64,{b64}" download="x_test.csv" target="_blank">Download <b>x_test</b></a>'
		st.markdown(href, unsafe_allow_html=True)

		csv = y_trainDF.to_csv().encode()
		b64 = base64.b64encode(csv).decode()
		href = f'<a href="data:file/csv;base64,{b64}" download="y_train.csv" target="_blank">Download <b>y_train</b></a>'
		st.markdown(href, unsafe_allow_html=True)

		csv = y_testDF.to_csv().encode()
		b64 = base64.b64encode(csv).decode()
		href = f'<a href="data:file/csv;base64,{b64}" download="y_test.csv" target="_blank">Download <b>y_test</b></a>'
		st.markdown(href, unsafe_allow_html=True)

		st.write("---------------------------------------")
	elif(y_n1 == "No"):
		c_names.remove(tc)
		xDF  = pd.DataFrame(x , columns=c_names)

		yDF = pd.DataFrame(y, columns=[tc])

		csv = xDF.to_csv().encode()
		b64 = base64.b64encode(csv).decode()
		href = f'<a href="data:file/csv;base64,{b64}" download="x.csv" target="_blank">Download <b>X</b></a>'
		st.markdown(href, unsafe_allow_html=True)

		csv = yDF.to_csv().encode()
		b64 = base64.b64encode(csv).decode()
		href = f'<a href="data:file/csv;base64,{b64}" download="y.csv" target="_blank">Download <b>Y</b></a>'
		st.markdown(href, unsafe_allow_html=True)
		st.write("---------------------------------------")

else:
	time.sleep(1)

