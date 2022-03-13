# Example: AWS Personal Health Dashboard  <img src="https://dojo.o360.cloud/wp-content/uploads/2020/09/adequate.png" height="24px" />

## Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Argument Reference](#argument-reference)
- [Attributes Reference](#attributes-reference)
- [Usage](#usage)
- [Known Issues](#known-issues)

## Overview

This example helps to send notification on AWS Personal Health Dashboard specific to account.

This example provisions the following AWS Resources:

1. Lambda function to notify PHD.
2. Cloudwatch rule to trigger Lambda.
3. Roles associated with Lambda.
4. Parameter store to hold the Azure mail server credentials to send mails to distribution list.

## Requirements

Supports:

| Name | Version |
|------|---------|
| terraform | >= 0.12.6, <= 0.14.10 |
| aws | >= 2.67, < 4.0 |
| random | ~> 2 |

## Argument Reference

The following arguments are supported:

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| allowed\_triggers | Map of allowed triggers to create Lambda permissions | `map(any)` | `{}` | no |
| artifacts\_dir | Directory name where artifacts should be stored | `string` | `"builds"` | no |
| attach\_async\_event\_policy | Controls whether async event policy should be added to IAM role for Lambda Function | `bool` | `false` | no |
| attach\_cloudwatch\_logs\_policy | Controls whether CloudWatch Logs policy should be added to IAM role for Lambda Function | `bool` | `true` | no |
| attach\_dead\_letter\_policy | Controls whether SNS/SQS dead letter notification policy should be added to IAM role for Lambda Function | `bool` | `false` | no |
| attach\_network\_policy | Controls whether VPC/network policy should be added to IAM role for Lambda Function | `bool` | `false` | no |
| attach\_policies | Controls whether list of policies should be added to IAM role for Lambda Function | `bool` | `false` | no |
| attach\_policy | Controls whether policy should be added to IAM role for Lambda Function | `bool` | `false` | no |
| attach\_policy\_json | Controls whether policy\_json should be added to IAM role for Lambda Function | `bool` | `false` | no |
| attach\_policy\_jsons | Controls whether policy\_jsons should be added to IAM role for Lambda Function | `bool` | `false` | no |
| attach\_policy\_statements | Controls whether policy\_statements should be added to IAM role for Lambda Function | `bool` | `false` | no |
| attach\_tracing\_policy | Controls whether X-Ray tracing policy should be added to IAM role for Lambda Function | `bool` | `false` | no |
| build\_in\_docker | Whether to build dependencies in Docker | `bool` | `false` | no |
| cloudwatch\_logs\_kms\_key\_id | The ARN of the KMS Key to use when encrypting log data. | `string` | `null` | no |
| cloudwatch\_logs\_retention\_in\_days | Specifies the number of days you want to retain log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1827, and 3653. | `number` | `null` | no |
| cloudwatch\_logs\_tags | A map of tags to assign to the resource. | `map(string)` | `{}` | no |
| compatible\_runtimes | A list of Runtimes this layer is compatible with. Up to 5 runtimes can be specified. | `list(string)` | `[]` | no |
| create | Controls whether resources should be created | `bool` | `true` | no |
| create\_async\_event\_config | Controls whether async event configuration for Lambda Function/Alias should be created | `bool` | `false` | no |
| create\_current\_version\_allowed\_triggers | Whether to allow triggers on current version of Lambda Function (this will revoke permissions from previous version because Terraform manages only current resources) | `bool` | `true` | no |
| create\_current\_version\_async\_event\_config | Whether to allow async event configuration on current version of Lambda Function (this will revoke permissions from previous version because Terraform manages only current resources) | `bool` | `true` | no |
| create\_function | Controls whether Lambda Function resource should be created | `bool` | `true` | no |
| create\_layer | Controls whether Lambda Layer resource should be created | `bool` | `false` | no |
| create\_package | Controls whether Lambda package should be created | `bool` | `true` | no |
| create\_role | Controls whether IAM role for Lambda Function should be created | `bool` | `true` | no |
| create\_unqualified\_alias\_allowed\_triggers | Whether to allow triggers on unqualified alias pointing to $LATEST version | `bool` | `true` | no |
| create\_unqualified\_alias\_async\_event\_config | Whether to allow async event configuration on unqualified alias pointing to $LATEST version | `bool` | `true` | no |
| dead\_letter\_target\_arn | The ARN of an SNS topic or SQS queue to notify when an invocation fails. | `string` | `null` | no |
| description | Description of your Lambda Function (or Layer) | `string` | `""` | no |
| destination\_on\_failure | Amazon Resource Name (ARN) of the destination resource for failed asynchronous invocations | `string` | `null` | no |
| destination\_on\_success | Amazon Resource Name (ARN) of the destination resource for successful asynchronous invocations | `string` | `null` | no |
| docker\_build\_root | Root dir where to build in Docker | `string` | `""` | no |
| docker\_file | Path to a Dockerfile when building in Docker | `string` | `""` | no |
| docker\_image | Docker image to use for the build | `string` | `""` | no |
| docker\_pip\_cache | Whether to mount a shared pip cache folder into docker environment or not | `any` | `null` | no |
| docker\_with\_ssh\_agent | Whether to pass SSH\_AUTH\_SOCK into docker environment or not | `bool` | `false` | no |
| environment\_variables | A map that defines environment variables for the Lambda Function. | `map(string)` | `{}` | no |
| file\_system\_arn | The Amazon Resource Name (ARN) of the Amazon EFS Access Point that provides access to the file system. | `string` | `null` | no |
| file\_system\_local\_mount\_path | The path where the function can access the file system, starting with /mnt/. | `string` | `null` | no |
| function\_name | A unique name for your Lambda Function | `string` | `""` | no |
| handler | Lambda Function entrypoint in your code | `string` | `""` | no |
| hash\_extra | The string to add into hashing function. Useful when building same source path for different functions. | `string` | `""` | no |
| kms\_key\_arn | The ARN of KMS key to use by your Lambda Function | `string` | `null` | no |
| lambda\_at\_edge | Set this to true if using Lambda@Edge, to enable publishing, limit the timeout, and allow edgelambda.amazonaws.com to invoke the function | `bool` | `false` | no |
| lambda\_role | IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See Lambda Permission Model for more details. | `string` | `""` | no |
| layer\_name | Name of Lambda Layer to create | `string` | `""` | no |
| layers | List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. | `list(string)` | `null` | no |
| license\_info | License info for your Lambda Layer. Eg, MIT or full url of a license. | `string` | `""` | no |
| local\_existing\_package | The absolute path to an existing zip-file to use | `string` | `null` | no |
| maximum\_event\_age\_in\_seconds | Maximum age of a request that Lambda sends to a function for processing in seconds. Valid values between 60 and 21600. | `number` | `null` | no |
| maximum\_retry\_attempts | Maximum number of times to retry when the function returns an error. Valid values between 0 and 2. Defaults to 2. | `number` | `null` | no |
| memory\_size | Amount of memory in MB your Lambda Function can use at runtime. Valid value between 128 MB to 3008 MB, in 64 MB increments. | `number` | `128` | no |
| number\_of\_policies | Number of policies to attach to IAM role for Lambda Function | `number` | `0` | no |
| number\_of\_policy\_jsons | Number of policies JSON to attach to IAM role for Lambda Function | `number` | `0` | no |
| policies | List of policy statements ARN to attach to Lambda Function role | `list(string)` | `[]` | no |
| policy | An additional policy document ARN to attach to the Lambda Function role | `string` | `null` | no |
| policy\_json | An additional policy document as JSON to attach to the Lambda Function role | `string` | `null` | no |
| policy\_jsons | List of additional policy documents as JSON to attach to Lambda Function role | `list(string)` | `[]` | no |
| policy\_statements | Map of dynamic policy statements to attach to Lambda Function role | `any` | `{}` | no |
| provisioned\_concurrent\_executions | Amount of capacity to allocate. Set to 1 or greater to enable, or set to 0 to disable provisioned concurrency. | `number` | `-1` | no |
| publish | Whether to publish creation/change as new Lambda Function Version. | `bool` | `false` | no |
| reserved\_concurrent\_executions | The amount of reserved concurrent executions for this Lambda Function. A value of 0 disables Lambda Function from being triggered and -1 removes any concurrency limitations. Defaults to Unreserved Concurrency Limits -1. | `number` | `-1` | no |
| role\_description | Description of IAM role to use for Lambda Function | `string` | `null` | no |
| role\_force\_detach\_policies | Specifies to force detaching any policies the IAM role has before destroying it. | `bool` | `true` | no |
| role\_name | Name of IAM role to use for Lambda Function | `string` | `null` | no |
| role\_path | Path of IAM role to use for Lambda Function | `string` | `null` | no |
| role\_permissions\_boundary | The ARN of the policy that is used to set the permissions boundary for the IAM role used by Lambda Function | `string` | `null` | no |
| role\_tags | A map of tags to assign to IAM role | `map(string)` | `{}` | no |
| runtime | Lambda Function runtime | `string` | `""` | no |
| s3\_bucket | S3 bucket to store artifacts | `string` | `null` | no |
| s3\_existing\_package | The S3 bucket object with keys bucket, key, version pointing to an existing zip-file to use | `map(string)` | `null` | no |
| s3\_object\_storage\_class | Specifies the desired Storage Class for the artifact uploaded to S3. Can be either STANDARD, REDUCED\_REDUNDANCY, ONEZONE\_IA, INTELLIGENT\_TIERING, or STANDARD\_IA. | `string` | `"ONEZONE_IA"` | no |
| s3\_object\_tags | A map of tags to assign to S3 bucket object. | `map(string)` | `{}` | no |
| source\_path | The absolute path to a local file or directory containing your Lambda source code | `any` | `null` | no |
| store\_on\_s3 | Whether to store produced artifacts on S3 or locally. | `bool` | `false` | no |
| tags | A map of tags to assign to resources. | `map(string)` | `{}` | no |
| timeout | The amount of time your Lambda Function has to run in seconds. | `number` | `3` | no |
| tracing\_mode | Tracing mode of the Lambda Function. Valid value can be either PassThrough or Active. | `string` | `null` | no |
| trusted\_entities | Lambda Function additional trusted entities for assuming roles (trust relationship) | `list(string)` | `[]` | no |
| use\_existing\_cloudwatch\_log\_group | Whether to use an existing CloudWatch log group or create new | `bool` | `false` | no |
| vpc\_security\_group\_ids | List of security group ids when Lambda Function should run in the VPC. | `list(string)` | `null` | no |
| vpc\_subnet\_ids | List of subnet ids when Lambda Function should run in the VPC. Usually private or intra subnets. | `list(string)` | `null` | no |

## Attributes Reference

The following attributes are exported:

| Name | Description |
|------|-------------|
| lambda\_cloudwatch\_log\_group\_arn | The ARN of the Cloudwatch Log Group |
| lambda\_role\_arn | The ARN of the IAM role created for the Lambda Function |
| lambda\_role\_name | The name of the IAM role created for the Lambda Function |
| local\_filename | The filename of zip archive deployed (if deployment was from local) |
| s3\_object | The map with S3 object data of zip archive deployed (if deployment was from S3) |
| this\_lambda\_function\_arn | The ARN of the Lambda Function |
| this\_lambda\_function\_invoke\_arn | The Invoke ARN of the Lambda Function |
| this\_lambda\_function\_kms\_key\_arn | The ARN for the KMS encryption key of Lambda Function |
| this\_lambda\_function\_last\_modified | The date Lambda Function resource was last modified |
| this\_lambda\_function\_name | The name of the Lambda Function |
| this\_lambda\_function\_qualified\_arn | The ARN identifying your Lambda Function Version |
| this\_lambda\_function\_source\_code\_hash | Base64-encoded representation of raw SHA-256 sum of the zip file |
| this\_lambda\_function\_source\_code\_size | The size in bytes of the function .zip file |
| this\_lambda\_function\_version | Latest published version of Lambda Function |
| this\_lambda\_layer\_arn | The ARN of the Lambda Layer with version |
| this\_lambda\_layer\_created\_date | The date Lambda Layer resource was created |
| this\_lambda\_layer\_layer\_arn | The ARN of the Lambda Layer without version |
| this\_lambda\_layer\_source\_code\_size | The size in bytes of the Lambda Layer .zip file |
| this\_lambda\_layer\_version | The Lambda Layer version |


## Usage

To run this example you need to execute:

```bash
$ terraform init
$ terraform plan
$ terraform apply
```

Note that this example may create resources which cost money. Run `terraform destroy` when you don't need these resources.

## Known Issues

None at this time.
