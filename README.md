# Django Todo App

This is a Todo List application built using Django.  
It allows users to add, update, complete, and delete tasks with a user-friendly interface.

## Features
- Add new tasks
- View all tasks
- Update existing tasks
- Delete tasks
- Mark tasks as completed (strike-through effect)
- Checkboxes for task completion
- Dark and Light theme toggle with symbol
- Data is stored securely in a local MySQL Workbench database

## Technologies Used
- Python
- Django
- HTML, CSS (Basic templates)
- JavaScript (for theme switching and checkbox functionality)
- MySQL Workbench database

## Project Structure
```text
├── manage.py
├── project_folder/
│   ├── urls.py (project-level)
├── app_folder/
│   ├── urls.py (app-level)
│   ├── views.py
│   ├── templates/
│       ├── tasks.html
│   ├── static/ (if you have CSS/JS files)
