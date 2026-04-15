# Personal DevOps API - Stage 1

A minimal, high-performance FastAPI application deployed on a Linux VPS using Nginx as a reverse proxy. This project demonstrates backend service configuration, process management with `systemd`, and web server orchestration.


## 🛠 Tech Stack
- **Language:** Python 3.x
- **Framework:** FastAPI
- **Server:** Uvicorn (ASGI)
- **Reverse Proxy:** Nginx
- **Process Manager:** Systemd
- **Infrastructure:** Linux VPS

## 📌 API Endpoints

| Endpoint | Method | Description | Expected Response |
| :--- | :--- | :--- | :--- |
| `/` | `GET` | Root status check | `{"message": "API is running"}` |
| `/health` | `GET` | Service health check | `{"message": "healthy"}` |
| `/me` | `GET` | Developer information | `{"name": "...", "email": "...", "github": "..."}` |

> **Note:** All responses are returned in `application/json` format with a `200 OK` status code and a response time under 500ms.

## ⚙️ Local Setup & Installation

If you want to run this project locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Oluwatise-Ajayi/me_devops_api.git](https://github.com/Oluwatise-Ajayi/me_devops_api.git)
   cd me_devops_api