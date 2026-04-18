# AI-Powered Health Screening Platform

## Overview

AI-Powered Health Screening Platform is a full-stack web application designed to
provide AI-driven preliminary health assessments for rural and underserved
communities. The project combines a modern React frontend, a FastAPI backend,
machine learning workflows, and a PostgreSQL-ready data layer to support early
screening, accessible reporting, and future clinical workflow integrations.

The goal is to help communities with limited access to healthcare professionals
receive timely, technology-assisted screening support. This platform is meant
for preliminary guidance and workflow support, not as a replacement for
licensed medical diagnosis or emergency care.

## Features

- React frontend bootstrapped with Vite for a fast development experience
- FastAPI backend prepared for REST API development and model-serving endpoints
- Dedicated `ml_models` workspace for training scripts, experiments, and saved
  models
- Database folder reserved for PostgreSQL schema definitions and migrations
- Docker workspace for containerization and deployment-ready packaging
- Clear starter structure for scaling into authentication, screening workflows,
  image analysis, and triage recommendations

## Tech Stack

- React
- FastAPI
- PostgreSQL
- Scikit-learn
- PyTorch
- Docker

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/sam15-ai/AI-Powered-Health-Screening-Platform.git
cd AI-Powered-Health-Screening-Platform
```

### 2. Frontend setup

```bash
cd frontend
npm install
npm run dev
```

The Vite development server will start locally and serve the React app.

### 3. Backend setup

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

The FastAPI app will be available locally, typically at
`http://127.0.0.1:8000`.

### 4. Database and ML workflows

- Add PostgreSQL schema files and migration assets in `database/`
- Place training scripts, notebooks, and exported models in `ml_models/`
- Add Dockerfiles and compose assets in `docker/` as deployment requirements
  become clearer

## Folder Structure

```text
health-screening-platform/
├── frontend/         # React.js app powered by Vite
├── backend/          # FastAPI app and backend modules
├── ml_models/        # ML training scripts and saved models
├── database/         # SQL schema files
├── docker/           # Dockerfiles and container assets
├── .gitignore
└── README.md
```

### Backend starter contents

```text
backend/
├── main.py
├── requirements.txt
├── routers/
├── models/
├── schemas/
└── utils/
```

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a feature branch
3. Make your changes with clear commits
4. Open a pull request describing the update and rationale

When adding healthcare-related features, prioritize privacy, accessibility,
ethical AI usage, and clinical safety review. Any predictive output should be
treated as supportive screening guidance rather than definitive medical advice.
