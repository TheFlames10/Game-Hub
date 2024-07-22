# Game Hub

Welcome to Game Hub! This project is a web-based game hub featuring a variety of games, including Tic-Tac-Toe. It includes user authentication with login and signup pages, a profile page to track scores, and more.

## Features

- **Game Hub**: A central place to access and play different games.
- **Tic-Tac-Toe**: Play against another player or an AI (easy or hard mode).
- **User Authentication**: Sign up and log in with username and password.
- **Profile Page**: Track your all-time scores.
- **Responsive Design**: The game board and other content adjust to fit the page size.
- **Captcha Security**: Enhanced login security with Google reCAPTCHA.

## Technologies Used

- **Frontend**:
  - React
  - React Router
  - Axios
  - CSS for styling
  - Google reCAPTCHA

- **Backend**:
  - Flask
  - Flask SQLAlchemy
  - Flask CORS
  - Bcrypt for password hashing

## Installation

### Prerequisites

- Node.js and npm
- Python and pip

### Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/game-hub.git
    cd game-hub
    ```

2. **Backend Setup:**

    ```bash
    cd backend
    pip install -r requirements.txt
    ```

3. **Frontend Setup:**

    ```bash
    cd ../frontend
    npm install
    ```

### Running the Project

1. **Start the Backend:**

    ```bash
    cd backend
    python app.py
    ```

2. **Start the Frontend:**

    ```bash
    cd ../frontend
    npm start
    ```
