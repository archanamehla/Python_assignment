# ETL Pipeline using Docker Compose

## Overview
This project implements an ETL (Extract, Transform, Load) pipeline that reads data from a pipe-separated file, transforms the data according to specific requirements, and loads it into a MongoDB database. The application is Dockerized using Docker Compose for easy deployment.

## Requirements
- Python 3.8+
- MongoDB
- Docker Compose
- Docker Desktop

## Setup Instructions by any of below option
1. Clone the repository:
2. Source code copy to destination folder

## Running the ETL Pipeline
1. To execute the ETL pipeline, run the main Python script:
2. docker desktop must be running
3. docker-compose up

## Docker Compose Configuration
The Docker Compose file defines two services: the Python application service for running the ETL pipeline and the MongoDB service.

## Directory Structure
- /tests: Contains unit test
- /app: Contains the source code for the ETL pipeline and main.py
- docker-compose.yml: Configuration for Docker Compose

## Authors
- Archana Mehla