import os

# stop all jobs
for i in range(1, 51):
	os.system('nomad stop -purge linear_' + str(i))
