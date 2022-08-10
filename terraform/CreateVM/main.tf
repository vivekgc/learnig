terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-west-2"
  access_key = "AKIAUAH2YDUU5J7ECUIF"
  secret_key = "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"
}

resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
resource "aws_instance" "web_server" {
  ami = aws_instance.app_server.ami
  instance_type = "t2.micro"
  tags = {
    Name = "ExampleAppServerInstance"
  }
}
output "app_imstace_ip" {
  description="instance"
  value = aws_instance.app_server.public_ip
}
output "web_imstace_ip" {
  description="instance"
  value = aws_instance.web_server.public_ip
}
