# iceCream_parlour
A simple Python application for an ice cream parlor cafe using Flask, SQLite, and Docker. 
# Ice Cream Parlor Cafe Application

## Overview
This application manages:
- Seasonal flavor offerings
- Ingredient inventory
- Customer flavor suggestions and allergy concerns

## Features
- Maintain a cart of favorite products
- Search & filter the offerings
- Add allergens

## Installation and Running the Application

### Using Virtual Environment
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd ice_cream_parlor
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Initialize the database:
    ```sh
    python run.py
    ```

### Using Docker
1. Build the Docker image:
    ```sh
    docker build -t ice_cream_parlor .
    ```

2. Run the Docker container:
    ```sh
    docker run -p 5000:80 ice_cream_parlor
    ```
