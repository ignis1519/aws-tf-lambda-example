terraform {
  backend "s3" {
    bucket = "cl.ignis"
    key    = "terraform/examples/lambda/terraform.tfstate"
    region = "us-east-1"
  }
}

provider "aws" {
  region = "us-east-1"
}
