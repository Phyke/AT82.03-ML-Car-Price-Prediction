# AT82.03 Machine Learning
## A1: Car Price Prediction

- Name: Prombot Cherdchoo
- Student ID: st125923

### Deriverables
- `Prombot_st125923_A1.ipynb` - Jupyter Notebook with all the processes (This is the same file as on TEAL)
- `Prombot_st125923_A1.pdf` - PDF version of Jupyter Notebook generated via `nbconvert` (This is the same file as on TEAL)
- `app/` - Folder containing the app with `docker-compose.yml`
  - `app/backend/` - Folder containing FastAPI backend server with `Dockerfile`
  - `app/frontend/` - Folder containing Sveltekit frontend server with `Dockerfile`
  - `app/nginx/` - Folder containing Nginx config file with `Dockerfile`

### How to run
1. Build Docker Compose Stack
```bash
cd app
docker compose up --build
```

2. Go to `http://localhost:8080`

### Technology Stack
- Frontend: Sveltekit
- Backend: FastAPI
- Deployment: Docker, Nginx
