# Masterblog API 🚀

A full-stack blog application built with a **decoupled architecture** — a Flask REST API backend and a separate Flask-served JavaScript frontend that communicate via HTTP.

## Architecture

```
┌─────────────────────────┐        HTTP / JSON        ┌─────────────────────────┐
│   Frontend (Port 5001)  │  ◄──────────────────────► │   Backend (Port 5002)   │
│   Flask + HTML/CSS/JS   │                            │   Flask REST API        │
└─────────────────────────┘                            └─────────────────────────┘
```

The frontend and backend run as **independent services** and communicate through the REST API. CORS is enabled on the backend to allow cross-origin requests.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/posts` | Retrieve all posts |
| `GET` | `/api/posts?sort=title&direction=asc` | Retrieve posts sorted by `title` or `content` |
| `POST` | `/api/posts` | Create a new post |
| `PUT` | `/api/posts/<id>` | Update an existing post |
| `DELETE` | `/api/posts/<id>` | Delete a post by ID |
| `GET` | `/api/posts/search?title=...&content=...` | Search posts by title or content |

### Example Requests

**Create a post**
```bash
curl -X POST http://localhost:5002/api/posts \
  -H "Content-Type: application/json" \
  -d '{"title": "Hello World", "content": "My first post."}'
```

**Update a post**
```bash
curl -X PUT http://localhost:5002/api/posts/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Title"}'
```

**Sort posts**
```bash
curl "http://localhost:5002/api/posts?sort=title&direction=asc"
```

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)

- **Flask** — REST API backend & frontend server
- **Flask-CORS** — cross-origin resource sharing between services
- **Fetch API** — asynchronous HTTP requests from the frontend
- **In-memory storage** — posts stored as a Python list (no database required)

## Project Structure

```
Masterblog-API/
├── backend/
│   └── backend_app.py      # REST API (runs on port 5002)
└── frontend/
    ├── frontend_app.py     # Frontend server (runs on port 5001)
    ├── templates/
    │   └── index.html      # Blog UI
    └── static/
        ├── main.js         # Fetch API calls (load, add, delete posts)
        └── styles.css      # Styling
```

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/vincentkoenig/Masterblog-API.git
cd Masterblog-API
```

**2. Install dependencies**
```bash
pip install flask flask-cors
```

**3. Start the backend** (in one terminal)
```bash
cd backend
python backend_app.py
# Running on http://localhost:5002
```

**4. Start the frontend** (in a second terminal)
```bash
cd frontend
python frontend_app.py
# Running on http://localhost:5001
```

**5. Open in your browser**
```
http://localhost:5001
```

Enter `http://127.0.0.1:5002/api` as the API Base URL and click **Load Posts**.

## What I Learned

- Designing and implementing a RESTful API with full CRUD operations
- Decoupling frontend and backend into independent services
- Handling CORS with `flask-cors` to allow cross-origin communication
- Using the JavaScript Fetch API to asynchronously consume a REST API
- Implementing query parameter validation and returning proper HTTP status codes (`200`, `201`, `400`, `404`)
- Dynamically rendering and updating the DOM based on API responses
