provider "aws" {
  region = "ap-south-1"
}

#security_groups
resource "aws_security_group" "app_sg" {
  name        = "devops-app-sg"
  description = "Allow SSH and HTTP"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}


# EC2 Instance
resource "aws_instance" "app_server" {
  ami           = "ami-0317b0f0a0144b137"
  instance_type = "t3.micro"
  key_name      = "real-estate-key"

  security_groups = [aws_security_group.app_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install docker.io -y
              sudo systemctl start docker
              sudo systemctl enable docker
              sudo docker pull samruddhi1muley/real-estate-app:latest
              sudo docker run -d -p 80:5000 samruddhi1muley/real-estate-app:latest
              EOF

  tags = {
    Name = "DevOps-Flask-App"
  }
}
