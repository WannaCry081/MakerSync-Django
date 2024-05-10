# MakerSync [Django]

MakerSync API facilitates the interaction between our Flutter mobile app and the circuitry involved in the process of converting PETG plastic into 3D printing filament. It offers two versions: v1, which integrates with Firebase Firestore using firebase_admin in Python, and v2, which utilizes SQLite.

## Tools Used

- [Django](https://www.djangoproject.com/)
- [Django Ninja](https://django-ninja.dev/)
- [Django Ninja-Extra](https://eadwincode.github.io/django-ninja-extra/)
- [Firebase Admin](https://github.com/firebase/firebase-admin-python)
- [Vercel (Deployment)](https://vercel.com/)

## Endpoints

You can access the MakerSync API endpoints through the provided documentation. Simply browse to [MakerSync API Documentation](https://maker-sync-django.vercel.app/api/v1/docs) to get an overview of available endpoints and interact with the API.

### Users

- **GET** `/api/v1/machines/{machine_code}/users/`: Retrieve all users within the machine identified by a unique sensor ID.
- **POST** `/api/v1/machines/{machine_code}/users/`: Add a user to a specific machine identified by its sensor ID.
- **GET** `/api/v1/machines/{machine_code}/users/{email}`: Retrieve user information based on email within a specific machine.
- **PUT** `/api/v1/machines/{machine_code}/users/{email}`: Update user information within a specific machine based on email.
- **DELETE** `/api/v1/machines/{machine_code}/users/{email}`: Delete a specific user from the machine based on email.

### Sensors

- **GET** `/api/v1/sensors/{sensor_id}`: Retrieve sensor information for a specific machine based on its sensor ID.
- **POST** `/api/v1/sensors`: Add a new machine to the database identified by its sensor ID.
- **PUT** `/api/v1/sensors/{sensor_id}`: Update all information related to a specific machine based on its sensor ID.
- **DELETE** `/api/v1/sensors/{sensor_id}`: Delete a machine from the database based on its sensor ID.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/WannaCry081/MakerSync-Django.git
   ```

2. Navigate to the project directory:
   ```bash
   cd makersync-django
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

5. Access the API documentation at [MakerSync API Documentation](https://maker-sync-django.vercel.app/api/v1/docs).


### Additional Option

Alternatively, you can use the provided `run.sh` script to automate the setup process:

```bash
# In Windows
> run.sh [venv | pipenv]

# In Linux
$ chmod +x run.sh
$ ./run.sh
```

> [!NOTE]
>
> This script will automatically create a virtual environment, install the necessary dependencies, and run the Django API for you.

## Usage

Once the server is running, you can interact with the API using tools like cURL, Postman, or directly from your Flutter mobile app. Refer to the provided API documentation for detailed information on available endpoints and their usage.

## Contribution

Contributions to MakerSync-Django are welcome! If you have any ideas, suggestions, or improvements, feel free to open an issue or submit a pull request on the GitHub repository.