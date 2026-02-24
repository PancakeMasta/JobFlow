# JobFlow - Personal Job Application Tracker

## Summary

An app for organizing and keeping track of job applications - where a person sent applications, their status, notes and statistics

## Tech Stack

- Python3
- FastAPI
- PostgreSQL (Docker)
- SQLAlchemy
- Docker Compose

## Usage

### 1. Clone the repo

```
git clone https://github.com/PancakeMasta/JobFlow.git
cd JobFlow
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Start DB

```
docker compose up -d
```

### 5. Run backend

```
uvicorn app.main:app --reload
```
