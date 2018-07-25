# docker-compose

Does the following
- run a nginx container using ubuntu base image.
- run a fluentd container using ubunutu base image.
- fluentd ships the nginx logs to AWS S3.

To run with docker-compose
```
docker-compose up -d
```
NOTE: Do not enclose AWS Credentials in double quotes while filling up docker-compose.yml
