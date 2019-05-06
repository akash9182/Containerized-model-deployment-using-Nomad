import os

# create a new job for the corresponding 
# test input
def create_nomad_job(i):
	nomad_job = 'job "linear_' + str(i) + '" {'
	nomad_job += '''datacenters = ["us-east-1-private"]
    		type="batch"
	
    		group "python" {
        	count=1
        	task "linear_regression_app" {
                	driver = "docker"
                	config {
                		image = "shah3am/linear_regression_app:latest"
                	}
			env {'''

	nomad_job += 'input_file_name = "input/test_' + str(i) + '.csv"'
	nomad_job += '''}
       		}
	
    		}
	}'''
	return nomad_job

# interate over all test inputs and run
# nomad jobs for each of them
for i in range(1, 51):
	with open('linear.nomad', 'w') as f:
		f.write(create_nomad_job(i))
	os.system('nomad job run linear.nomad')
	

