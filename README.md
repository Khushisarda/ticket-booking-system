# 🎟️ Ticket Booking Management System(Assignment 2)

please watch the video
https://github.com/user-attachments/assets/fdd13d5b-6645-4d3a-afcf-5f14b68f45b1

## 📌 Project Overview  
The **Ticket Booking Management System** is a web-based application built with Django. It allows users to register, view available shows, and book tickets. Key features include secure user authentication, a custom admin panel for managing shows and bookings, and a personalized booking history page for users.

---

## 🚀 Setup & Run Instructions

### 🧰 Prerequisites
- Docker & Docker Compose installed  
- Jenkins (optional, for CI/CD)

### 🔧 Local Setup using Docker

Clone the repository:
```bash
git clone https://github.com/Khushisarda/ticket-booking.git
cd ticket-booking
```
## 🔧 Build and Run the Containers

```bash
docker-compose up --build
```
### Access the Application
#### Web App: http://localhost:8000

#### MySQL DB: Port 3307 on host (maps to 3306 inside container)

### Run Migrations and Create Superuser
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```
### 🛠️ Tech Stack Used
##### Backend: Django (Python)

Database: MySQL 8

Frontend: HTML, CSS, Bootstrap

DevOps: Docker, Docker Compose, Jenkins

Version Control: Git & GitHub

### 🐳 Docker Notes
The application runs in a multi-container Docker environment:

web: Django web application

db: MySQL 8 database

Configuration Highlights
MySQL port mapped from container (3306) to host (3307)

Docker volumes are used for persistent database storage

A custom Docker network ensures secure internal communication

Key Commands
#### Start containers
docker-compose up --build

#### Stop containers
docker-compose down
## 🧪 Jenkins CI/CD Notes
A Jenkinsfile is provided to automate the CI/CD pipeline.

Pipeline Stages
Build – Installs dependencies and builds Docker images

Test – Placeholder for unit tests or linters

Deploy – Uses Docker Compose to deploy the app

Integration Notes
Configure GitHub webhooks to trigger Jenkins jobs on push

Jenkins requires the Docker Pipeline and Git plugins

Jenkins agent should have Docker and Docker Compose installed
```bash
Sample Jenkinsfile
groovy

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker-compose build'
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Run tests here"'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
