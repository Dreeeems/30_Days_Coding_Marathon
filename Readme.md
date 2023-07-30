# Movie API Web App

![Movie Icon](./client/src/assets/img/movie.jpg)

## Introduction

Welcome to the Movie API Web App! This web application allows you to search for movies and retrieve movie details using a simple and user-friendly interface. The app is built with React on the client-side and Flask on the server-side, providing a seamless and responsive experience.

## Features

- Search for movies by their names
- Display movie details and information
- Built with React and Flask for a powerful and efficient combination
- Beautifully designed user interface for an enjoyable experience

## How to Use

1. **Search for Movies**: Enter the name of the movie you want to search for in the search bar and press Enter. The app will display a list of movies that match your search query.

To run the Movie API Web App on your local machine, follow these steps:

1. Clone the Repository: Start by cloning this repository to your local machine using Git.

```bash
git clone https://github.com/your_username/movie-api-app.git

2. Install Dependencies:

a. Client-side (React):
Navigate to the client folder and install the required dependencies.
cd movie-api-app/client
npm install

b. Server-side (Flask):
Navigate to the server folder and create a virtual environment (optional but recommended).
cd ../server
python -m venv venv
# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

Install the required dependencies.
pip install -r requirements.txt

3.Set Environment Variables:

Create a .env file in the server folder and add the following:
API_KEY=your_tmdb_api_key_here
Replace your_tmdb_api_key_here with your actual TMDB API key.

4.Run the App:

a. Client-side (React):
In the client folder, start the React development server.
npm start

b. Server-side (Flask):
In the server folder, start the Flask server.
python app.py

5.Access the App:

Open your web browser and navigate to http://localhost:3000/ to access the Movie API Web App.
Technologies Used
React
Flask
TMDB API
Axios for API calls

Feedback and Support
We hope you enjoy using our Movie API Web App! If you have any feedback, questions, or need support, please feel free to contact us or raise an issue in the GitHub repository.

🎥 🍿 Happy movie searching! 🍿 🎥

```
