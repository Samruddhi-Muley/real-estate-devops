# 🏠 Real Estate DevOps Project

A Flask-based Real Estate web application with automated infrastructure provisioning and deployment using Docker, Terraform, and AWS.

This project demonstrates modern DevOps practices including containerization, Infrastructure as Code (IaC), and cloud deployment.

---

## 🚀 Live Deployment

Application deployed on AWS EC2 using Terraform and Docker:

```
http://<your-ec2-public-ip>
```

Example:

```
http://52.66.167.176
```

---

## 📌 Features

* Property listings with detailed information
* Responsive modern UI
* SQLite database integration
* Docker containerized application
* Automated AWS infrastructure provisioning using Terraform
* Automated Docker deployment on EC2
* Infrastructure as Code (IaC) implementation

---

## 🛠️ Tech Stack

**Backend**

* Python
* Flask
* SQLAlchemy

**Frontend**

* HTML5
* CSS3
* Jinja2

**Database**

* SQLite

**DevOps & Cloud**

* Docker
* Docker Compose
* Terraform
* AWS EC2
* GitHub

**CI/CD (Ready)**

* GitHub Actions
* Docker Hub

**Orchestration (Optional / Planned)**

* Kubernetes

---

## 📂 Project Structure

```
real-estate-devops/
│
├── app.py
├── init_db.py
├── add_sample_data.py
├── requirements.txt
│
├── Dockerfile
├── docker-compose.yml
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── properties.html
│   └── property_detail.html
│
├── static/
│   └── css/
│       └── style.css
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
│
└── README.md
```

---

# ⚙️ Local Setup (Without Docker)

## 1. Clone repository

```bash
git clone https://github.com/Samruddhi-Muley/real-estate-devops.git
cd real-estate-devops
```

---

## 2. Create virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Initialize database

```bash
python add_sample_data.py
```

---

## 5. Run application

```bash
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

---

# 🐳 Docker Setup

## Build and run container

```bash
docker-compose up --build
```

Visit:

```
http://localhost:5000
```

---

## Stop container

```bash
docker-compose down
```

---

# ☁️ Terraform Setup (AWS Deployment)

Terraform automatically creates AWS infrastructure and deploys the application.

---

## Prerequisites

Install:

* Terraform
* AWS CLI
* AWS Account
* EC2 Key Pair

Verify Terraform:

```bash
terraform -version
```

Verify AWS CLI:

```bash
aws --version
```

---

## Configure AWS CLI

```bash
aws configure
```

Enter:

```
AWS Access Key ID: YOUR_ACCESS_KEY
AWS Secret Access Key: YOUR_SECRET_KEY
Default region name: ap-south-1
Default output format: json
```

---

## Deploy Infrastructure

Navigate to terraform folder:

```bash
cd terraform
```

Initialize Terraform:

```bash
terraform init
```

Preview deployment:

```bash
terraform plan
```

Deploy infrastructure:

```bash
terraform apply
```

Type:

```
yes
```

Terraform will automatically:

* Create EC2 instance
* Create Security Group
* Install Docker
* Pull Docker image
* Run Flask container

---

## Access Application

After deployment, Terraform outputs:

```
instance_public_ip = "xx.xx.xx.xx"
```

Open in browser:

```
http://<instance_public_ip>
```

Example:

```
http://52.66.167.176
```

---

## Destroy Infrastructure (to avoid AWS charges)

```bash
terraform destroy
```

Type:

```
yes
```

---

# 🧱 Infrastructure Architecture

```
Developer
   ↓
GitHub Repository
   ↓
Docker Image (Docker Hub)
   ↓
Terraform (Infrastructure as Code)
   ↓
AWS EC2 Instance
   ↓
Docker Container
   ↓
Flask Application
   ↓
User Browser
```

---

# 🔄 DevOps Workflow

```
Code → GitHub → Docker → Terraform → AWS EC2 → Live Application
```

---

# ✅ Completed Features

* [x] Flask web application
* [x] Property listings and details
* [x] Responsive UI design
* [x] SQLite database integration
* [x] Docker containerization
* [x] Terraform infrastructure provisioning
* [x] Automated AWS EC2 deployment

---

# 🚧 Planned Improvements

* [ ] Kubernetes deployment
* [ ] CI/CD pipeline automation
* [ ] Domain name integration
* [ ] Load balancer setup

---

# 🔐 Security Features

* AWS Security Groups
* SSH key authentication
* Container isolation via Docker
* Infrastructure managed via Terraform

---

# 📸 Screenshots

### Application Running on AWS EC2

![Application Screenshot](https://github.com/Samruddhi-Muley/real-estate-devops/blob/main/screenshots/Screenshot%20(268).png)

Example:

* Running website
* AWS EC2 instance
* Terraform deployment
* Docker container running

---

# 👨‍💻 Author

Samruddhi Muley
DevOps Project

---

# 📚 References

* https://docs.aws.amazon.com/
* https://developer.hashicorp.com/terraform/docs
* https://docs.docker.com/
* https://flask.palletsprojects.com/

---

# 📄 License

This project is for educational and learning purposes.
