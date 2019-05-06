docker-build:
	docker build -t linear_regression_app:latest -f ./Dockerfile .
	docker tag linear_regression_app:latest shah3am/linear_regression_app:latest

docker-push:
	docker push shah3am/linear_regression_app:latest

# run the docker container locally
docker-run:
	docker run -P shah3am/linear_regression_app:latest

docker: docker-build docker-push

nomad-run-task:
	nomad job run linear.nomad

nomad-stop-task:
	nomad stop -purge linear

ssh-linux-bastion:
	ssh -i keys/test-instance/test-instance.pem -A ubuntu@3.210.118.241

ssh-nomad-server:
	ssh -i keys/test-instance/test-instance.pem -A ubuntu@10.0.7.229

create-input-batches:
	python3 create_input_batches.py
