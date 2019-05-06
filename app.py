import csv
import os
import sys
import s3
import pickle
import linear_regression
import pandas as pd
from sklearn.model_selection import train_test_split
import datetime

print(sys.version_info)
try:
	# reads input file names from the environment variable
	print(os.environ['input_file_name'])
	print('input_file_name available')
except:	
	print('input_file_name not available')
	sys.exit(1)
test_file_path = os.environ['input_file_name']

print('reading input file from s3 bucket')
test_data = s3.read_test_file(test_file_path)
print('done reading file from s3_bucket')

print('creating temp file containing contents of test_data from s3')
tempfile = os.path.join('tmp', str(datetime.datetime.now().time()))

# create a tmp directory if it doesn't already exist
if not (os.path.exists('tmp') and os.path.isdir('tmp')):
	print('creating tmp directory')
	os.mkdir('tmp')
print('done creating temp file ' + str(tempfile) + ', writing data to it')
with open(tempfile, 'w') as w:
	w.write(test_data)

print('done writing to tempfile, creating pandas dataframe')
df = pd.read_csv(tempfile)
print('done creating a pandas dataframe')

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
              'Avg. Area Number of Bedrooms', 'Area Population']]

print('running the model against test inputs')
predictions = linear_regression.predict(X)	

print('writing predictions to the s3 bucket')
predictions_file_name = str(datetime.datetime.now().time()) + '_' + test_file_path.split('/')[-1].split('.')[0] + '.txt'

predictions_file_path = predictions_file_name
with open(predictions_file_path, 'w') as f:
	for prediction in predictions:
		f.write(str(prediction[0]) + '\n')



s3.write_file_to_bucket('predictions', predictions_file_name, predictions_file_path)
print('done writing predictions to the s3 bucket')
