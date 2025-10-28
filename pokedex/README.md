# Pokedex

This is a simple web application built with Flask that allows you to look up information about Pokémon using the [PokeAPI](https://pokeapi.co/).

## Features

*   **Search for Pokémon:** Enter the name or ID of a Pokémon to retrieve its information.
*   **View Pokémon Details:** The application displays the Pokémon's image, name, ID, height, and weight.

## Setup

1.  **Install Dependencies:** Install the required Python libraries using the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application:** To start the Flask server, run the `main.py` script:
    ```bash
    python main.py
    ```

3.  **Open in Browser:** Open your web browser and navigate to `http://127.0.0.1:5000` to use the Pokedex.

## How it Works

*   The application uses the `Flask` web framework to handle requests.
*   When you submit a Pokémon name or ID, the application makes a request to the PokeAPI.
*   The JSON response from the API is then parsed to extract the relevant information, which is displayed on the `response.html` template.

## Files

*   `main.py`: The main Flask application file.
*   `requirements.txt`: A list of the required Python libraries.
*   `templates/frontend.html`: The main page of the application with the search form.
*   `templates/response.html`: The page that displays the Pokémon information.
