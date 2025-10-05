# AT82.03 Machine Learning
## A1 & A2 & A3: Car Price Prediction

- Name: Prombot Cherdchoo
- Student ID: st125923

### Note:
- I used the same repo from A1 to build A2, and then A3, so some parts of the app might overlap a bit for the docker compose files.

#### A1
  - the app uses Nginx as a reverse proxy to serve the frontend and backend.
  - Deriverables for A1:
    - `Prombot_st125923_A1.ipynb` - Jupyter Notebook with all the processes in A1 (This is the same file as on TEAL)
    - `Prombot_st125923_A1.pdf` - PDF version of Jupyter Notebook generated via `nbconvert` (This is the same file as on TEAL)

#### A2
  - the app is deployed manually on the ML Brain server.
  - Nginx is not used in A2 but the docker compose file is still in the repo for reference.
  - the app is deployed on `http://st125923.ml.brain.cs.ait.ac.th`
  - Deriverables for A2:
    - `Prombot_st125923_A2.ipynb` - Jupyter Notebook with all the processes in A2 (This is the same file as on TEAL)
    - `Prombot_st125923_A2.pdf` - PDF version of Jupyter Notebook generated via `nbconvert` (This is the same file as on TEAL)

#### A3
  - CI/CD is implemented using GitHub Actions.
  - the app is automatically deployed on the ML Brain server when a new tag is pushed to the repo.
  - Deriverables for A3:
    - `Prombot_st125923_A3.ipynb` - Jupyter Notebook with all the processes in A3 (This is the same file as on TEAL)
    - `Prombot_st125923_A3.pdf` - PDF version of Jupyter Notebook generated via `nbconvert` (This is the same file as on TEAL)
    - `.github/workflows/deploy.yml` - GitHub Actions workflow file for CI/CD

### App Structure
- `app/` - Folder containing the app with all docker compose files and source code
  - `app/docker-compose.yml` - Docker Compose file for A2, A3 for local deployment
  - `app/docker-compose-test.yml` - Docker Compose file for A2 for testing image from DockerHub
  - `app/docker-compose-deploy.yml` - Docker Compose file for A2, A3 for production deployment on ML Brain Server
  - `app/docker-compose-a1.yml` - Docker Compose file for A1 (not used in A2, A3)
  - `app/backend/` - Folder containing FastAPI backend server with `Dockerfile`
  - `app/frontend/` - Folder containing Sveltekit frontend server with `Dockerfile`
  - `app/nginx/` - Folder containing Nginx config file with `Dockerfile` (This is used in A1, but not in A2, A3)

### How to run locally
As I implemented all the A1, A2, A3 in the same repo, the last version is gonna be the A3 version but I make 3 separated pages and API endpoints which don't interfere with each other, so feel free to run docker compose normally to build and grade.
1. Build Docker Compose Stack
```bash
cd app
docker compose up --build
```
2. go to `http://localhost`

### App API
#### Frontend
- `GET /` - Serve the main HTML page with 3 buttons to select models
- `GET /model1` - Serve the HTML page for Model from A1 (Random Forest Regressor)
- `GET /model2` - Serve the HTML page for Model from A2 (Linear Regression From Scratch)
- `GET /model3` - Serve the HTML page for Model from A3 (Logistic Regression From Scratch)
#### Backend
- Designed to handle requests from the frontend and return predictions
- `POST /predict/a1` - Predict car price using Model from A1 (Random Forest Regressor)
- `POST /predict/a2` - Predict car price using Model from A2 (Linear Regression From Scratch)
- `POST /predict/a3` - Predict car price using Model from A3 (Logistic Regression From Scratch)



### Technology Stack
- Frontend: Sveltekit
- Backend: FastAPI
- Deployment: Docker

