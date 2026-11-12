# DevOps Lab 🚀

A hands-on DevOps learning project focused on building, testing, containerising, and automatically deploying a Flask application using GitHub Actions, Docker, and an Ubuntu Server virtual machine.

The goal is to learn practical DevOps workflows by implementing them in a real environment.

## Project Overview

This project demonstrates a basic Continuous Integration and Continuous Deployment (CI/CD) pipeline.

Whenever code is pushed to the `main` branch or a pull request is opened against it, GitHub Actions runs automated checks and builds a Docker image.

When changes are successfully pushed to `main`, the pipeline connects to my Ubuntu Server VM through Tailscale and SSH, then deploys the updated application.

## Technologies Used

- **Python & Flask** — Web application
- **Git & GitHub** — Version control and collaboration
- **GitHub Actions** — CI/CD automation
- **Docker** — Application containerisation
- **Docker Compose** — Container management
- **Ubuntu Server** — Deployment environment
- **Tailscale** — Private network connectivity
- **SSH (Ed25519)** — Secure remote access
- **Flake8** — Python code linting
- **pip-audit** — Python dependency vulnerability scanning
- **pytest** — Test framework

## Application Features

The Flask application currently provides two endpoints:

| Endpoint | Description |
|---|---|
| `/` | Displays the application homepage |
| `/health` | Returns the application's health status |

Example health response:

```json
{
  "status": "healthy"
}
```

## Project Structure

```text
DevOps-Lab/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   └── CI-CD.md
├── docker-compose.yml
└── .gitignore
```

## Running the Application Locally

Clone the repository:

```bash
git clone https://github.com/kcee01/DevOps-Lab.git
cd DevOps-Lab
```

Install the dependencies:

```bash
pip install -r app/requirements.txt
```

Run the application:

```bash
python app/app.py
```

Open the application at:

```text
http://localhost:5000
```

Check the health endpoint:

```text
http://localhost:5000/health
```

## Running with Docker

Build the Docker image:

```bash
docker build -t devops-lab-web ./app
```

Run the container:

```bash
docker run -d \
  --name flask-app \
  -p 5000:5000 \
  devops-lab-web
```

Verify the health endpoint:

```bash
curl http://localhost:5000/health
```

Alternatively, use Docker Compose:

```bash
docker compose up -d --build
```

Stop the application:

```bash
docker compose down
```

## CI/CD Pipeline

The project uses GitHub Actions to automate the build, verification, and deployment process.

### Continuous Integration (CI)

The `build-test` job runs on pushes and pull requests targeting `main`.

It performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.12.
3. Installs application dependencies.
4. Runs Flake8 code linting.
5. Scans dependencies using pip-audit.
6. Runs pytest if a `tests` directory exists.
7. Builds the Docker image.
8. Starts a test container and checks the `/health` endpoint.

### Continuous Deployment (CD)

The `deploy` job runs only after successful CI checks on a push to `main`.

The deployment process:

1. Connects the GitHub Actions runner to the private Tailscale network.
2. Loads the dedicated SSH deployment key.
3. Establishes a secure SSH connection to the Ubuntu Server VM.
4. Executes a restricted deployment script.
5. Pulls the latest code from `main`.
6. Rebuilds and restarts the application using Docker Compose.

The deployment credentials are stored in GitHub repository secrets rather than committed to the repository.

## Deployment Environment

The application is deployed to an Ubuntu Server virtual machine.

Docker Compose manages the Flask container, while Tailscale provides private network connectivity between GitHub Actions and the server.

The application's health endpoint was verified after deployment and returned:

```text
HTTP 200 OK
{"status":"healthy"}
```

## Learning Objectives

This project is part of my practical DevOps learning journey. It focuses on:

- Understanding CI/CD pipelines.
- Working with Linux server environments.
- Managing containers with Docker.
- Automating deployments.
- Applying secure SSH access practices.
- Integrating automated code quality and security checks.
- Improving software delivery through automation.

## Future Improvements

Planned enhancements include:

- AI-powered pull request reviews using CodeRabbit.
- SSH hardening and improved key management.
- Encrypted backups using GPG and rclone.
- Database integration with PostgreSQL.
- Self-hosted automation services using n8n.
- Application monitoring and error tracking.
- Automated testing and performance testing.

---

**Author:** Cliff Keabetswe

**Repository:** https://github.com/kcee01/DevOps-Lab
