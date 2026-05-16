# COE 558 Calculator App - Homework 4

This project is a simple cloud-hosted calculator web application developed for the COE 558 homework. It demonstrates a frontend web page communicating with a backend RESTful API deployed on separate Amazon EC2 instances.

The application supports the four basic arithmetic operations:

- Addition
- Subtraction
- Multiplication
- Division

The calculation is performed by the backend API only. The frontend does not calculate the result locally; it sends the user input to the backend and displays the API response.

---

## Architecture Overview

The project uses two EC2 instances:

| Component | Domain | Purpose |
|---|---|---|
| Frontend | `https://www.coe558calculatorappalem.com` | Hosts the calculator web page |
| Backend API | `https://api.coe558calculatorappalem.com` | Hosts the RESTful calculator API |

---

## Technologies Used

### Frontend

- HTML
- JavaScript
- Bootstrap 5
- Python static file server container
- Traefik reverse proxy
- Let's Encrypt TLS certificate

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- Docker
- Docker Compose
- Traefik reverse proxy
- Let's Encrypt TLS certificate

### Cloud Provider

- AWS

---

## DNS Configuration

Used CloudFlare for domain management, and created two records which are:

```text
www.coe558calculatorappalem.com  -> Frontend EC2 public IP
api.coe558calculatorappalem.com  -> Backend EC2 public IP
```

---

# Running the project

First make sure that your instance IP matches the resolved IP in your DNS record so that LetsEncrypt certbot can auto generate the TLS certificate.
Clone the repository, and run the following:

For backend:
```bash
cd backend
docker compose up -d
```

For frontend:
```bash
cd frontend
docker compose up -d
```

# API Docs

Visit [api.coe558calculatorappalem.com/docs](api.coe558calculatorappalem.com/docs) to view swagger UI for API docs

# Postman collection

To make testing easier, a postman collection is added and can be found in `postman_collection.json`
