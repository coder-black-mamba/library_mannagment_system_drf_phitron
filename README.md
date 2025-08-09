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

The Library Management System provides a RESTful API built with Django REST Framework. Below are the main endpoints and their usage:

### Authentication
All API endpoints require authentication. Use JWT tokens for authentication.

```http
POST /auth/jwt/create/
Content-Type: application/json

{
    "username": "your_username",
    "password": "your_password"
}
```

Include the token in subsequent requests:
```
Authorization: JWT your_token_here
```

### Available Endpoints

#### 1. Borrow a Book

**Endpoint**: `POST /api/v1/operations/borrow/`  
**Description**: Borrow a book from the library  
**Authentication**: Required  
**Request Body**:
```json
{
    "book": 1,
    "member": 1
}
```
**Response (Success - 201 Created)**:
```json
{
    "id": 1,
    "book": 1,
    "member": 1,
    "borrow_date": "2023-01-01",
    "return_date": null,
    "status": "borrowed"
}
```

#### 2. List Borrowed Books

**Endpoint**: `GET /api/v1/operations/borrow/`  
**Description**: List all borrowed books with optional filtering  
**Authentication**: Required  
**Query Parameters**:
- `member_id` (optional): Filter by member ID
- `book_id` (optional): Filter by book ID

**Example**: `GET /api/v1/operations/borrow/?member_id=1`

**Response (200 OK)**:
```json
[
    {
        "id": 1,
        "book": 1,
        "member": 1,
        "borrow_date": "2023-01-01",
        "return_date": null,
        "status": "borrowed"
    }
]
```

#### 3. Return a Book

**Endpoint**: `POST /api/v1/operations/return/<borrow_id>/`  
**Description**: Return a borrowed book  
**Authentication**: Required  
**URL Parameters**:
- `borrow_id`: ID of the borrow record

**Response (200 OK)**:
```json
{
    "message": "Book returned successfully",
    "borrow_id": 1,
    "book_id": 1,
    "return_date": "2023-01-10"
}
```

#### 4. View Borrow Record

**Endpoint**: `GET /api/v1/operations/return/<borrow_id>/`  
**Description**: Get details of a specific borrow record  
**Authentication**: Required

**Response (200 OK)**:
```json
{
    "id": 1,
    "book": 1,
    "member": 1,
    "borrow_date": "2023-01-01",
    "return_date": "2023-01-10",
    "status": "returned"
}
```

### Error Responses

#### 400 Bad Request
- Invalid input data
- Book is not available for borrowing
- Book is already returned

#### 401 Unauthorized
- Missing or invalid authentication credentials

#### 404 Not Found
- Borrow record not found
- Book or member not found

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
