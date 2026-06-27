provider "aws" {
  region = "us-east-1"
}


resource "aws_s3_bucket" "my_bucket" {
  bucket = "remote-ecommerce-terraform-eks-state"

  lifecycle {
    prevent_destroy = false
  }

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}


resource  "aws_dynamodb_table" "my_table" {
  name           = "ecommerce-terraform-eks-state-lock"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name        = "My table"
    Environment = "Dev"
  }
}