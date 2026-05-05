# CI/CD Pipeline — GitHub Actions, Docker, AWS ECR/ECS

Fully automated CI/CD pipeline that builds a Docker image, pushes it to Amazon ECR, and deploys it to AWS ECS Fargate using GitHub Actions. No manual deployment steps required.

---

## Pipeline Overview

```
Developer pushes code
        │
        ▼
GitHub Actions triggered
        │
        ▼
Build Docker image
        │
        ▼
Push image to Amazon ECR
        │
        ▼
Deploy to ECS Fargate
        │
        ▼
ALB routes traffic to updated container
```

---

## What This Builds

- GitHub Actions workflow triggered on every push to main
- Docker image built and pushed to Amazon ECR
- ECS Fargate service updated with new image automatically
- Application Load Balancer routing traffic to ECS service
- IAM roles with least-privilege permissions for deployment
- ECS deployment circuit breaker for automatic rollback on failure

---

## Project Structure

```
cicd-github-actions-ecs/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── app/
│   ├── app.py
│   └── requirements.txt
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── terraform.tfvars
├── Dockerfile
└── README.md
```

---

## Prerequisites

- AWS account with ECR and ECS configured
- GitHub repository secrets configured:
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `AWS_REGION`
  - `ECR_REPOSITORY`
  - `ECS_CLUSTER`
  - `ECS_SERVICE`

---

## How It Works

1. Developer pushes code to the main branch
2. GitHub Actions detects the push and starts the pipeline
3. Docker image is built from the Dockerfile
4. Image is tagged and pushed to Amazon ECR
5. ECS service is updated with the new image
6. ECS circuit breaker rolls back automatically if deployment fails

---

## Key Concepts Demonstrated

- Containerization with Docker
- Automated CI/CD with GitHub Actions
- Amazon ECR for private container registry
- ECS Fargate for serverless container deployment
- IAM least-privilege for deployment credentials
- Automatic rollback with ECS circuit breaker

---

## Stack

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
