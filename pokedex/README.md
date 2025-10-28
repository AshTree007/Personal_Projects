# Pokedex Web Application

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

This project is a simple web application built with Flask, designed to retrieve and display Pokémon information using the [PokeAPI](https://pokeapi.co/).

---

## Features

*   **Search Functionality:** Users can search for Pokémon by entering their name or ID.
*   **Detailed Information Display:** The application presents comprehensive Pokémon details, including image, name, ID, height, and weight.

---

## Getting Started

### Prerequisites

*   Python 3.x

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/your-username/Personal_projects.git
    ```
2.  Navigate to the project directory:
    ```bash
    cd Personal_projects/pokedex
    ```
3.  Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

To run the Pokedex web application:

1.  **Start the Flask Server:** From the `pokedex` directory, execute the `main.py` script:
    ```bash
    python main.py
    ```
2.  **Access the Application:** Open your web browser and navigate to `http://127.0.0.1:5000`. You will be presented with the Pokedex interface where you can search for Pokémon.

---

## How it Works

*   The application leverages the `Flask` web framework to manage HTTP requests and responses.
*   Upon a user's search query, an asynchronous request is made to the official PokeAPI.
*   The JSON response from the API is then parsed, and relevant data is extracted to populate the `response.html` template, which is rendered to the user.

---

## Project Structure

```
pokedex/
├───README.md
├───main.py
├───requirements.txt
├───test.py
└───templates/
    ├───frontend.html
    └───response.html
```

---

## Technologies Used

*   Python
*   Flask
*   Requests (for API interaction)
*   HTML/CSS

---