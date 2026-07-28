output "instance_public_ip" {
  value = aws_instance.ai_platform.public_ip
}

output "instance_public_dns" {
  value = aws_instance.ai_platform.public_dns
}

output "instance_id" {
  value = aws_instance.ai_platform.id
}

output "bucket_name" {
  value = aws_s3_bucket.artifacts.bucket
}
