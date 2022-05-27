resource "aws_cloudwatch_event_rule" "start" {
  name                = "start-event"
  description         = "Start all stopped instances on Schedule"
  schedule_expression = "cron(${var.start_cron})"
}

resource "aws_cloudwatch_event_rule" "stop" {
  name        = "stop-event"
  description = "Stop all started instances on Schedule"
  #schedule_expression = "rate(2 minutes)"
  schedule_expression = "cron(${var.stop_cron})"

}

resource "aws_cloudwatch_event_target" "lambda_start" {
  rule      = aws_cloudwatch_event_rule.start.name
  target_id = "lambda_function"
  arn       = var.lambda_arn
  input     = <<JSON
  {
  "EventType": "${var.start_event_name}"
  }
 JSON
}
resource "aws_cloudwatch_event_target" "lambda_stop" {
  rule      = aws_cloudwatch_event_rule.stop.name
  target_id = "lambda_function"
  arn       = var.lambda_arn
  input     = <<JSON
  {
   "EventType": "${var.stop_event_name}"   
  }
 JSON
}

resource "aws_lambda_permission" "allow_cloudwatch_start_to_invoke" {
  statement_id  = "AllowWaktimeExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = var.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.start.arn
}
resource "aws_lambda_permission" "allow_cloudwatch_stop_to_invoke" {
  statement_id  = "AllowBedtimeExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = var.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.stop.arn
}
