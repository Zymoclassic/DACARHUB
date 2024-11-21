This project is a web-based application that aspires to provide a comprehensive and effective solution for the car rental industry, combining technology, usability, and innovation to create a modern and competitive online platform. With HTML, CSS and JavaScript on the Frontend, and Django on the Backend, risk mitigation strategies, and a clear development and testing process, we aim to deliver a high-quality and reliable car rental website that allows users to browse available cars, make reservations, and manage bookings.

--------------------------------------
Features

User Features:
Browse Cars: View a list of available vehicles with details such as model, price, and availability.

Book Cars: Reserve a car for specific dates.

Manage Bookings: View and cancel existing reservations.


Admin Features:
Add/Edit Cars: Admins can add new cars or update details of existing ones.

Manage Bookings: View all reservations and manage them.

--------------------------------------
Tech Stack

Frontend:
HTML: Structure of the web application.

CSS: Styling for an attractive and responsive user interface.

JavaScript: Interactive elements like form validations and dynamic car listings.


Backend:
Django: Handles the server-side logic, database management, and APIs.

SQLite (default Django database): Stores car details, user data, and booking records.

--------------------------------------
Installation
1. Clone the repository:

git clone https://github.com/zymoclassic/dacarhub.git

cd dacarhub


2. Run the virtual environment:

virtualenv\Scripts\activate


3. Install dependencies:

pip install -r requirements.txt


4. Run database migrations:

python manage.py migrate


5. Start the development server:

python manage.py runserver


6. Open the application:
Visit http://127.0.0.1:8000 in your browser.

--------------------------------------
Usage
1. Frontend:
The user interface is built with HTML, CSS, and JavaScript for a smooth and interactive experience.


2. Backend:
Django handles user requests, processes bookings, and communicates with the database.

Admins can access a separate dashboard for car and booking management (127.0.0.1/8000/admin).

--------------------------------------
Future Improvements

Payment Gateway: Integrate online payment for bookings.

Advanced Filters: Allow users to search for cars by type, brand, or price range.

Notifications: Email notifications for booking confirmations and reminders.

--------------------------------------
License

This project is licensed under the MIT License.

--------------------------------------
Contact

For questions or feedback, feel free to reach out:
Awopeju Kolawole Moses
https://www.kolawolemawopeju.online
