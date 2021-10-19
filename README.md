### What you will expect on this sample Project.
* Faster API endpoint creation using our re-usable API classes.
* Demonstration of writing clean codes and project structure.
* Reusable API classes.
     - https://github.com/arceduardvincent/valhalla/blob/master/backend/generic/views.py
* A consistent API response formats.
* API docs enabled. 
* Token Base authentication.
* Use pipenv for python env.
* API - AUTH
    - login.
    - logout.
    - change password.
    - password reset confirm via email.
    - User PUT/PATCH request.

* API - Rest AUTH 
    - Auth Registration
    - Registration verify by email
* API - User
    - Create user.
    - Update(Patch/PUT )user.
    - Get user.
    - Delete user.

### Deployment
1. Docker setup.
2. Heroku setup.

### Installation
1. Install [pipenv](https://pypi.org/project/pipenv/)
2. Clone this repo and `cd backend`
3. Run `pip install --user --upgrade pipenv` to get the latest pipenv version.
4. Run `pipenv --python 3.7`
5. Run `pipenv install`

### Getting Started
1. Run `pipenv shell`
2. Run `python manage.py makemigrations`
3. Run `python manage.py migrate`
4. Run `python manage.py runserver`


### Where you can find the API docs?
    http://localhost:8000/api-docs/

### Author
    Eduard James Aban
