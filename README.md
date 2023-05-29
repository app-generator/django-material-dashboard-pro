# [Django Material PRO](https://appseed.us/product/material-dashboard-pro/django/)

**Django** starter styled with **[Material Dashboard PRO](https://appseed.us/product/material-dashboard-pro/django/)**, a premium `Bootstrap` Design from [Creative-Tim](https://bit.ly/3fKQZaL).
The product is designed to deliver the best possible user experience with highly customizable feature-rich pages. 

> **NOTE**: This product `requires a License` in order to access the theme. During the purchase, a `GitHub Access TOKEN` is provided. 

- 🛒 [Django Material PRO](https://appseed.us/product/material-dashboard-pro/django/) - `Product page` (contains payment links)
- 👉 [Django Material PRO](https://django-material-dashboard-pro.appseed-srv1.com/) - `LIVE Demo`

<br /> 

## Features: 

- ✅ `Up-to-date Dependencies`
- ✅ `Design`: [Django Theme Material](https://github.com/app-generator/django-admin-material-pro) - `PRO Version`
- ✅ `Sections` covered by the design:
  - ✅ **Admin section** (reserved for superusers)
  - ✅ **Authentication**: `Django.contrib.AUTH`, Registration
  - ✅ **All Pages** available in for ordinary users 
- ✅ `Docker`
- 🚀 `Deployment` 
  - `CI/CD` flow via `Render`

<br />

![Material Dashboard BS4 PRO - Premium Django Starter](https://user-images.githubusercontent.com/51070104/215266235-2b096d5a-4447-4a35-ba2b-933389b28bda.jpg)

<br />

## Manual Build 

> 👉 Download the code  

```bash
$ git clone https://github.com/app-generator/django-material-dashboard-pro.git
$ cd django-material-dashboard-pro
```

<br />

> Export `GITHUB_TOKEN` in the environment. The value is provided by AppSeed during purchase. 

This is required because the project has a private REPO dependency: `github.com/app-generator/priv-django-admin-material-pro`

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

## How to Customize 

When a template file is loaded in the controller, `Django` scans all template directories starting from the ones defined by the user, and returns the first match or an error in case the template is not found. 
The  theme used to style this starter provides the following files: 

```bash
< LIBRARY_ROOT >                     # This exists in ENV: LIB/admin_material_pro
   |
   |-- templates/                    # Root Templates Folder 
   |    |          
   |    |-- accounts/       
   |    |    |-- login.html          # Sign IN Page
   |    |    |-- register.html       # Sign UP Page
   |    |
   |    |-- includes/       
   |    |    |-- footer.html         # Footer component
   |    |    |-- sidebar.html        # Sidebar component
   |    |    |-- navigation.html     # Navigation Bar
   |    |    |-- scripts.html        # Scripts Component
   |    |
   |    |-- layouts/       
   |    |    |-- base.html           # Masterpage
   |    |    |-- base-auth.html      # Masterpage for Auth Pages
   |    |
   |    |-- pages/       
   |         |-- dashboard.html      # Dashboard Page
   |         |-- widgets.html        # Widgets Page
   |         |-- calendar.html       # Calendar page
   |         |-- *.html              # All other pages
   |    
   |-- ************************************************************************
```

When the project requires customization, we need to copy the original file that needs an update (from the virtual environment) and place it in the template folder using the same path. 

For instance, if we want to customize the `footer.html` these are the steps:

- `Step 1`: create the `templates` DIRECTORY inside the `home` app
- `Step 2`: configure the project to use this new template directory
- `Step 3`: copy the `footer.html` from the original location (inside your ENV) and save it to the `home/templates` DIR
  - Source PATH: `<YOUR_ENV>/LIB/admin_material_pro/includes/footer.html`
  - Destination PATH: `<PROJECT_ROOT>home/templates/includes/footer.html`

To speed up all these steps, the codebase is already configurated (`Steps 1, and 2`) and a custom footer can be found at this location:

`home/templates/includes/custom_footer.html` 

By default, this file is unused because the `theme` expects `footer.html` (without the `custom_` prefix). 

In order to use it, simply rename it to `footer.html`. Like this, the default version shipped in the library is ignored by Django. 

In a similar way, all other files and components can be customized easily.

<br />

## Recompile SCSS

- Copy the SCSS files from the UI LIbrary from `VENV` or from the UI library Repo 
  - **VENV**: `Lib/site-packages/admin_material_pro/static/assets`
  - https://github.com/app-generator/priv-django-admin-material-pro
    - `admin_material_pro/static/assets`
- Edit the SCSS files
- Regenerate SCSS (requires Node 16.x)
  - `yarn`: install modules
  - `gulp`: regenerate CSS files from SCSS 

<br />

## Deploy on [Render](https://render.com/)

- Create a Blueprint instance
  - Go to https://dashboard.render.com/blueprints this link.
- Click `New Blueprint Instance` button.
- Connect your `repo` which you want to deploy.
- Fill the `Service Group Name` and click on `Update Existing Resources` button.
- After that your deployment will start automatically.

At this point, the product should be LIVE.

<br />

---
[Django Material PRO](https://appseed.us/product/argon-dashboard-pro/django/) - **Django** starter provided by **[AppSeed](https://appseed.us/)**
