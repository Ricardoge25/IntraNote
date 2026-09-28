# IntraNote

IntraNote is a web-based incident and operational note management system developed as a university graduation project for Comware S.A.

The application was designed to centralize incident management and operational information in a single web platform.

## Overview

IntraNote was developed using Django with a modular application structure focused on incident management, operational notes, and user registration.

The project includes user authentication, role-based access control, incident management, and operational note management.

## Features

- User registration and authentication
- Role-based access control
- Incident management
- Operational note management
- Structured information management
- Administrative functionality
- Static file configuration for deployment

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** PostgreSQL
- **Deployment:** Render
- **Version Control:** Git, GitHub

## Project Structure

```text
IntraNote/
├── core/
├── incidents/
├── notes/
├── registration/
├── staticfiles/
├── xmen/
├── manage.py
├── requirements.txt
└── full_data.json
```

### Main Applications

- **core:** Core application functionality.
- **incidents:** Incident management functionality.
- **notes:** Operational notes management.
- **registration:** User registration and authentication.
- **xmen:** Main Django project configuration.

## Getting Started

### Prerequisites

- Python 3.x
- pip
- PostgreSQL
- Git

### Installation

Clone the repository:

```bash
git clone https://github.com/Ricardoge25/IntraNote.git
cd IntraNote
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

### Database Setup

Apply the Django migrations:

```bash
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Academic Context

IntraNote was developed as a university graduation project for Comware S.A.

The project was designed around an operational environment involving incident management and internal information workflows.

## Project Status

This project was developed as an academic project and is currently maintained as a portfolio project.

## Author

**Ricardo González**

Software Engineer | Python Backend & Full Stack Developer

- GitHub: https://github.com/Ricardoge25
- LinkedIn: https://www.linkedin.com/in/ricardogonzalez-dev/
