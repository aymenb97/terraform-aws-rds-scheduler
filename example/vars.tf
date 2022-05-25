variable "lambda_function_name" {
  description = "Name of the lambda  function"
  type        = string
  default     = "rds-start-stop"
}
variable "lambda_runtime" {
  description = "Runtime environment for the lambda function"
  type        = string
  default     = "python3.8"
}
