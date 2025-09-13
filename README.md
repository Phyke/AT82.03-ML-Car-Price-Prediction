# AT82.03 Machine Learning
## A1 & A2: Car Price Prediction
Note: I used the same repo from A1 to build A2

- Name: Prombot Cherdchoo
- Student ID: st125923

### Deriverables
- `Prombot_st125923_A1.ipynb` - Jupyter Notebook with all the processes in A1 (This is the same file as on TEAL)
- `Prombot_st125923_A1.pdf` - PDF version of Jupyter Notebook generated via `nbconvert` (This is the same file as on TEAL)
- `Prombot_st125923_A2.ipynb` - Jupyter Notebook with all the processes in A2 (This is the same file as on TEAL)
- `Prombot_st125923_A2.pdf` - PDF version of Jupyter Notebook generated via `nbconvert` (This is the same file as on TEAL)
- `app/` - Folder containing the app with all docker compose files and source code
  - `app/docker-compose.yml` - Docker Compose file for A2 for local deployment
  - `app/docker-compose-test.yml` - Docker Compose file for A2 for testing image from DockerHub
  - `app/docker-compose-deploy.yml` - Docker Compose file for A2 for production deployment on ML Brain Server
  - `app/backend/` - Folder containing FastAPI backend server with `Dockerfile`
  - `app/frontend/` - Folder containing Sveltekit frontend server with `Dockerfile`
  - `app/docker-compose-a1.yml` - Docker Compose file for A1 (not used in A2)
  - `app/nginx/` - Folder containing Nginx config file with `Dockerfile` (This is used in A1, but not in A2)

### How to run
1. Build Docker Compose Stack
```bash
cd app
docker compose up --build
```

2. Go to `http://localhost`

### Technology Stack
- Frontend: Sveltekit
- Backend: FastAPI
- Deployment: Docker
