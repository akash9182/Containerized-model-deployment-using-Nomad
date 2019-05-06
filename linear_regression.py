import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import json
import s3
import os
import datetime

# Save to file in the current working directory
pkl_filename = "pickle_model.pkl"  
lm = LinearRegression()

def train():
       df = pd.read_csv('https://raw.githubusercontent.com/aashayshahh/data/master/USA_Housing.csv')
       X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
              'Avg. Area Number of Bedrooms', 'Area Population']]
       y = df[['Price']]
       X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
       # model = lm.fit(X_train,y_train)
       # with open(pkl_filename, 'wb') as file:  
       #        pickle.dump(model, file)
       return X_test, y_test

def predict(X_test):
	pickle_model = s3.read_pickle_model()
	return pickle_model.predict(X_test) 
	

