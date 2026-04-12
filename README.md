# 💼 Job Salary Prediction 

A Machine Learning-powered REST API built with **FastAPI** that predicts job salaries based on employee attributes like job title, experience, education, and more.

---

## 🚀 Demo

<a href='https://jobsalaryprediction.onrender.com/'>Click here to see my project</a>

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | FastAPI (Python) |
| **ML Model** | Scikit-learn (joblib) |
| **Frontend** | HTML, CSS, JavaScript |
| **Server** | Uvicorn (ASGI) |

---

## 📁 Project Structure

```
jobsalaryprediction/
│
├── app.py          # FastAPI backend & prediction logic
├── models.pkl      # Trained ML model
├── index.html      # Frontend UI
└── README.md       # You are here!
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ramashishmaurya/jobsalaryprediction.git
cd jobsalaryprediction
```

### 2. Create Virtual Environment

```bash
python -m venv myapp
myapp\Scripts\activate        # Windows
# source myapp/bin/activate   # Mac/Linux
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn joblib pandas scikit-learn
```

### 4. Run the Server

```bash
uvicorn app:app --reload
```

Server will start at → `http://127.0.0.1:8000`

### 5. Open Frontend

Just open `index.html` in your browser — done! 🎉

---

## 📡 API Endpoints

### `GET /`
Health check — returns API status.

**Response:**
```json
{
  "message": "Salary prediction API is running"
}
```

---

### `POST /predict`
Predicts salary based on employee data.

**Request Body:**
```json
{
  "job_title": "Backend Developer",
  "experience_years": 3,
  "education_level": "Bachelor's",
  "skills_count": 5,
  "industry": "Technology",
  "company_size": "Medium",
  "location": "New York",
  "remote_work": "Yes",
  "certifications": 2
}
```

**Response:**
```json
{
  "predicted_salary": 95000.0
}
```

---

## 🧠 Model Input Features

| Feature | Type | Example |
|---|---|---|
| `job_title` | string | `Backend Developer`, `Cybersecurity Analyst` |
| `experience_years` | int | `3` |
| `education_level` | string | `Bachelor's`, `Master's`, `PhD` |
| `skills_count` | int | `5` |
| `industry` | string | `Technology`, `Finance` |
| `company_size` | string | `Small`, `Medium`, `Large` |
| `location` | string | `New York`, `San Francisco` |
| `remote_work` | string | `Yes`, `No`, `Hybrid` |
| `certifications` | int | `2` |

---

## 🌐 CORS

CORS is enabled for all origins so the frontend can communicate with the API without any issues.

---

## 📬 API Documentation

FastAPI provides auto-generated docs:

- **Swagger UI** → `http://127.0.0.1:8000/docs`
- **ReDoc** → `http://127.0.0.1:8000/redoc`

---

## 🙌 Author

Made with ❤️ by **[Ashish Maurya]**  
GitHub: [@ramashishmaurya](https://github.com/ramashishmaurya)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
