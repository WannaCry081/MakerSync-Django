# MakerSync [Django]

MakerSync API facilitates the interaction between our Flutter mobile app and the circuitry involved in the process of converting PETG plastic into 3D printing filament. It offers two versions: v1, which integrates with Firebase Firestore using firebase_admin in Python, and v2, which utilizes SQLite.

## Tools Used

- [Django](https://www.djangoproject.com/)
- [Django Ninja](https://django-ninja.dev/)
- [Django Ninja-Extra](https://eadwincode.github.io/django-ninja-extra/)
- [Firebase Admin](https://github.com/firebase/firebase-admin-python)
- [Vercel (Deployment)](https://vercel.com/)

## Endpoints

You can access the MakerSync API endpoints through the provided documentation. Simply browse to [MakerSync v1 API Documentation](https://maker-sync-django.vercel.app/api/v1/docs) or [MakerSync v2 API Documentation](https://maker-sync-django.vercel.app/api/v2/docs) to get an overview of available endpoints and interact with the API.


### v1 Endpoints

MakerSync v1 utilizes Firebase as its primary database system, offering real-time updates and changes through the Firebase console website.

#### Users

- **GET** `/api/v1/machines/{machine_code}/users/`: Retrieve all users within the machine identified by a unique sensor ID.
- **POST** `/api/v1/machines/{machine_code}/users/`: Add a user to a specific machine identified by its sensor ID.
- **GET** `/api/v1/machines/{machine_code}/users/{email}`: Retrieve user information based on email within a specific machine.
- **PUT** `/api/v1/machines/{machine_code}/users/{email}`: Update user information within a specific machine based on email.
- **DELETE** `/api/v1/machines/{machine_code}/users/{email}`: Delete a specific user from the machine based on email.

#### Machine

- **GET** `/api/v1/machines/{machine_code}/sensors`: Retrieve sensor information for a specific machine based on its sensor ID.
- **POST** `/api/v1/machines`: Add a new machine to the database identified by its sensor ID.
- **PUT** `/api/v1/machines/{machine_code}/sensors`: Update all information related to a specific machine based on its sensor ID.
- **DELETE** `/api/v1/machines/{machine_code}/sensors`: Delete a machine from the database based on its sensor ID.


### v2 Endpoints

MakerSync v2 utilizes SQLite as its primary database system, offering unlimited user request and response capabilities.

#### Machine

- **POST** `/api/v2/machines`: Create a new machine entry in the database with a unique machine code.

#### Sensor

- **GET** `/api/v2/machines/{machine_code}/sensors`: Retrieve all sensors associated with a specific machine identified by its machine code.
- **POST** `/api/v2/machines/{machine_code}/sensors`: Add a new sensor to a specific machine identified by its machine code.
- **PUT** `/api/v2/machines/{machine_code}/sensors`: Update sensor information within a specific machine based on its machine code.
- **DELETE** `/api/v2/machines/{machine_code}/sensors`: Delete a specific sensor from the machine based on its machine code.

#### Notification

- **GET** `/api/v2/machines/{machine_code}/notifications`: Retrieve all notifications associated with a specific machine identified by its machine code.
- **GET** `/api/v2/machines/{machine_code}/notifications/{notification_id}`: Retrieve a specific notification by its ID within a machine identified by its machine code.
- **POST** `/api/v2/machines/{machine_code}/notifications`: Create a new notification associated with a specific machine identified by its machine code.

#### User

- **GET** `/api/v2/machines/{machine_code}/users`: Retrieve all users associated with a specific machine identified by its machine code.
- **GET** `/api/v2/machines/{machine_code}/users/{email}`: Retrieve user information based on email within a specific machine identified by its machine code.
- **POST** `/api/v2/machines/{machine_code}/users`: Add a new user to a specific machine identified by its machine code.
- **PUT** `/api/v2/machines/{machine_code}/users/{email}`: Update user information within a specific machine based on email and machine code.
- **DELETE** `/api/v2/machines/{machine_code}/users/{email}`: Delete a specific user from the machine based on email and machine code.


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

4. Migrate database:
   ```bash
   python manage.py makemigrations v2
   python manage.py migrate

   # View changes using the admin page
   python manage.py createsuperuser 
   ```

5. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

6. Access the API documentation at [MakerSync v1 API Documentation](https://maker-sync-django.vercel.app/api/v1/docs) or [MakerSync v2.0 API Documentation](https://maker-sync-django.vercel.app/api/v2/docs). 


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