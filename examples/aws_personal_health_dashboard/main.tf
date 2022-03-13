locals {
  pkg  = "truss-aws-tools"
  name = "aws-health-notifier"
}

provider "aws" {

    region = "us-east-1"

  # Make it faster by skipping something
  skip_get_ec2_platforms      = true
  skip_metadata_api_check     = true
  skip_region_validation      = true
  skip_credentials_validation = true
  skip_requesting_account_id  = true
}

resource "random_pet" "this" {
  length = 2
}

#
# CloudWatch Event
#

resource "aws_cloudwatch_event_rule" "main" {
  name          = "${local.name}-${var.environment}"
  description   = "AWS Health Notifications"
  event_pattern = file("${path.module}/event-pattern.json")
}

resource "aws_cloudwatch_event_target" "main" {
  rule = aws_cloudwatch_event_rule.main.name
  #arn  = aws_lambda_function.main.arn
  arn  = module.lambda_function.lambda_function_arn
}

#
# Parameter store to store Azure SMTP password
#

resource "aws_ssm_parameter" "AzureSMTP" {
  name        = "Azure-SMTP"
  description = "The parameter description"
  type        = "SecureString"
  value       = var.AzureSMTP

  tags = {
    environment = "production"
  }
}

#
# Lambda Function
#

data "aws_iam_policy_document" "lamda_ssm" {
  statement {
    effect    = "Allow"
    actions   = ["ssm:GetParameters",
                "ssm:GetParameter"]
    #resources = ["arn:aws:codebuild:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:project/${module.codebuild.name}"]
    resources = ["*"]
  }
}


module "lambda_function" {
  source = "git::https://github.com/terraform-aws-modules/terraform-aws-lambda.git?ref=v2.0.0"

  publish = true

  function_name = "Notifications-lambda-PHD"
  handler       = "index.lambda_handler"
  runtime       = "python3.8"

  environment_variables = {
    mail_receivers         = var.mail_receivers
    sender                 = var.sender
  }



  source_path = [
    "${path.module}/../../fixtures/python3.8-app1/index.py",
  ]
  attach_policy_json = true
  policy_json        = data.aws_iam_policy_document.lamda_ssm.json
}