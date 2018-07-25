provider "aws" {
    access_key = "${var.provider["access_key"]}"
    secret_key = "${var.provider["secret_key"]}"
    region = "${var.provider["region"]}"
}


resource "aws_s3_bucket" "honestbee-nginx-logs" {
    bucket  = "${var.bucket_name}"
    acl     = "private"
    
    tags {
      Name = "honestbee-nginx-logs"
      Environment = "test"
    }
}

