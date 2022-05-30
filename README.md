# terraform-rds-scheduler
Terraform module to create a lambda function to start/Stop RDS instances with a `scheduled-start-stop:true` tag triggered by two cron Eventbridge resources. 
## Features
- Creates two AWS Eventbridge resources.
- Attaches the resources to the default EventBridge Bus.
- Creates a Lambda function that starts/stops tagged instances based on the EventBridge Event.

## Usage
Specify in the `/example/main.tf` the cron expression for the `start_cron` and `stop_cron` variables.
An example is provided in the `example.tf` file.

in the example directory run:

```shell
$terraform init
```
```shell
$terraform plan
```
```shell
$terraform apply
```

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | n/a |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_cloudwatch_event_rule.start](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_rule) | resource |
| [aws_cloudwatch_event_rule.stop](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_rule) | resource |
| [aws_cloudwatch_event_target.lambda_start](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_target) | resource |
| [aws_cloudwatch_event_target.lambda_stop](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/cloudwatch_event_target) | resource |
| [aws_lambda_permission.allow_cloudwatch_start_to_invoke](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_permission) | resource |
| [aws_lambda_permission.allow_cloudwatch_stop_to_invoke](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_permission) | resource |
| [aws_iam_role.lambda_exec](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role) | resource |
| [aws_iam_role_policy_attachment.this](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/iam_role_policy_attachment) | resource |
| [aws_lambda_function.this](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) | resource |
| [archive_file.this](https://registry.terraform.io/providers/hashicorp/archive/latest/docs/data-sources/file) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_function_name"></a> [function\_name](#input\_function\_name) | Name of the lambda function | `string` | n/a | yes |
| <a name="input_lambda_arn"></a> [lambda\_arn](#input\_lambda\_arn) | ARN of the lambda function | `string` | n/a | yes |
| <a name="input_region"></a> [region](#input\_region) | AWS Region | `string` | `"us-east-1"` | no |
| <a name="input_start_cron"></a> [start\_cron](#input\_start\_cron) | Cron expression for wake up time | `any` | n/a | yes |
| <a name="input_start_event_name"></a> [start\_event\_name](#input\_start\_event\_name) | Name of the Start event detail in Event Bridge | `string` | `"start"` | no |
| <a name="input_stop_cron"></a> [stop\_cron](#input\_stop\_cron) | Cron Expression for bed time | `any` | n/a | yes |
| <a name="input_stop_event_name"></a> [stop\_event\_name](#input\_stop\_event\_name) | Name of the Stop event detail in Event Bridge | `string` | `"stop"` | no |
| <a name="input_lambda_function_name"></a> [lambda\_function\_name](#input\_lambda\_function\_name) | Name of the lambda function | `string` | `"lambda-rds-start-stop"` | no |
| <a name="input_lambda_handler"></a> [lambda\_handler](#input\_lambda\_handler) | Lambda Handler name | `string` | n/a | yes |
| <a name="input_lambda_runtime"></a> [lambda\_runtime](#input\_lambda\_runtime) | Runtime of the lambda function | `string` | n/a | yes |
| <a name="input_policy_arns"></a> [policy\_arns](#input\_policy\_arns) | Policies for the lambda function | `set(string)` | n/a | yes |
| <a name="input_region"></a> [region](#input\_region) | Region | `string` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_lambda_arn"></a> [lambda\_arn](#output\_lambda\_arn) | ARN of the lambda function |
| <a name="output_lambda_name"></a> [lambda\_name](#output\_lambda\_name) | Name of the lambda function |
