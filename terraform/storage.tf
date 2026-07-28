resource "aws_s3_bucket" "artifacts" {

  bucket = var.bucket_name

  tags = {
    Name = "${var.project_name}-artifacts"
  }
}
