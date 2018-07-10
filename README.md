# mikedh/selenium-simple
----------

A simple example of how to use headless Chrome inside the Selenium Docker images to run a simple integration test of a web app in Python.

The idea is you would use this as boilerplate, and then put your tests inside `integration/base.py` after generating them with something like Katalon and editing by hand.


## Quick Start
To run, use docker-compose:
```
docker-compose build
docker-compose up
```
