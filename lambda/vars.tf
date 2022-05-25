variable "lambda_function_name" {
  description = "Name of the lambda function"
  type        = string
  default     = "lambda-rds-start-stop"
}
variable "lambda_runtime" {
  description = "Runtime of the lambda function"
  type        = string
}
variable "policy_arns" {
  description = "Policies for the lambda function"
  type        = set(string)
}
variable "lambda_handler" {
  description = "Lambda Handler name"
  type        = string
}

variable "region" {
  description = "Region"
  type        = string
}
