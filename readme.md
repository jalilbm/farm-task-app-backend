# Farm Task App Backend

## Overview

This repository contains the Django backend for a single-page web application designed for farm management. It's tailored for a single farmer, providing the functionality to list, add, edit, and remove animals, each uniquely identified by name.

## Features

- **PostgreSQL Integration**: Integrated PostgreSQL for user data management. This change enhances the application's scalability and data persistence capabilities.
- **Simple JWT Authentication**: Implemented simple JWT-based authentication to ensure that only authenticated users can access and modify the data. This feature adds a layer of security and personalization to the application.
- **CRUD Functionality for Animals**: Alongside listing, adding, and removing animals, the application also supports editing animal data, allowing for complete data management.
- **Tailwind CSS**: Demonstrated proficiency in frontend design using Tailwind CSS, avoiding the use of UI frameworks like Ant Design or Material UI. This approach showcases custom styling skills.
- **Deployment on Heroku**: The application backend is deployed on Heroku, leveraging its powerful cloud platform for hosting.

## Local Development

To run this project locally, follow these steps:

1. **Clone the Repository**:

   - Clone this repository to your local machine.

2. **Environment Variables**:

   - An `.env` file with necessary environment variables will be provided via email for connecting to the PostgreSQL database, and should be placed at the root directory (alongside `readme.md`).

3. **Install Dependencies**:

   - Install the required Python packages using `pip install -r requirements.txt`.

4. **Start the Development Server**:

   - Run the Django development server using `python manage.py runserver`.

5. **Access the Application**:
   - The application should be available at `http://localhost:8000`.

## Testing

- **Authentication Details**: For testing purposes, authentication credentials will be supplied via email.

## Note

- The application has been developed with a focus on functionality and demonstration of technical skills. Test cases can be written and included upon request to ensure the reliability and robustness of the application.
