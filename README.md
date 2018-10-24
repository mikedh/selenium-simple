# mikedh/selenium-simple

Boilerplate for one option to test Javascript blob web apps. It uses headless Chrome inside the Selenium Docker images to run a simple integration test in Python. If you attach [sentry.io](https://sentry.io) to the logger, when the web app is down it sends you angry emails until you fix things.

The idea is you would use this as boilerplate, and then put your tests inside `integration/base.py` after generating them with something like Katalon and editing by hand.

## Quick Start
To run, use docker-compose:
```
docker-compose build
docker-compose up
```
