# DevOps Lab - CI/CD Pipeline

## Overview

This project uses GitHub Actions to automate testing and deployment
of a Flask application running inside Docker on an Ubuntu Server VM.

## Pipeline Stages

1. Checkout source code.
2. Set up Python 3.12.
3. Install application dependencies.
4. Run Flake8 code quality checks.
5. Scan dependencies using pip-audit.
6. Run automated tests when available.
7. Build and test the Docker image.
8. Connect securely to the server using Tailscale.
9. Deploy using SSH and Docker Compose.

## Deployment Architecture

- Source control: GitHub
- CI/CD: GitHub Actions
- Secure networking: Tailscale
- Remote access: SSH
- Containerization: Docker and Docker Compose
- Application: Python Flask
- Server: Ubuntu Server

## Deployment Trigger

A successful push to the `main` branch triggers the deployment job.
Pull requests run CI checks but do not deploy.

## Health Check

The application exposes:

`GET /health`

Expected response:

```json
{"status": "healthy"}

```

```
