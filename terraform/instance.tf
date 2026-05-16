// Key pairs
resource "aws_key_pair" "coe_558_hw4_frontend_server" {
  key_name   = "coe-558-hw4-frontend-server-key"
  public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHivUB8yZJnn/jEIMSAl3J3V2zaktMNudIoKhyWULoxa coe558 hw4 frontend"
}

resource "aws_key_pair" "coe_558_hw4_backend_server" {
  key_name   = "coe-558-hw4-backend-server-key"
  public_key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIAj0QgV3t2AjkEh2iwLJr0ANf+TXOWxcCUtSr3fxDFjX coe558 hw4 backend"
}

// Instances EC2
resource "aws_instance" "coe_558_hw4_frontend_server" {
  ami = "ami-0281b0943230d40d1"
  instance_type = "t3.medium"
  availability_zone = var.av_zone
  subnet_id = "subnet-07856761a4ac292b1"
  key_name = aws_key_pair.coe_558_hw4_frontend_server.key_name
  user_data = file("${path.module}/scripts/install_docker.sh")
  vpc_security_group_ids = [
    "sg-09a862554f50c67bc"
  ]
  tags = {
    Name = "coe-558-hw4-frontend-instance"
  }
}

resource "aws_instance" "coe_558_hw4_backend_server" {
  ami = "ami-0281b0943230d40d1"
  instance_type = "t3.medium"
  availability_zone = var.av_zone
  subnet_id = "subnet-07856761a4ac292b1"
  key_name = aws_key_pair.coe_558_hw4_backend_server.key_name
  user_data = file("${path.module}/scripts/install_docker.sh")
  vpc_security_group_ids = [
    "sg-09a862554f50c67bc"
  ]
  tags = {
    Name = "coe-558-hw4-backend-instance"
  }
}