# To-Doist

A FastAPI-based to-do list backend with JWT authentication, user management, and CRUD operations for personal tasks.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Notes](#notes)

## Overview

`to-doist` is a REST API for managing user-specific to-do items. The backend supports user registration, login, and authenticated CRUD operations on tasks. It uses PostgreSQL through SQLAlchemy and secures access with JWT bearer tokens.

## Features

- User registration with secure password hashing
- JWT authentication via OAuth2 password flow
- Create, read, update, and delete to-do items
- User-specific item isolation
- PostgreSQL database persistence

## Tech Stack

- Python 3.14+
- FastAPI
- SQLAlchemy
- PostgreSQL (`psycopg2`)
- JWT authentication (`PyJWT`)
- Secure password hashing (`pwdlib`)
- Uvicorn

## Project Structure

- `backend/main.py` - FastAPI application entrypoint
- `backend/app/api/routes/` - API router definitions
  - `items.py` - item CRUD endpoints
  - `user.py` - user registration endpoint
  - `login.py` - authentication endpoint
- `backend/app/core/` - core application modules
  - `db.py` - database connection and session management
  - `model.py` - SQLAlchemy models
  - `schema.py` - Pydantic request schemas
  - `security.py` - password hashing and JWT utilities
- `pyproject.toml` - project metadata and dependencies

## Getting Started

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd to-doist
   ```

2. Create a Python virtual environment and activate it:

   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -e .
   ```

4. Create a `.env` file in the project root with the required environment variables.

## Configuration

The application reads configuration from environment variables using `python-dotenv`.

Required variables:

- `DATABASE_URL` - SQLAlchemy database URL for PostgreSQL
- `SECRET_KEY` - secret key used to sign JWT tokens
- `ALGORITHM` - JWT signing algorithm (e.g. `HS256`)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - token lifetime in minutes

Example `.env`:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/todoist
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

## Running the Application

From the project root, run the server from the `backend` folder:

```bash
cd backend
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Endpoints

### User Registration

- `POST /api/users`
- Request body: `username`, `email`, `password`
- Creates a new user account

### Login

- `POST /login/`
- Form data: `username`, `password`
- Returns: `access_token`, `token_type`

### To-Do Items (Protected)

All `/api/items` routes require a valid Bearer token.

- `GET /api/items` - List current user items
- `POST /api/items` - Create a new item
- `GET /api/items/{item_id}` - Retrieve an item by ID
- `PUT /api/items/{item_id}` - Update an existing item
- `DELETE /api/items/{item_id}` - Delete an item

### Item Payload

```json
{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "status": "pending",
  "priority": "medium"
}
```

## Authentication

Use the returned JWT token in the `Authorization` header for protected endpoints:

```http
Authorization: Bearer <access_token>
```

## Notes

- `backend/main.py` automatically creates database tables on startup using SQLAlchemy metadata.
- The current backend repository does not include frontend views; it is designed as a REST API service.
- Add tests and deployment automation as needed.
  > > > > > > > bd7bb15 (initial commit)
