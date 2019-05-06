import boto3
import pickle
import os

#boto3 is used to read and write data from s3 buckets conveniently

bucket_name = 'rhombuscandidate'
resource = boto3.resource('s3')
rhombuscandidate_bucket = resource.Bucket(bucket_name)

# read test files from rhombuscandidate/input
def read_test_file(file_path):
	for obj in rhombuscandidate_bucket.objects.filter(Prefix=file_path):
		key = obj.key
		if key.endswith('.csv'):
			return obj.get()['Body'].read().decode('utf-8')

# read pickle file from rhombuscandidate/model
def read_pickle_model():
	for obj in rhombuscandidate_bucket.objects.filter(Prefix='model'):
		key = obj.key
		if key == 'model/pickle_model.pkl':
			return pickle.loads(obj.get()['Body'].read())

# write predictiuons to rhombuscandidate/predictions
def write_file_to_bucket(bucket_folder_name, file_name, file_path):
	rhombuscandidate_bucket.upload_file(file_path, os.path.join(bucket_folder_name, file_name))
