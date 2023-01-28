# [Django Argon PRO](https://appseed.us/product/argon-dashboard-pro/django/)

**Django** starter styled with **[Argon Dashboard PRO](https://appseed.us/product/argon-dashboard-pro/django/)**, a premium `Bootstrap` Design from [Creative-Tim](https://bit.ly/3fKQZaL).
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

> **NOTE**: This product `requires a License` in order to access the theme. During the purchase, a `GitHub Access TOKEN` is provided. 

- 🛒 [Django Argon PRO](https://appseed.us/product/argon-dashboard-pro/django/) - `Product page` (contains payment links)
- 👉 [Django Argon PRO](https://django-argon-dashboard-pro.appseed-srv1.com/) - `LIVE Demo`
- 🚀 [Go LIVE in Minutes](https://www.youtube.com/watch?v=9OtA9Kw01yM) - `video presentation`

<br /> 

## Features: 

- ✅ `Up-to-date Dependencies`
- ✅ `Design`: [Django Theme Argon](https://github.com/app-generator/django-admin-argon-pro) - `PRO Version`
- ✅ `Sections` covered by the design:
  - ✅ **Admin section** (reserved for superusers)
  - ✅ **Authentication**: `Django.contrib.AUTH`, Registration
  - ✅ **All Pages** available in for ordinary users 
- ✅ `Docker`
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

<br />

![Django Argon PRO - Premium Seed project powered by Flask.](https://user-images.githubusercontent.com/51070104/213974264-fe9250ff-7035-427b-b63f-bf69790f5a73.png)

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-argon-dashboard-pro.git
$ cd django-argon-dashboard-pro
```

<br />

> Export `GITHUB_TOKEN` in the environment. The value is provided by AppSeed during purchase. 

This is required because the project has a private REPO dependency: `github.com/app-generator/priv-django-admin-argon-pro`

```bash
$ export GITHUB_TOKEN='TOKEN_HERE'  # for Linux, Mac
$ set GITHUB_TOKEN='TOKEN_HERE'     # Windows CMD
$ $env:GITHUB_TOKEN = 'TOKEN_HERE'  # Windows powerShell 
```

<br />

> 👉 Install modules via `VENV`.


```bash
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

<br />

> 👉 Edit the `.env` using the template `.env.sample`. 

```env

# True for development, False for production
DEBUG=True

```

<br />

> 👉 Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> 👉 Create the Superuser

```bash
$ python manage.py createsuperuser
```

<br />

> 👉 Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

---
[Django Argon PRO](https://appseed.us/product/argon-dashboard-pro/django/) - **Django** starter provided by **[AppSeed](https://appseed.us/)**
