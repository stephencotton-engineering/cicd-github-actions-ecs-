# The AWS region to deploy resources into
variable "aws_region" {
  description = "AWS region to deploy resources"
  type        = string
  default     = "us-east-1"
}

# Name prefix for all resources
variable "project_name" {
  description = "Name prefix for all resources"
  type        = string
  default     = "stephen-cicd-project"
}

# The name of the ECR repository that stores Docker images
variable "ecr_repository_name" {
  description = "Name of the ECR repository"
  type        = string
  default     = "stephen-app"
}
