# Farm Task App Backend

## Overview

This repository hosts the backend of a farm management web application, designed for use by a single farmer. It facilitates listing, adding, and removing animals, each uniquely identified by name.

## Key Features

- **Intentional `.env` Inclusion**: The `.env` file is included in this repository purposefully as this project is a test.
- **Extended JWT Lifetime**: Due to Heroku's ephemeral filesystem not saving `db.sqlite3` (treated as a static file), the JWT `ACCESS_TOKEN_LIFETIME` and `REFRESH_TOKEN_LIFETIME` have been extended from deployment until testing.
- **Simple Authentication**: Added simple authentication using SIMPLE-JWT, which wasn't included in the original task, to enhance the application.
- **Animals Data Updating**: Beyond the initial requirements, the feature to update (edit) animal data has been added for dynamic data management.
- **Custom CSS and Tailwind**: Opted not to use UI frameworks like Ant Design or Material UI. Instead, demonstrated skills in Tailwind and custom CSS.
- **Deployment**: Deployed the application on Heroku.

## Testing the Application

- **Local Testing**: Create a superuser for local testing due to the authentication requirement. Only authenticated users (the farmer) can access the data.
- **Deployed Version**: For testing the deployed version, no need to create a superuser. Username and password for testing will be provided via email.

## Note

- If requested, I would have included tests in the project to ensure functionality and reliability.
