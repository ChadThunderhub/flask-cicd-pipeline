# Flask CI/CD Pipeline

A lightweight Flask web application featuring a fully automated Continuous Integration and Continuous Delivery (CI/CD) pipeline using GitHub Actions and Docker.

## Project Overview
This project demonstrates the implementation of modern DevOps practices on a lightweight web architecture. It serves as a portfolio piece showcasing containerization, automated testing, and seamless deployment workflows. 

## Tech Stack
* **Framework:** Flask (Python 3.12)
* **Containerization:** Docker & Docker Compose
* **CI/CD:** GitHub Actions
* **Frontend:** HTML5, Bootstrap 5 (Jinja2 Templates)
* **Package Management:** `pyproject.toml`

## Features
* **Automated CI/CD:** GitHub Actions workflow triggered on push/pull requests.
* **Dockerized Environment:** Isolated and reproducible environments using `python:3.12-slim`.
* **Production Grade:** Powered by Gunicorn with multi-worker setup for high concurrency.
* **Dynamic Content:** * Real-time server (UTC) vs. local client time rendering.
  * In-memory cached image gallery generation for optimized I/O performance.

## Getting Started

### Prerequisites
Make sure you have [Docker](https://www.docker.com/) and Docker Compose installed on your machine.

### Local Deployment
1. Clone the repository:
   ```bash
   git clone https://github.com/ChadThunderhub/flask-cicd-pipeline.git
   cd flask-cicd-pipeline

2. Build and start the container in detached mode:
    docker-compose up --build -d

3. Access the application at: http://localhost:5000

To stop the application, run:
    docker-compose down