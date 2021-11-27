# Real-time twitter scraper microservice

## Purpose
This project is used as a microservice in an expanded project for performing sentiment analysis on a real-time basis.
This microservice will continously source tweets from twitter and stream them to other microservices using kafka.

The service will mostly use Twint to scrape tweets of Twitter and use Kafka to stream towards the other services.
The infrastructure consists of dockerized applications based on flask and deployed on Kubernetes.


TODO:
- Add github links to other repositories

## Installing Twint
Run command:
`pip3 install -r requirements.txt` 
[Source](https://github.com/twintproject/twint)

Afterwards run the follwing if having trouble running twint in a script:
`pip3 install --upgrade -e git+https://github.com/twintproject/twint.git@origin/master#egg=twint`
[Source](https://github.com/twintproject/twint/issues/384)