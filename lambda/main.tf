
data "archive_file" "this" {
  type        = "zip"
  source_dir  = "${path.module}/src"
  output_path = "${path.module}/src.zip"

}
resource "aws_iam_role" "lambda_exec" {
  name = var.lambda_function_name
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"
      Sid    = ""
      Principal = {
        Service = "lambda.amazonaws.com"
      }
    }]
  })
}
resource "aws_lambda_function" "this" {
  filename         = "${path.module}/src.zip"
  function_name    = var.lambda_function_name
  runtime          = var.lambda_runtime
  role             = aws_iam_role.lambda_exec.arn
  source_code_hash = data.archive_file.this.output_base64sha256
  handler          = var.lambda_handler
  environment {
    variables = {
      START_EVENT = "start"
      STOP_EVENT  = "stop"
      TAG_KEY     = "rds-scheduled-start-stop"
      TAG_VALUE   = "true"
    }
  }
}

resource "aws_iam_role_policy_attachment" "this" {
  for_each   = var.policy_arns
  role       = aws_iam_role.lambda_exec.name
  policy_arn = each.value
}
