<!--
# 🎓 EduShare

> A web-based educational resource-sharing platform built with Python and Django that allows students to upload, discover, bookmark, rate, review, and manage academic resources.

---

# 📌 Project Overview

EduShare is an educational resource-sharing platform designed to help students easily share and access academic study materials.

Users can upload study materials such as PDFs, documents, presentations, spreadsheets, images, videos, and ZIP files. Other users can search and filter resources, view and download materials, bookmark useful resources, and provide ratings and reviews.

The application provides user authentication, resource management, search and filtering, bookmarks, ratings and reviews, dashboard, profile management, and an administrative panel.

The project is developed using Python and Django with a responsive frontend using HTML, CSS, and JavaScript.

---

# 🎯 Objectives

- Provide a centralized platform for sharing educational resources.
- Allow students to upload and access study materials.
- Make resources easy to search and filter.
- Allow users to bookmark useful resources.
- Provide ratings and reviews for educational materials.
- Allow users to manage their own uploaded resources.
- Provide a personalized dashboard and profile.
- Implement secure user authentication.
- Demonstrate practical Django web development.
- Implement database relationships and CRUD operations.
- Practice Git and GitHub version control.

---

# 🔐 Authentication

EduShare uses Django's built-in authentication system.

Features:

- User registration
- User login
- User logout
- Password authentication
- Session-based authentication
- Automatic login after registration
- Login protection for authenticated features

Authenticated users can:

- Upload resources
- Bookmark resources
- Rate resources
- Write reviews
- Edit resources
- Delete resources
- View dashboard
- View profile

---

# 📚 Resource Management

Users can:

- Upload educational resources
- View resources
- Download resources
- Edit their own resources
- Delete their own resources
- View resource details

Each resource contains:

- Title
- Description
- Subject
- Semester
- Resource type
- Resource file
- Uploaded user
- Upload date

Users can only edit and delete resources uploaded by themselves.

---

# 🔎 Search

Users can search resources by:

- Title
- Subject
- Description

Example:

Search: Python

The application displays resources matching the search query.

---

# 🎯 Filtering

Resources can be filtered by:

## Semester

- 1st Semester
- 2nd Semester
- 3rd Semester
- 4th Semester
- 5th Semester
- 6th Semester
- 7th Semester
- 8th Semester

## Resource Type

- PDF
- Document
- Presentation
- Spreadsheet
- Image
- Video
- Archive
- Other

Search and filtering can be used together.

---

# 📄 Supported Files

EduShare supports:

## Documents

- PDF
- DOC
- DOCX

## Presentations

- PPT
- PPTX

## Spreadsheets

- XLS
- XLSX

## Images

- JPG
- JPEG
- PNG
- GIF
- WEBP

## Videos

- MP4
- WEBM
- MOV

## Archives

- ZIP

### Maximum Upload Size

100 MB

---

# 🔖 Bookmarks

Users can save useful educational resources.

Features:

- Add bookmark
- Remove bookmark
- View bookmarked resources
- Access bookmarks from navigation
- Access bookmarks from dashboard

A user cannot bookmark the same resource multiple times.

---

# ⭐ Ratings & Reviews

Users can rate resources from 1 to 5 stars.

1 ⭐
2 ⭐⭐
3 ⭐⭐⭐
4 ⭐⭐⭐⭐
5 ⭐⭐⭐⭐⭐

Users can:

- Submit ratings
- View average rating
- Write reviews
- View reviews
- Delete their own reviews

Each user can submit one review for a particular resource.

---

# 📊 Dashboard

The dashboard provides an overview of the user's uploaded resources.

Features:

- Welcome section
- Total uploads
- Uploaded resources
- View resource
- Edit resource
- Delete resource

---

# 👤 Profile

The profile page displays:

- Username
- Email
- Account creation date
- Last login
- Total uploads
- Total bookmarks
- Total reviews

The profile also provides access to:

- Dashboard
- Bookmarks
- Materials

---

# 🏠 Homepage

The homepage contains:

- Modern hero section
- Educational illustration
- Platform introduction
- Total resources count
- Total users count
- Total reviews count
- Latest uploaded resources
- Feature highlights
- Call-to-action section
- Responsive design

---

# ⚙️ Admin Panel

EduShare uses Django's built-in Admin Panel.

Administrators can manage:

- Users
- Materials
- Bookmarks
- Reviews

Admin features include:

- Search
- Filtering
- Sorting
- Resource management
- Review management

Admin URL:

http://127.0.0.1:8000/admin/

---

# ❌ Error Pages

EduShare includes custom error pages.

## 404 - Page Not Found

404.html

## 500 - Server Error

500.html

---

# 🛠️ Tech Stack

## Frontend

- HTML5
- CSS3
- JavaScript
- Responsive Web Design

## Backend

- Python
- Django

## Database

- SQLite

## Authentication

- Django Authentication System
- Session-based Authentication

## Version Control

- Git
- GitHub

## Development Tools

- Visual Studio Code
- Python Virtual Environment

---

# 🏗️ Architecture

EduShare follows the Django MVT architecture.

Browser
   |
   v
Django URLs
   |
   +-----------------------------+
   |             |               |
   v             v               v
Accounts     Materials          Core
   |             |               |
   v             v               v
Authentication Resources      Home
              Bookmarks       Dashboard
              Reviews         Profile
                    |
                    v
                Django ORM
                    |
                    v
                  SQLite

---

# 🧩 Django Apps

## 1. Accounts

Responsible for:

- Registration
- Login
- Logout
- User authentication

Main files:

accounts/
├── forms.py
├── urls.py
└── views.py

---

## 2. Materials

Responsible for:

- Resource upload
- Resource listing
- Resource details
- Search
- Filtering
- Editing
- Deleting
- Bookmarks
- Ratings
- Reviews

Main files:

materials/
├── models.py
├── forms.py
├── views.py
├── urls.py
└── admin.py

---

## 3. Core

Responsible for:

- Homepage
- Dashboard
- Profile
- Bookmarks
- Custom error pages

Main files:

core/
├── views.py
└── urls.py

---

# 📂 Project Structure

EduShare/
│
├── accounts/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── accounts/
│   │       ├── login.html
│   │       └── register.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── core/
│   ├── migrations/
│   │   └── __init__.py
│   ├── static/
│   │   └── core/
│   │       └── images/
│   │           └── hero-education.png
│   ├── templates/
│   │   ├── 404.html
│   │   ├── 500.html
│   │   └── core/
│   │       ├── bookmarks.html
│   │       ├── dashboard.html
│   │       ├── home.html
│   │       └── profile.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── materials/
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_bookmark.py
│   │   ├── 0003_alter_bookmark_material.py
│   │   ├── 0004_review.py
│   │   └── __init__.py
│   ├── templates/
│   │   └── materials/
│   │       ├── delete_material.html
│   │       ├── edit_material.html
│   │       ├── material_detail.html
│   │       ├── material_list.html
│   │       └── upload.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── edushare/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
├── .gitignore
└── README.md

---

# 🗄️ Database

EduShare uses SQLite as the development database.

The application uses Django's built-in User model and three main custom models:

- Material
- Bookmark
- Review

Database relationship:

User
 |
 +---------- Material
 |
 +---------- Bookmark
 |
 +---------- Review

---

# 🧱 Database Models

## User Model

EduShare uses Django's built-in User model.

Important fields:

- id
- username
- email
- password
- date_joined
- last_login

Relationship:

User 1 -------- * Material

---

## Material Model

Stores educational resources.

Fields:

- id
- title
- description
- subject
- semester
- resource_type
- resource_file
- uploaded_by
- uploaded_at

Relationship:

User 1 -------- * Material

---

## Bookmark Model

Stores bookmarked resources.

Fields:

- id
- user
- material
- created_at

Relationship:

User 1 -------- * Bookmark

A unique constraint prevents duplicate bookmarks.

---

## Review Model

Stores ratings and reviews.

Fields:

- id
- user
- material
- rating
- comment
- created_at

Relationship:

User 1 -------- * Review

A unique constraint prevents a user from reviewing the same resource multiple times.

---

# 🔗 Database Relationships

User
 |
 +---------------- Material
 |
 +---------------- Bookmark
 |                      |
 |                      +---- Material
 |
 +---------------- Review
                        |
                        +---- Material

---

# 🔄 Workflow

User
 |
 v
Register / Login
 |
 v
Homepage
 |
 +--------------------+
 |                    |
 v                    v
Browse Resources    Upload Resource
 |                    |
 +-- Search            +-- Add Details
 |                    +-- Select Semester
 +-- Filter            +-- Select Type
 |                    +-- Upload File
 v
Resource Details
 |
 +------------+------------+
 |            |            |
 v            v            v
Bookmark     Rating       Review
 |
 v
Dashboard
 |
 v
Profile

---

# 🔐 Security

EduShare uses Django's built-in security features.

Security includes:

- Password hashing
- Django authentication
- Session management
- CSRF protection
- Login-required views
- User ownership validation
- Environment variables
- .gitignore
- Secret key protection

The Django secret key is stored in an environment variable.

---

# 📁 Environment Variables

Create a .env file in the project root.

Example:

DJANGO_SECRET_KEY=your-secret-key

The .env file is excluded from Git.

Never upload the actual secret key to GitHub.

---

# ⚙️ Installation & Setup

## 1. Clone Repository

git clone https://github.com/PrashanthShankar024/EduShare.git

## 2. Navigate to Project

cd EduShare

## 3. Create Virtual Environment

python -m venv .venv

## 4. Activate Virtual Environment

Windows PowerShell:

.venv\Scripts\Activate.ps1

## 5. Install Dependencies

pip install django python-dotenv

## 6. Create .env

Create:

.env

Add:

DJANGO_SECRET_KEY=your-secret-key

## 7. Apply Migrations

python manage.py migrate

## 8. Create Superuser

python manage.py createsuperuser

## 9. Check Project

python manage.py check

## 10. Run Server

python manage.py runserver

## 11. Open Application

http://127.0.0.1:8000/

---

# 🔑 Admin Setup

Create a superuser:

python manage.py createsuperuser

Then open:

http://127.0.0.1:8000/admin/

Login using the superuser credentials.

---

# 🧪 Testing

Run Django system checks:

python manage.py check

Run the development server:

python manage.py runserver

Test the following:

## Authentication

- Registration
- Login
- Logout

## Resources

- Upload
- View
- Download
- Search
- Filtering
- Edit
- Delete

## Bookmarks

- Add bookmark
- Remove bookmark
- View bookmarks

## Ratings & Reviews

- Add rating
- Add review
- View reviews
- Delete own review

## User Features

- Dashboard
- Profile

## Admin

- User management
- Material management
- Bookmark management
- Review management

---

# 📸 Screenshots

Recommended screenshots:

screenshots/
├── home.png
├── login.png
├── register.png
├── materials.png
├── material-detail.png
├── upload.png
├── dashboard.png
├── bookmarks.png
├── profile.png
└── admin.png

Screenshots can be added to the README after creating the screenshots folder.

---

# 📦 File Upload Configuration

Maximum file upload size:

100 MB

Resource categories:

- PDF
- Document
- Presentation
- Spreadsheet
- Image
- Video
- Archive
- Other

Uploaded resources are stored using Django's media configuration during development.

---

# 📈 Future Improvements

## Django REST Framework

Develop REST APIs for:

- Users
- Materials
- Bookmarks
- Reviews

## Pagination

Add pagination to resource listings.

## Advanced Search

Add:

- Multiple filters
- Tags
- Categories
- Date range
- Ratings
- Subjects
- Semesters

## Tags and Categories

Add resource tags such as:

- Python
- Django
- Java
- Database
- Machine Learning
- Cloud Computing
- Web Development

## Notifications

Add notifications for:

- New resources
- New reviews
- New ratings
- Resource updates
- Admin announcements

## Email Notifications

Send emails for important account and resource activities.

## Profile Management

Allow users to update:

- Profile picture
- Name
- Email
- Department
- College
- Bio

## Discussion System

Allow students to discuss resources and ask questions.

## Like System

Allow users to like useful resources.

## Resource Reporting

Allow users to report:

- Incorrect resources
- Duplicate resources
- Inappropriate content
- Broken files

## Resource Moderation

Allow administrators to approve or reject resources.

Possible statuses:

- Pending
- Approved
- Rejected

## Cloud Storage

Move uploaded files to:

- AWS S3
- Cloudinary
- Google Cloud Storage

## PostgreSQL

Use PostgreSQL instead of SQLite for production.

## Mobile Application

Develop a mobile application using:

- React Native
- Flutter

## Cloud Deployment

Deploy using:

- Render
- Railway
- AWS
- DigitalOcean
- PythonAnywhere

---

# 🚀 Production Improvements

Before production deployment:

DEBUG=False

Recommended production configuration:

- PostgreSQL
- Proper ALLOWED_HOSTS
- Environment variables
- Production static files
- Cloud media storage
- HTTPS
- Secure cookies
- Production web server
- Secure secret management

---

# 🧠 Learning Outcomes

Through this project, I gained practical experience in:

- Python
- Django
- Django MVT architecture
- Django applications
- URL routing
- Django ORM
- Database models
- Model relationships
- Forms
- ModelForms
- Authentication
- File uploads
- Media handling
- CRUD operations
- Search
- Filtering
- Django templates
- Django Admin
- Database migrations
- SQLite
- Environment variables
- Git
- GitHub
- Responsive web design

---

# 📊 Project Information

| Category | Details |
|---|---|
| Project Name | EduShare |
| Project Type | Educational Resource Sharing Platform |
| Backend | Django |
| Language | Python |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite |
| Architecture | Django MVT |
| Authentication | Django Authentication |
| Version Control | Git & GitHub |
| Maximum Upload | 100 MB |
| Development Tool | Visual Studio Code |
| Main Branch | main |

---

# 👨‍💻 Developer

## Prashanth Shankar

Information Science Engineering Graduate

### Technical Skills

- Python
- Django
- JavaScript
- React.js
- HTML5
- CSS3
- Node.js
- Express.js
- SQL
- MongoDB
- Git
- GitHub

---

# 🔗 Links

GitHub Profile:

https://github.com/PrashanthShankar024

EduShare Repository:

https://github.com/PrashanthShankar024/EduShare

---

# 📄 License

This project was developed for educational and portfolio purposes.

---

# 🎓 EduShare

## Share Knowledge • Discover Resources • Learn Together

Built with ❤️ using Python & Django

-->