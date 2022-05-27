module "eventbridge" {
  source        = "../eventbridge"
  start_cron    = "0 10 * * ? *"
  stop_cron     = "0 10 * * ? *"
  lambda_arn    = module.lambda.lambda_arn
  function_name = module.lambda.lambda_name
  region        = "us-east-1"
  depends_on = [
    module.lambda
  ]
}
module "lambda" {
  source         = "../lambda"
  lambda_runtime = "python3.8"
  lambda_handler = "func.lambda_handler"
  policy_arns    = ["arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole", "arn:aws:iam::aws:policy/AmazonRDSFullAccess", "arn:aws:iam::aws:policy/ResourceGroupsandTagEditorReadOnlyAccess"]
  region         = "us-east-1"
}
