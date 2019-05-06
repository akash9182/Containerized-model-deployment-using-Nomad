job "linear_50" {datacenters = ["us-east-1-private"]
    		type="batch"
	
    		group "python" {
        	count=1
        	task "linear_regression_app" {
                	driver = "docker"
                	config {
                		image = "shah3am/linear_regression_app:latest"
                	}
			env {input_file_name = "input/test_50.csv"}
       		}
	
    		}
	}