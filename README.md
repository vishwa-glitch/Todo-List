# To-Do List App

A simple and intuitive To-Do list application built with Django, designed to help users efficiently manage their tasks. Whether it's for work, study, or personal projects, this app allows users to keep track of their to-dos, prioritize tasks, and stay organized.

## Features

- **Task Management:** Easily add, edit, and delete tasks as your to-do list evolves.
- **Task Status:** Mark tasks as completed or pending to track progress.
- **User Authentication:** A secure login and registration system manages personal tasks.
- **Responsive Design:** A simple and clean interface built with Bootstrap, ensuring usability on all devices.

## Technologies Used

- **Backend:** Django (Python web framework)
- **Database:** SQLite (default setup, suitable for local development)
- **Frontend:** HTML, CSS, Bootstrap
- **Authentication:** Django’s built-in authentication system

---

## Local Deployment Instructions

Follow these steps to set up and run the app locally:

### Prerequisites
- **Python 3.8+** installed on your system.
- **Git** installed for cloning the repository.
- A virtual environment manager like `venv` or `virtualenv` (optional but recommended).

---

### Steps to Run Locally

1. **Clone the Repository**  
   Open your terminal and clone the repository:
   ```bash
   git clone https://github.com/vishwa-glitch/Todo-List
   ```

3. **Create a Virtual Environment (Optional)**  
   It's recommended to use a virtual environment to isolate dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate      # On Linux/Mac
   venv\Scripts\activate         # On Windows
   ```

4. **Install Dependencies**
   Install the required packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Database Migrations**
   Initialize the database by running the migrations:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**
   Start the server locally:
   ```bash
   python manage.py runserver
   ```

7. **Access the App**
   Open your web browser and go to:
   ```
   http://127.0.0.1:8000
   ```

---

## Future Enhancements

- **Push Notifications:** Implement task reminders and deadline notifications.
- **Dark Mode:** Add a dark mode option for a better user experience in low-light environments.
- **Task Filters:** Provide more advanced task sorting and filtering options (e.g., by priority).
- **Priority Levels:** Allow users to categorize tasks by priority (high, medium, low).

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
