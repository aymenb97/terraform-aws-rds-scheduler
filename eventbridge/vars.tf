variable "start_cron" {
  description = "Cron expression for wake up time"
}
variable "stop_cron" {
  description = "Cron Expression for bed time"
}
variable "start_event_name" {
  description = "Name of the Start event detail in Event Bridge"
  default     = "start"
}
variable "stop_event_name" {
  description = "Name of the Stop event detail in Event Bridge"
  default     = "stop"
}
variable "lambda_arn" {
  description = "ARN of the lambda function"
  type        = string
}
variable "function_name" {
  description = "Name of the lambda function"

  type = string

}
variable "region" {
  description = "AWS Region"
  type        = string
  default     = "us-east-1"
}
