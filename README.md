# Monitoring App

This repository contains a simple monitoring application built with Python Flask. It provides a web interface to visualize system resource metrics such as CPU usage, RAM usage, disk usage, and GPU utilization.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.9 or later
- Docker
- AWS CLI configured with appropriate permissions
- An Amazon EKS cluster set up with nodes capable of running GPU workloads (if GPU monitoring is required)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/DemonXslayer47/monitoring-app.git
   cd monitoring-app

## Installation

To install dependencies, run the following command:

   ```bash
   pip install -r requirements.txt
```
## Building the Docker Image

To build the Docker image, execute the following command:

   ```bash
   docker build -t monitoring-app .
```
## Pushing the Docker Image to Amazon ECR

To push the Docker image to Amazon ECR, run the following command:

```bash
python ecr.py
```
## Deploying the Application to Amazon EKS

To deploy the application to Amazon EKS, execute the following command:

```bash
kubectl apply -f deployment.yaml
```
## Usage

To start the application, run the following command:

```bash
docker run -d -p 5000:5000 monitoring-app
```
Open a web browser and navigate to http://localhost:5000 to view the monitoring dashboard.

## How it looks :![image](https://github.com/DemonXslayer47/Monitoring-app/assets/129634823/35015657-cbb8-4955-88cb-8561cf33fcbc)

**Author :** `[Sreehari Thota (DemonXslayer47)]`


This README file contains instructions for building the Docker image, pushing it to Amazon ECR, deploying the application to Amazon EKS, and starting the application for usage.
