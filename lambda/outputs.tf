output "lambda_arn" {
  description = "ARN of the lambda function"
  value       = aws_lambda_function.this.arn
}
output "lambda_name" {
  description = "Name of the lambda function"
  value       = aws_lambda_function.this.function_name
}
