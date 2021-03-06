# Intro

- Is a python web development framework.
- It is used to map a user requested url to code that is meant to handle it, then using templates, cresate the requested html dynamically, then fetch requested data from a database and inject it to the generated html to dipslay to the user. It is thus an interface between the front and back end.
- Developed in 2003 by web dev at the Lawrence Journal-World newspaper, when they started using python for their dev work. Because of its writer influenced origin, good documentation is key to django and it has elaborate documentations to reference.
- Using a virtual env with django apps is improtant so us to not break compatibility with the current web app, when testing out updated python packages the web app relies on.
- By using a venv, you isolate packages for a specific app away from the those of another app.
- Create a venv using conda or pip (see for flask projects), for conda run:

 `conda create --name venv_name django` _Meaning create a venv called venv_name and initialize it as a django package_

- The above command may try to install python 2 by default, so instead create the venv as a python 3 package first instead

 _`conda create --name venv_name python=3.7` View the packages to be installed and confirm the correct version, the proceed with init_

_Run `conda info --envs` To view all venv present_

- Django provides a command line tool called django-admin to easily manage django projects e.g

## To create a new django project run

`django-admin startproject project_name`

- Which initializes a new project folder with some files in them:

 1. __init__.py :tells python that this folder is a python package and can be imported.
 2. settings.py :all settings for the project
 3. urls.py :stores all url patterns of the project i.e the various pages for the web app
 4. wsgi.py :web server gateway interface used during the app deployment
 5. manage.py :Associated with alot of the commands used during the building of the web app

- A Django project is a collection of applications and configurations that wehn combined, make up the full web application ie. site + logic
- A django application is created to perform a specific function for the website. These are re-useable by us or by other people.

- To create an app run:

 `python manage.py startapp app_name`

- This creates a django app folder with some files and folders:

 1. __init__.py
 2. admin.py :used to register models to be used with django's admin interface
 3. apps.py :application specific configs
 4. models.py : applications data models
 5. tests.py :test functions for the app
 6. views.py :functions that handle requests and return responses
 7. Migrations :database info relating to the models

- Specify that this new app exists by adding it to the project settings.py file
- Run database migrations to effect the project changes (see models below)

- Django uses the ModelViewTemplate architecture design pattern (MVT).

## Templates

- Contain static parts of the html page ie. the html files
- Template tags with their own special syntax allows the injection of dynamic content that the app's views will produce to affect the final html.
- Working with templates:

 1. Create a 'templates' folder inside the project folder and then sub directory inside it, for each specific app's templates, then inside the template main folder, the app folder.
 2. Edit the DIRS key inside the 'TEMPLATES' dict in settings.py to let Django know where the tmeplates are.
 3. Since DIR uses absolute paths to the templates, use os.path.dirname(__file__) to fetch the file independent of platform or file system (__file__) representing the file to fetch the path for)
 4. Create an index.html create inside of template/app_folder
 5. Insert html tags aka Django template variables that will allow the injection of content into html direclty from django. {{}}
 6. Use the render() inside the index() in the views.py file to enable the injection above.

## Static

- Folder containing media files, css and JavaScript.
- Working with static files:

 1. Create a 'static' folder in same location as the templates folder
 2. Add its path to settings.py.
 3. For images, create an images folder under the static folder, where the images will go.
 4. Inside a html file, insert the static file html tag {% load staticfiles %} at the top of the file under the DOCTYPE declaration.
 5. Insert the desired photo using &lt;img src={%static 'images/pic.jpg' %}>

## Media Files

- Unlike the static files, media file are user provided e.g profile photo uploads and should be stored in a media folder and reference to the folder added to settings.py (SEE USER_AUTH APP):

Models & Databases

- Edit the database engine in settngs.py (SQLite is default).
- Models are used to interact with databases from the django app.
- To implement models, we use a class structure in the relevant app's models.py file, which is a sub class of django.db.models.Model.
- Each attribute of the class reps a field containing a column name with constraints in SQL.
- After creating the model classes, they can them be migrated to actual database tables by Django by running the django command:

 `python manage.py migrate`

- The register the changes to the app:

`python manage.py makemigrations app_name`

- Then migrate the database one more time: >> python manage.py migrate

_Use the interactive shell in manage.py to play around the models `python manage.py` shell_

 _Import the model and if error occurs, there was a migration problem_
 `from first_app.models import Topic`

 _Print All topics_
 `print(Topics.objects.a())`

 _Add topics_
 `t = Topic(top_name="Social Network")`
 `t.save()`

 _To quit the interactive shell_
 _quit()_

 _If you dont define a primary key, django defines a default one called id_

## Admin Interface

- To use the models with the admin interface, we need to register them in the apps admin.py file:

 `from django.contrib import admin`
 `from app.models import model1, model2`
 `admin.site.register(model1)`
 `admin.site.register(model2)`

_The admin interface is a key feature of Django that allows easy interaction with the database created_

- To use the admin interface, first create a "superuser" `python manage.py createsuperuser`
- Then provide an name, email and password.

_You can use the python 'Faker' library to quickly populate a new DB with some fake test data_

- First install the lib: `pip install Faker your venv`

 _Faker Docs online at faker.readthedocs.io_

## Django MTV Implementation

 1. Import the necessary model.py in the views.py
 2. Use the view to query data from the model
 3. Pass the results of the query to template
 4. Edit the template to accept and display the data from the model
 5. Map a url to the view

## Forms

- Extra features from HTML forms:

 1. Quickly generate HTML form widgets using template tagging
 2. Validate data and process into a python data structure direct
 3. Create form versions of the models
 4. Quickly update models directly from forms

- Working with django forms:

1. Create forms.py file inside the app folder
2. Create django form classes just like the models classes

_Demo:_

`import django import forms`

`class FormName(forms.Form):`
 `name = forms.CharField()`
 `email = forms.EmailField()`
 `text = forms.CharField(widget=forms.TextArea)`

3. Show the form using a view:

- Import the forms in the views file
- Create a view for the form:

`def form_view(request):`
 `form = forms.FormName()`
 `return render(request, 'form_name.html', {'form':form})`

4. Add the form view into the apps urls file:

 `re_path(r'formpage/', views.form_name_view, name='form_name')`

5. Create the html file inside template that will hold the template tagging for the form.
6. Update the settings file
7. Form tags look lke this {{ % form.as_p % }} there are many form method that assist in improving the from presentation of the template.
8. { % csrf_token % } (cross site request forgery) token is requred for every from POST request and secures the site.
9. Working with the POST data received in the view:

- Check if the request method is POST
- Validate the form data
- Then access the data in returend dict called 'cleaned_data' e.g cleaned_data['name']

## Form Validation

- Necessary to prevent mis-use of the site form either by users or malicious bots
- Custom clean_form class methods can be used to prevent site mis_use.
- See notes in demo app (forms_app)

## Model Forms

- Used to accept user input and pass it to a model.
- Uses forms.ModelForm helper class in the forms.py file, which allows the creation of a form from a pre-existing model.
- An inline class (class within a class) called Meta is then used to provide information for conneting the model to the form.
- Implementation of model forms in forms.py file:

 1. import forms from django
 2. import the model
 3. Create the form class, inheriting from forms.ModelForm
 4. Add the form fields incase of custom field validators, else leave them out to be auto generated from the model.
 5. Add the Meta class within the form class
 6. Connect the model, 'model = my_model'
 7. Connect up the model fields to the form using either the following options:

 (a) fields = '__all__' which grabs all the model fields for the form
 (b) exclude = ['field1, 'field2'] lists the fields from the model to exclude
 (c) fields = ('field1', 'field2') lists the fields to include

_See level_ _two app for demo_

## Realtive URLS with Templates

- Involves replacing hard-coded url paths within the html e.g in anchor tags with relative ones, ensuring the app is system independent.
- Ways to do this:

 1. Replace absolute link with relative link e.g href='basicapp/thankyou' with href="{% url 'thankyou' %}"
 2. Replace absolute links with links to actual views e.g href="{% url 'basicapp.views.thankyou'%}" (NB) Deprecated in Django 2.0
 3. Future proof and recommended for referencing a view:

	(a) Inside the urls.py () file, add a variable called app_name and set it to your apps name.
	(b) In the HTML, "{% url 'your_app_name: view_name'%}"

## Template Extending / Inheritance

- Using base template ensures DRY code and maintenance of a std look and feel across the entire website e.g a navbar on top of all pages, we set it to a base html file and inherit it whenever needed.
- Implmenetation:

 1. Id repetitive parts of the project
 2. create base template for them
 3. Set tags int he base template
 4. Extende and call those tags in other html files

## Template Filters

- These allow us to effect content before displaying it, thus allowing flecibility to use a single data source.
- Implementation (Built-in filters):

 1. Django docs have a list of all availble filter
 2. Filter take the form {{ value_key|filter_to_apply_to value }}, where the value key is a dict key, with the key referencing data that you will apply the filer to.
 3. Filters can also take args: {{ my_date|date:"Y-m-d" }}
 4. Django filters are usually based on python functions and properties for affecting data e.g strings and doing arithmetic before displaying
 5. Create the dict in views.py for the view to be effected, the dict can have any number of values.
 6. Pass the context_dict into the render fucnction as a separate arg
 7. Add the required filters in the html page

- Implementing custom filters:

 1. In the same level as models.py, create a new python package called 'templatetags' ie. folder having a __init__.py file.
 2. Create a .py file that will house the custom filters.
 3. Inside the file, import templates from django
 4. Create an object called 'register' and set it to 'templates.Library()'
 5. Create a custom filter as a normal python function. (See list of available filters from django docs)
 6. Regiter the filter: 'register.filter('filter_call_name', filter_function_name)'
 7. LOAD THE CUSTOM FILTERS IN THE HTML TEMPLATE USING THE TAG {% load my_filters %}

## User Authentication

- To enable this functionality, we need the following apps in the settings.py INSTALLED_APPS list:

 1. django.contrib.auth
 2. django.contrib.contenttypes

- If they are not there, add them then run database migrations.
- Paswords are jashed using django's inbuilt PBKDF2 algo (uses SHA256 hash), which is pretty secure, though you can implement a different hashing algo, if higher security levels are required e.g bcrypt or argon2 [installation pip install bycrypt or django[argon2]]
- Then inside a PASSWORD_HASHERS list in settings.py, add your hasher in the order of desired use, if the lib support for those is not available django will revert to the default.
- Password validator options can also be added, to enforce user password rules in AUTH_PASSWORD_VALIDATORS.
- Django has an inbuilt auth model called User by default (refrain from calling any custom models 'User'), which already has details for users of the website (see doc for fields). User model class and adding the extra fields there. User objects also have attrs by default e.g is_active etc
- You can add more user fields by creating another model that indireclty (OneToOne) inherits from the default User class e.g images for user profiles.

_To work with images in Django the 'pillow' lib needs to be installed_
_To use auth with CBVs, instead of auth decorators, use mixins, which are auth classes that the CVBs can inherit from, to automatically get the auth functionality_

## Deployment

- Links to guide for deploying to some services are in the links section e.g AWS, Heroku, PythonAnywhere, Digital Oceans.
- Working with PythonAnywhere:

 1. Create free account on PythonAnywhere.com
 2. Under console, run bash and create a virtual env for your project:

	`mkvirtualenv --python=python3.7 project_name`

 3.Install django with the virtual env activated if it has not already been activated.
 4. Install other requirements for the web app (Have a requirements file handy)
 5. Make migrations as you would locally
 6. Create a super user as usual
 7. Create a web app under the web tab:

	(a) Set the virtualenv path
	(b) Set the source code path (to your project)
	(c) Configure WSGI file
	(d) Set the admin static files path
	(e) Create your own static files folder and set its path
	(f) Set debug to false

## Class Based Views (CBVs)

- Using class and OOP for the views instead of function based views.
- Django provides classes to implement the CBV which are simply imported.
- CBVs use the TemplateView class to call views instead of functions.
- To use the TemplateView class, create a view class and inherit from TemplateView, then set a 'template_name' variable within your view class to the template to render.
- Model with CBVs:

	(a) Django has generic classes to handle models and model data e.g ListView and DetailView
	(b) Rather than having the template in a project level dir, its common practice to have that inside the app folder, when working with CBVs.
	(c) The two Django classes above simplify the work of listing model data and details rather than us having to do it manually, since these operations are very common.

## CRUD

- Django provides CBVs to perform crud operations. The ListView and DetailView CBVs are used for retrieving resources while the CreateView, UpdateView and DeleteView classes are used to perform create, update and delete operations respectively.

## Django Debug Toolbar (See level_two_project)

- Is a package that is useful in debugging Django projects.
- Ideal for large projects.
- To use the debug toolbar:

	(a) Install the package: pip install Django-debug-toolbar
	(b) Add the debug app after the 'staticfiles' in the 'installed apps' list: 'debug_toolbar'
	(c) Add the toolbar to middleware in the settings.py:

	`'debug_toolbar.middleware.DebugToolbarMiddleware'`

	(d) Add to settings.py (at the bottom) the localhost IP addres to ensure the debug toolbar is only visible if the server is running locally, incase the debug property is left to TRUE:

	`INTERNAL_IPS = ['127.0.0.1']`

	(e) Add a url in the projects url file to link to the debug toolbar and view it:

	`from Django.conf import settings`

	(f) Under the main urlpatterns list add:

			if settings.DEBUG:  # If true
				import debug_toolbar
				urlpatterns = [ url(r'^__debug__', include(debug_toolbar.urls)) ] + urlpatterns

- When running the django server, the debug_toolbar will appear on the RHS of the screen.

_CUSTOMIZING THE ADMIN PAGE - DEMO EDI-ADMIN-PAGE PROJECT_

## Look and Feel

- For projects where osme users will have access to the admin page, its look can be customized by overwriting the html file associated with the admin page.
- Under the project's folder, add the usual 'templates' folder and an 'admin' under that.
- Visit django's github page and locate the admin html files:

`/django/contrib/admin/templates`

- Id the file of interest and copy and paste it into your admin folder in your project.
- EDIT the copied file, then add the templates url in your settings.py

_To make massive changes to the enter admin section, overwrite the 'base.html' file as all other template extend it._

## Field Ordering

- By default the admin page display the model fields in the order they were define, this order can be changed in the admin.py file:

	(a) Create a 'MyModelAdmin' class in admin.py
	(b) Add a fields list of your models fields in the order you want them displayed
	(c) Register the new class alongside the model it relates to.

## Adding Search Fields

- Achieved by adding a 'search_fields' list attr.
- See videos admin.py

## Adding Filters

- Filters can be added to the views for the models and will appear on the right hand side of the view and will auto filter depending on the data type.
- These wil look like the filter in the admin auth section.
- This is achieved by adding a 'list_filter' list attr.

## Adding more model fields to the model list view, such that you can view all the fields on a single row in a table-style format.

- This achieved by adding a 'list_display' list attr and the field names to display, in the required order. The first field name will have the link to the model detail view.

## Edits in List model view

- To aid the bulk editing, some if the fields displayed in the list view can edited without having to enter the detail view.
- This achieved by adding the 'list_editable' attr.
