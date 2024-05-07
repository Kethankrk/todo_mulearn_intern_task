Follow these steps to run the Django project on your local machine.

## Prerequisites

Before you begin, make sure you have the following installed:

- Python (version specified in the project's requirements)
- pip (Python package installer)

## Step 1: Get the Project Code

First, you need to obtain the project code. You can either:

- Clone the project repository from a version control system like Git.
- Download the project code as a ZIP file and extract it.

## Step 2: Create a Virtual Environment (Optional but Recommended)

It's a good practice to create a virtual environment to isolate the project dependencies. Navigate to the project directory and run the following command to create a new virtual environment:

```
python -m venv env
```

## Step 3: Activate the Virtual Environment

Activate the virtual environment:

- On Windows:
  ```
  env\Scripts\activate
  ```

- On Unix or macOS:
  ```
  source env/bin/activate
  ```

## Step 4: Install Project Dependencies

Install the project dependencies by running the following command in the project directory:

```
pip install -r requirements.txt
```

This will install all the required packages listed in the `requirements.txt` file.

## Step 5: Apply Database Migrations

Django uses migrations to manage database schema changes. Run the following command to apply any pending migrations:

```
python manage.py makemigrations
python manage.py migrate
```

## Step 6: Create a Superuser (Optional)

If the project requires an admin user, create a superuser by running the following command:

```
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password for the superuser.

## Step 7: Run the Development Server

Start the Django development server by running the following command in the project directory:

```
python manage.py runserver
```

You should see output similar to the following:

```
Performing system checks...

System check identified no issues (0 silenced).
May 16, 2023 - 15:50:53
Django version 4.2, using settings 'myproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Step 8: Access the Project

Open your web browser and visit `http://127.0.0.1:8000/` to access the project.

If the project has a different URL or port configuration, make sure to use the appropriate URL provided in the server output.

-----------------------------------------------------------------------------------------------------------------------------


# Todo REST API
API for managing todo items

## Version: 1.0.0

### /api/login/

#### POST
##### Summary:

Login route to get refresh and access token

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |

### /api/register

#### POST
##### Summary:

Register a new user

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |
| 400 | Bad request |
| 500 | Internal server error |

### /api/todo

#### GET
##### Summary:

Get all todos for the authenticated user

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | query | ID of the todo to retrieve (optional) | No | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Successful response |
| 404 | Todo not found |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |

#### POST
##### Summary:

Create a new todo

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |
| 400 | Bad request |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |

#### DELETE
##### Summary:

Delete a todo

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | query |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 204 | Successful response |
| 404 | Todo not found |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |

#### PATCH
##### Summary:

Update a todo

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |
| 400 | Bad request |
| 404 | Todo not found |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |

### /api/make-done

#### POST
##### Summary:

Mark a todo as done

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| id | query |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 201 | Successful response |
| 404 | Todo not found |
| 500 | Internal server error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| bearerAuth | |
