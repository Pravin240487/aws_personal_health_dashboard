# AWS Personal Health Dashboard
Terraform example to build AWS Personal Health Dashboard

## Content

- [Overview](#overview)
- [Requirements](#requirements)
- [Examples](#Examples)
- [AWS Personal Health Dashboard components](#aws-personal-health_dashboard-components)
- [Launchpad Policies](#launchpad-policies)
- [Referrenced Modules](#referrenced-modules)
- [Known Issues](#known-issues)
- [Support Details](#support-details)

## Overview:
AWS Personal Health Dashboard provides alerts and guidance for AWS events that might affect your environment. While the Service Health Dashboard shows the general status of AWS services, the Personal Health Dashboard provides proactive and transparent notifications about your specific AWS environment.  

Personal Health Dashboard is account specific, hence it provides notifications depending on the resources used specific to the account and also about the resources which can be accessed from others regions. 

## Requirements:
Supports:
Terraform ~> 0.14.10

## Examples

### [AWS_Personal_Health_Dashboard](/examples/aws_personal_health_dashboard/) <img src="https://dojo.o360.cloud/wp-content/uploads/2020/09/adequate.png" height="24px" />

This example provisions the AWS cloudwatch rule and lambda to trigger notification mails to distribution list about Personal Health Dashboard.

## AWS Personal Health Dashboard components:

Below AWS resources are built as part of this module,

1. Lambda function to notify PHD.
2. Cloudwatch rule to trigger Lambda.
3. Roles associated with Lambda.
4. Parameter store to hold the Azure mail server credentials to send mails to distribution list.

## Launchpad Policies

Health Care Cloud and Enterprise Information Security collaborate on an ongoing collection of security policies to identify and address severe security vulnerabilities. List of AWS Launchpad Policies are available [here](https://cloud.optum.com/docs/launchpad/aws-policies/).

The examples in this repository prevents the below Launchpad violations:

* [All AWS Security Group related policies](https://cloud.optum.com/docs/launchpad/aws-policies/#network-policies)

## Referrenced Modules

N/A

## Known Issues

N/A

## Support Details:

📧 - OA_Cloud_Support@ds.uhc.com
