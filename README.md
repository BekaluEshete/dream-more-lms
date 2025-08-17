# Dream More LMS

Dream More LMS is a modern Learning Management System designed to empower learners and instructors with a robust platform for online education. Built with React (frontend) and Django (backend), it provides a seamless experience for managing courses, enrolling students, processing payments, and fostering a vibrant learning community.

## Features

- **Course Management:** Instructors can create, update, and manage courses, lessons, and materials.
- **User Authentication:** Secure login, registration, and account management powered by Django Allauth and Redux Toolkit.
- **Enrollment System:** Students can enroll in courses and track their progress.
- **Assessments & Certificates:** Integrated assessments and automatic certificate generation upon course completion.
- **Online Payments:** Secure payment processing with Chapa for course purchases.
- **Notifications:** Real-time notifications to keep users engaged and informed.
- **Discussions:** Built-in discussion forums for collaborative learning.
- **Responsive Frontend:** Fast and interactive UI using React, Tailwind CSS, and Vite.
- **Instructor & Learner Dashboards:** Personalized dashboards for both instructors and students.
- **Internationalization:** Supports multiple languages and is localized to Ethiopian time zone.

## Technology Stack

- **Frontend:** React, Redux Toolkit, Tailwind CSS, Vite
- **Backend:** Django, Django REST Framework, Django Allauth, drf_yasg (Swagger Docs)
- **Payments:** Chapa API integration
- **Database:** Configurable via Django settings

## Getting Started

### Prerequisites

- Node.js, npm, Python 3.10+, pip, Django
- (Optional) Virtual environment for Python

### Backend Setup

```bash
cd dream_more_lms
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup

```bash
cd dream-more-lms-frontend
npm install
npm run dev
```

### Access

- Backend API: `http://localhost:8000/`
- Frontend: `http://localhost:5173/` (default Vite port)

## Folder Structure

- `dream_more_lms/` - Django backend
- `dream-more-lms-frontend/` - React frontend

## Contributing

Pull requests and issues are welcome! Please follow standard practices for code contributions and documentation.

## License

This project is open-sourced under the MIT License.

---
