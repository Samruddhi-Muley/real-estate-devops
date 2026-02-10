# Real Estate DevOps Project

A Flask-based real estate web application with automated infrastructure provisioning and deployment using IaC tools.

##  Features
- Property listings with detailed information
- Responsive design with modern UI
- SQLite database
- Dockerized application
- Infrastructure as Code (IaC) deployment

##  Tech Stack
- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML5, CSS3, Jinja2
- **Database:** SQLite
- **Containerization:** Docker, Docker Compose
- **IaC:** Terraform (planned)
- **Orchestration:** Kubernetes (planned)
- **CI/CD:** GitHub Actions / Jenkins (planned)

##  Prerequisites
- Python 3.11+
- Docker & Docker Compose
- Git

## ️ Local Setup (Without Docker)

1. **Clone the repository**
```bash
git clone https://github.com/Samruddhi-Muley/real-estate-devops.git
cd real-estate-devops
```

2. **Create virtual environment**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Initialize database with sample data**
```bash
python add_sample_data.py
```

5. **Run the application**
```bash
python app.py
```

6. **Visit** `http://127.0.0.1:5000`

##  Docker Setup

1. **Build and run with Docker Compose**
```bash
docker-compose up --build
```

2. **Visit** `http://localhost:5000`

3. **Stop the application**
```bash
docker-compose down
```

##  Project Structure
```
real-estate-devops/
├── app.py                    # Main Flask application
├── init_db.py               # Database initialization script
├── add_sample_data.py       # Sample data script
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose configuration
├── templates/              # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── properties.html
│   └── property_detail.html
├── static/                 # Static files (CSS, images)
│   └── css/
│       └── style.css
└── README.md
```

##  Roadmap
- [x] Basic Flask application
- [x] Property listings and details
- [x] Responsive UI design
- [x] Docker containerization
- [ ] Terraform infrastructure provisioning
- [ ] Kubernetes deployment
- [ ] CI/CD pipeline with GitHub Actions
- [ ] AWS deployment
- [ ] PostgreSQL integration
- [ ] Monitoring and logging

##  License
MIT

##  Author
Samruddhi Muley