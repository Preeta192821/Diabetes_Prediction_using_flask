#By the help of Random Forest Classifier

#First, import all the relevant libraries
import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

def prediction(Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,Age):

	df = pd.read_csv(r"C:\Users\preet\Downloads\Datasets (1)\final data set\kaggle_diabetes.csv")

	#Replacing the 0 values from['Glucose','BloodPressure','SkinThickness','Insulin','BMI'] by NaN
	df_copy = df.copy(deep=True)
	df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']]

	#Replacing NaN value by mean, median depending upon distribution
	df_copy['Glucose'].fillna(df_copy['Glucose'].median(), inplace=True)
	df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].median(), inplace=True)
	df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].median(), inplace=True)
	df_copy['Insulin'].fillna(df_copy['Insulin'].median(), inplace=True)
	df_copy['BMI'].fillna(df_copy['BMI'].median(), inplace=True)

	# Model Building
	from sklearn.model_selection import train_test_split
	X = df.drop(columns='Outcome')
	y = df['Outcome']
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

	from sklearn.preprocessing import StandardScaler

	sc = StandardScaler()

	X_train_sc = sc.fit_transform(X_train)
	X_test_sc  = sc.transform(X_test)


	from sklearn.ensemble import RandomForestClassifier
	cl = RandomForestClassifier(n_estimators=20)
	cl.fit(X_train,y_train)


	prediction = cl.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,Bmi,DiabetesPedigreeFunction,Age]])
	return prediction

















