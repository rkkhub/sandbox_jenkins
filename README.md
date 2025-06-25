# sandbox_jenkins
Testing self hosted jenkins setup


## init docker image 
docker build -t sb_jenkins .

## running test
docker run --rm -it sb_jenkins:latest
docker run --rm -it sb_jenkins:latest pytest