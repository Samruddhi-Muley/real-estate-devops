provider "aws" {
  region = "ap-south-1"
}

# -----------------------------
# Security Group
# -----------------------------
resource "aws_security_group" "app_sg" {
  name        = "devops-app-sg"
  description = "Allow SSH and Kubernetes NodePort"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "NodePort Access"
    from_port   = 30007
    to_port     = 30007
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

# -----------------------------
# EC2 Instance
# -----------------------------
resource "aws_instance" "app_server" {

  ami           = "ami-019715e0d74f695be"  # Ubuntu 22.04 (Mumbai)
  instance_type = "t3.micro"
  key_name      = "real-estate-key"

  security_groups = [aws_security_group.app_sg.name]

  user_data = <<-EOF
#!/bin/bash

# Update system
apt update -y

# Install Docker
apt install docker.io -y
systemctl enable docker
systemctl start docker

# Install K3s (Lightweight Kubernetes)
curl -sfL https://get.k3s.io | sh -

# Set kubeconfig
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

# Wait until Kubernetes is ready
until kubectl get nodes; do
  sleep 5
done

# Create Deployment + Service
cat <<EOT > /root/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: real-estate-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: real-estate
  template:
    metadata:
      labels:
        app: real-estate
    spec:
      containers:
      - name: real-estate-container
        image: samruddhi1muley/real-estate-app:latest
        ports:
        - containerPort: 5000
---
apiVersion: v1
kind: Service
metadata:
  name: real-estate-service
spec:
  type: NodePort
  selector:
    app: real-estate
  ports:
    - port: 80
      targetPort: 5000
      nodePort: 30007
EOT

# Apply Kubernetes config
kubectl apply -f /root/deployment.yaml

EOF

  tags = {
    Name = "DevOps-K8s-App"
  }
}

# -----------------------------
# Output Public IP
# -----------------------------
output "public_ip" {
  value = aws_instance.app_server.public_ip
}