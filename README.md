# person-API

![Project Logo](logo.png)

## Introduction

The HNGx person API is a RESTful web service for managing person (people, employee etc ) records. It provides endpoints for creating, retrieving, updating, and deleting "person" data. This project was developed using Django and the Django REST framework.

## Table of Contents

1. Introduction
2. Features
3. Prerequisites
4. Getting Started
   - Installation
   - Running the Application
5. Usage
6. Testing
7. API Documentation
8. Known Limitations
9. Contributing
10. License


## Features

tag: person, people, employee, group . db

- Create new person records.
- Retrieve person details by ID.
- Update existing person records.
- Delete person records.
- Comprehensive test suite for ensuring API functionality.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Virtual environment (optional but recommended).
- Git (for cloning the repository).


### Installation

1. Clone the repository to your local machine using Git:

git clone https://github.com/Khansmira/hngx_person-api.git

2. Navigate to the project directory:


3. Create a virtual environment (optional but recommended):


4. Activate the virtual environment:

- **Windows:**

  ```
  env\Scripts\activate
  ```

- **Linux/macOS:**

  ```
  source env/bin/activate
  ```

5. Install project dependencies:


### Running the Application

To run the application locally, follow these steps:

1. Apply database migrations:


2. Start the development server:


You can now access the API at `http://localhost:8000/api/people/`.


## Usage

- Use your preferred API client (e.g., Postman) to interact with the API endpoints.
- Refer to the API Documentation file for detailed information on available endpoints, request formats, and responses.

## Testing

This project includes a comprehensive test suite for ensuring the functionality of the API. To run the tests, use the following command:


python manage.py test

### Hosting the Application

Deploying to a Server (Example: Heroku, render, pythonanywhere)



## API Documentation

The API is documented in the DOCUMENTATION.md file. It provides information on available endpoints, standard request and response formats, sample usage, and more.

## Known Limitations

- The API is still undergoing tests to ascertian its capabilities to support robust systems.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to help improve this project.