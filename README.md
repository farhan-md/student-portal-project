# Student Portal Project

A simple Django project to manage courses and students featuring course listing, student listing, and adding students through a form with validation.

## Features
- Manage courses with name and credits.
- Manage students with name, email, and course.
- Django admin panel for managing data.
- Add new students through a form with validation.

## Requirements
- Python 3
- Django
- HTML

## How to Use

1. **Login to the Admin Panel**  
   Go to `/admin/` and log in with your superuser credentials. Add some courses first.

2. **Add Students via Form**  
   Navigate to `/students/add/` to create a new student. Enter name, email, and select a course.

3. **View Data**  
   - Go to `/students/` to see all registered students.  
   - Go to `/courses/` to view all courses.

4. **Validation**  
   The form will not submit if the name is empty or the email is invalid.
