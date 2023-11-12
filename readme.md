# Farm Task App Backend

## Overview

This repository contains the Django backend for a single-page web application designed for farm management. It's tailored for a single farmer, providing the functionality to list, add, edit, and remove animals, each uniquely identified by name.

## Features

- **PostgreSQL Integration**: Integrated PostgreSQL for user data management. This change enhances the application's scalability and data persistence capabilities.
- **Simple JWT Authentication**: Implemented simple JWT-based authentication to ensure that only authenticated users can access and modify the data. This feature adds a layer of security and personalization to the application.
- **CRUD Functionality for Animals**: Alongside listing, adding, and removing animals, the application also supports editing animal data, allowing for complete data management.
- **Deployment on Heroku**: The application backend is deployed on Heroku, leveraging its powerful cloud platform for hosting.

## Local Development

To run this project locally, follow these steps:

1. **Clone the Repository**:

   - Clone this repository to your local machine.

   ```sh
    git clone https://github.com/jalilbm/farm-task-app-backend.git
    cd farm-task-app-backend
   ```

2. **Environment Variables**:

   - An `.env` file with necessary environment variables will be provided via email for connecting to the PostgreSQL database, and should be placed at the root directory (alongside `readme.md`), and make sure that it's saved as `.env` not `env`

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

## Performance Note

When running the application locally with PostgreSQL (that is hosted in Heroku), you might experience slightly slower response times compared to the production environment. This variance is typical due to the network latency in local setups. However, the publicly available interface on Netlify ensures a more responsive user experience. Keep this in mind while testing and developing locally.

## Local Development Recommended

We highly encourage using local development for both the backend and frontend of this application. This approach provides a more stable and consistent environment for data management and app functionality.

## Limitations of Deployed Version on Heroku

The version of this application deployed on Heroku has certain limitations due to how Heroku works. These limitations mainly affect how data (like the animals list) is stored and managed.

### Ephemeral Filesystem

- **What it Means**: Heroku uses an 'ephemeral' filesystem. This means that any information the app stores in memory is only temporary.
- **How it Affects the App**: When you add or remove animals on the website, these changes are stored in memory. However, because Heroku's memory is temporary, these changes get lost periodically. This reset happens at least once every day or whenever the app restarts (like after sleeping due to inactivity).
- **User Experience**: As a user, you might add some animals today and find that they're gone tomorrow. It might seem like the app is 'forgetting' the changes you've made.

### Distributed Nature

- **What it Means**: Heroku runs apps on multiple 'dynos', which are like separate little computers. Each dyno has its own separate memory.
- **How it Affects the App**: When you interact with the app, you might be talking to one dyno at one moment and a different dyno the next moment. Since each dyno doesn't share its memory with the others, they might have different lists of animals.
- **User Experience**: You might add an animal, and it appears to be saved successfully. But if your next action is handled by a different dyno, it may look like that animal was never added. It’s like each dyno has its own separate version of the animal list, leading to a confusing experience where the list seems to change unexpectedly.

## Conclusion

Due to these limitations, the Heroku-deployed version of our app might not always behave as expected, especially with adding or removing animals. For a more consistent and reliable experience, we recommend running the application locally.
