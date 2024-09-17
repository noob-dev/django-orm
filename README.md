# Django Models

## Project Description

This Django project consists of models representing the following entities:

- **Faculty**: Represents the faculties within an institution.
- **Group**: Represents groups of students within a faculty.
- **Student**: Represents students belonging to both a specific group and a kafedra.
- **Kafedra**: Represents the departments within an institution.
- **Subject**: Represents the subjects offered by different kafedras.
- **Teacher**: Represents the teachers who teach specific subjects.

## Models Overview

1. **Faculty**:
   - `id`: Auto-incremented primary key.
   - `name`: Name of the faculty.

2. **Group**:
   - `id`: Auto-incremented primary key.
   - `name`: Name of the group.
   - `faculty`: Foreign key referencing the `Faculty` model.

3. **Student**:
   - `id`: Auto-incremented primary key.
   - `first_name`: Student's first name.
   - `last_name`: Student's last name.
   - `kafedra`: Foreign key referencing the `Kafedra` model.
   - `group`: Foreign key referencing the `Group` model.

4. **Kafedra**:
   - `id`: Auto-incremented primary key.
   - `name`: Name of the kafedra.

5. **Subject**:
   - `id`: Auto-incremented primary key.
   - `name`: Name of the subject.
   - `kafedra`: Foreign key referencing the `Kafedra` model.

6. **Teacher**:
   - `id`: Auto-incremented primary key.
   - `first_name`: Teacher's first name.
   - `last_name`: Teacher's last name.
   - `subject`: Foreign key referencing the `Subject` model.

## Foreign Key Relationships

- **Group** → **Faculty**
- **Student** → **Group**, **Kafedra**
- **Subject** → **Kafedra**
- **Teacher** → **Subject**

## Design Source

These models were created according to the structure from **dedesigner.comm**.

## Requirements

- Django 3.x or higher

```bash
pip install django
