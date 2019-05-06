# from linear_regression import predict
# from flask import Flask, abort, request
import csv
import json
import ast
import os
import s3
import pickle
import linear_regression
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://raw.githubusercontent.com/aashayshahh/data/master/USA_Housing.csv')
X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
              'Avg. Area Number of Bedrooms', 'Area Population']]

for i in range(0, len(X), 100):
	file_name = 'test_' + str(int(i/100)+1) + '.csv'
	file_path = os.path.join('inputs', file_name)
	X[i:i+100].to_csv(file_path)
	s3.write_file_to_bucket('input', file_name, file_path)

