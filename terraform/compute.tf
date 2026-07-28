resource "aws_instance" "ai_platform" {

  ami                         = "ami-0f58b397bc5c1f2e8"
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.public.id
  vpc_security_group_ids      = [aws_security_group.ai_platform.id]
  associate_public_ip_address = true

  key_name = var.key_name

  tags = {
    Name = "${var.project_name}-ec2"
  }
}
