# Real Estate IaC Project

A Flask-based real estate web application with automated infrastructure provisioning and deployment.

## Features
- Property listings with search functionality
- SQLite database
- Responsive design
- RESTful API

## Tech Stack
- **Backend:** Flask, SQLAlchemy
- **Frontend:** HTML, CSS, Jinja2
- **Database:** SQLite
- **Deployment:** Docker, Kubernetes
- **IaC:** Terraform
- **CI/CD:** GitHub Actions / Jenkins

## Local Setup

1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/real-estate-iac-project.git
cd real-estate-iac-project
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install flask flask-sqlalchemy
```

4. Add sample data
```bash
python add_sample_data.py
```

5. Run the application
```bash
python app.py
```

Visit `http://127.0.0.1:5000`

## Project Structure
```
real-estate-iac-project/
├── app.py
├── add_sample_data.py
├── templates/
├── static/
└── README.md
```

## Roadmap
- [x] Basic Flask application
- [ ] Dockerize application
- [ ] Terraform infrastructure
- [ ] Kubernetes deployment
- [ ] CI/CD pipeline
- [ ] Cloud deployment (AWS)
