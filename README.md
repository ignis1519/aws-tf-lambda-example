# aws-tf-lambda-example
An example for provisioning a Lambda function using Terraform

## This Solution and other available options

Using Lambda + API Gateway was the quickest option, it took me less than a hour to implement. The Terraform provider config stores the state in a S3 bucket, the resources implements all necessary dependencies for a lambda function and a API Gateway to expose GET requests to the `/hello` endpoint, which accepts a query parameter named `p_message` that allows for a dynamic string without re-deploying.

## The reasons behind the decisions you made

### AWS resources used

Other options for this same implementations are available, but would definetively be way more overkill for this simple use-case, options such as Fargate (requires container definition), App Runner (using Flask or some other web framework is a bit much just for this), an EC2 instance or even EKS would be a heavy overkill just for this. So Lambda + API Gateway makes more sense for this.

### Code organization

Organized the code by the single responsibility principle, so each Terraform file fulfills its role.

## How you would embellish the solution were you to have more time. 

A first change would be add security to the endpoint call, such as a API key requirement or other form of authentication. Also a more through handling of the request parameters.