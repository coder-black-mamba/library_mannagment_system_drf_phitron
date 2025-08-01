# Library Management System

A comprehensive Library Management System built with Django that provides an efficient way to manage library operations. This system helps librarians manage books, members, and borrowing records with ease.

## Features

- **User Management**: Register and manage library members and staff
- **Book Management**: Add, update, and remove books from the library
- **Borrowing System**: Track book loans and returns
- **Search Functionality**: Quickly find books and members
- **Admin Dashboard**: Comprehensive admin interface for library staff
- **REST API**: Built with Django REST Framework for easy integration

## Tech Stack

- **Backend**: Django 5.2
- **Database**: SQLite (Development), PostgreSQL (Production-ready)
- **API**: Django REST Framework
- **Frontend**: HTML, CSS, JavaScript (with potential for frontend framework integration)

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Virtual Environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser (admin)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Frontend: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## Project Structure

```
library_management_system/
├── library_mannagment_system/  # Main project settings
├── users/                      # User management app
├── books/                      # Book management app
├── operations/                 # Library operations app
├── api/                        # API endpoints
├── manage.py                   # Django management script
└── requirements.txt            # Project dependencies
```

## API Documentation

API documentation is available at `/api/docs/` when the development server is running.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Django Documentation
- Django REST Framework
- All contributors who helped in development
