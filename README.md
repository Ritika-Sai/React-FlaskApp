React + Flask Full stack App

This project is a simple full-stack system built with React (frontend) and Flask + SQLite (backend). Users can sign up and log in, and data is stored in a local SQLite database.


📁 Project Structure

```
my-app/
├── backend/             # Flask API
│   ├── app.py
│   ├── users.db
│   └── db_setup.py
├── frontend/            # React App
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── Login.js
│       └── Signup.js
├── README.md
```


 🚀 Getting Started

1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

🔧 Backend Setup (Flask API)

1. Navigate to the `backend` directory:

```bash
cd backend
```

2. Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

3. Install required packages:

```bash
pip install flask flask-cors
```

4. Set up the database:

```bash
python db_setup.py
```

5. Run the Flask server:

```bash
python app.py
```

Flask server will start on: `http://localhost:5000`



💻 Frontend Setup (React App)

1. Open a new terminal tab/window.
2. Navigate to the `frontend` directory:

```bash
cd frontend
```

3. Install dependencies:

```bash
npm install
```

4. Start the React app:

''' bash
npm start


React app will run on: `http://localhost:3000`

🔁 How It Works

- The **React app** sends HTTP requests using `axios` to the Flask API.
- The **Flask backend** handles signup and login logic.
- Credentials are stored securely in a local **SQLite** database.

⚙️ Technologies Used

- Frontend: React, Axios
- Backend: Flask, Flask-CORS, SQLite
- Dev Tools: VSCode, Postman
