# Containerized-model-deployment-using-Nomad

- Created a cloud stack using AWS cloud formations to configure a virtual private cluster on AWS cloud.
- Deployed Nomad and Consul by HashiCorp on the VPC.
- Created a containerized linear regression model that could run on cloud using Nomad that takes an input of features from s3 bucket and pipes predictions directly into a s3 bucket.
- Trained the model offline and generated a pickle model.
- Automated launching of EC2 instances using Auto-Scaling and performed Load Balancing by integrating Fabio natively with Consul.
- Configured the cluster such that it was able to spin up EC2 instances when required to do the job and take them down when not in use.
