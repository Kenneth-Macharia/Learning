# Intro

- Digital oceans offers servers for rent, to run our app.
- The users full access to the server machines running their apps.
- Users do have to set up and configure their servers before deploying their apps.
- Droplets are the servers rented.
- Create a new ubuntu droplet and set it up, once done open it's console and log
  into it. Log in details will be sent via email.

## Setting up an Ubuntu Droplet

- If running unix, you can connect remotely to the droplet via terminal, if on
  Windows use the online console:

  1. Enter ssh &lt;username>@&lt;server address> (ssh is ubuntu's connection protocol)
  2. Enter the server password
  3. This logs in as 'root' which in unix based systems is the super user.
  4. apt > ubuntu package manager (similar to pip), can be queried for updates
    for any installs on the server: #apt-get update.
  5. Create another user so as not to use the root super user in the server for
    non-admin tasks: #adduser &lt;username> then follow instructions. This also
    creates a group with the same name as the user, so as to share rights.
  6. Ensure the new user can temporarily get root rights for admin tasks like
    installing programs in the server: #visudo , modify the file's user rights
    by adding the created user with the same parameters as root.
  7. For security reasons, deny root sign in rights and grant the new user
    this right: #vi /etc/ssh/sshd_config. (Opens vim editor file for user configs
    service, press i to enter insert mode & esc to exit insert mode. esc > : > wq,
    saves changes and exits the vim editor). In the user service file change:
    1.PermitRootLogin > no
    2.Add to PasswordAuthenitcation: 'AllowUsers &lt;username>'
    Exit the user config service and enter:# service sshd reload to refresh.
  8. #exit to exit the server.
  9. Log in as &lt;user> as above. To get root rights: #sudo su and enter password.
    To return the normal user &lt;user>: #exit.

## Setting up PostgreSQL

- Install postgres: #apt-get install postgresql postgresql-contrib.
- Switch over to the postgres user for the database: #sudo -i -u postgres. This also
  creates a database called postgres, the same name as the user connecting to it.
- Connect to the postgres database: #psql, prompt changes to : postgres=#
- Check connection details:#\conninfo
- We can run other sql commands : <https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546>
- #\q disconnects from the database & # exit reverts to the root super user.
- Link the new server user to postgres:

 1. Log in
 2. Make the user, the root user: sudo su
 3. Become the postgres user: #sudo -i -u postgres
 4. Create a postgresql user/role, having the same user name as the server user (must):
    #createuser &lt;username> -P (-P allows setting a password)
 5. Create a db for the new user #createdb &lt;username> (to delete a db #drop db
    using user postgres ONLY)
 6. Set All local connections to db server to require passwords to connect:
    #sudo vi /etc/postgresql/9.5/main/pg_hba.conf to edit the postgres user
    configuration file. Ammend unix domain socket connections from 'peer' to md5.
    SQLAchemy require this configuration, else it will not work.
 7. While as root user (#sudo su), #update-rc.d postgresql enable to configure
  postgres to start when server boots up.
 8. Use #service postgresql &lt;command> to instruct the postgres server, for options:
  <https://www.postgresql.org/docs/9.5/static/app-pg-ctl.html>

## Setting up NGINX

- This is a web server and reverse proxy.
- It will act as a gateway between the app and the external users. It will receive
  app requests and direct them to the right app.
- It allows multi-threaded operations of the app via uwsgi.
- Allow running of multiple flask apps on the server, simultaneously.
- Install nginx: #sudo apt-get update then #sudo apt-get install nginx.
- Check the ubuntu firewall status: #sudo ufw status, if inactive, activate it:
  #sudo ufw enable.
- Give nginx access through the firewall: #sudo ufw allow 'Nginx HTTP'
- Ensure ssh connections to the server are not blocked: #sudo ufw allow ssh.
- Check that Nginx is running using the ubuntu system controller:
    #systemctl status nginx (also start nginx, stop nginx , restart nginx)

## Configure NGINX Server Block

- Create the ngix config file for the server block which will host the app:
    #sudo vi /etc/nginx/sites-available/items-rest.conf
- Insert the following configurations:

 1. Server:specify's the app is a server and will listen for incoming requests
  and action them:

    (a) Default port which is 80 for the internet so that the ':port' part of a url
    is omitted.
    (b) Forward the ip of the requester to the flask app
    (c) Set the flask app to run on local host IP
    (d) server name which is localhost

 2. Location /:Whenever someone accesses the root location of the server, they will
  be directed as specified here, in this case to the app:

    (a) Include uwsgi params so that ngix can communicate with uwsgi
    (b) uwsgi pass:creates a connection point between the app and nginx in form of
     another config file.
    (c) uwsgi modifier parameter to tell the app threads when to die if they are blocked.

  3.Error pages:

    (a) 404 redirect to the 404.html saved in a folder specified. Nginx comes with
     these pages.
    (b) Any 500 error to the 50x,html file.

- Basically after specifying what we are serving and how to serve it (1), then we
  just specify the location of the app server and parameters for its dependancies
  e.g. uwsgi (2)
- If for some reason we are unable to do any of the above follow the error handlers
  endpoints (3)

_See the 'items-rest.conf' file_

- After creating the above file, enable it by creating a soft link between the config
  file and the nginx config source folder:

  `sudo ln -s /etc/nginx/sites-available/items-rest.conf /etc/nginx/sites-enabled/`

## Adding the Flask App to the Server

 - Create the folder to host the flask app, as specified in the conf file:

  `sudo mkdir /var/www/html/items-rest`

  _Note the folder is created using the user 'root' (used sudo), thus 'ken' does not have access to it_

- To give 'ken' access make the user the folder owner:

  _`sudo chown ken:ken /var/www/html/items-rest` (chwon - change owner)_

- Move cd into the dir: `cd /var/www/html/items-rest`

- Clone the app from github into the flask app dir, add a ' .' at after the github
  url to tell the server to put all the contents from the url in the current

  _ensure the folder is empty or the ' .' will not work_

- Install some python dependancies:

  1. python-pip - Python package manager
  2. python3-dev - enable installation of psycopg2 and uwsgi
  3. libpg-dev - allow running of psycopg2

  `sudo apt-get install python-pip python3-dev libpq-dev`

- Instal virtualenv and create a virtual env in the app folder.
- Activate 'venv' and install all from requirements.txt `pip install -r requirements.txt`

## Configure uWSGI

- Create an ubuntu service that will run when the server start and will set
environment variables, in this case uWSGI (See uwsgi_items_rest.service file)

  1. Creates a new service `sudo vi /etc/systemd/system/uwsgi_items_rest.service`
  file in the ubuntu service folder)
  2. Define a description section [Unit]
  3. Define a services unit to tell ubuntu what params to run the service with:

      (a) Tell ubuntu which program to run, in this case uWSGI in the venv/bin.
      (b) Includes the uwsgi.ini file which specify's how to run the flask app.
      (c) Includes user and group id to run the uwsgi service.
      (d) Specify the log to write the logs.
      (e) Specify the process to restart always if it dies.
      (f) Specify the process to shut down gracefully without losing data.
      (g) Notifications

  4. Define the 'install section' to allow the service to start when the server
    boots up.

- Edit uwsgi.ini so that the app can communicate with uwsgi and uwsgi can communicate
  with nginx.
- Have a section [uwsgi] and in it, add the following:

    1. Base folder where the uwsgi folder exists
    2. The run file, in this case run.py
    3. Module to import from the above file (var)
    3. Home folder for uwsgi executable
    4. Root folder for the python project
    5. Socket.sock file to allow communication between uwsgi and NGINX
    6. Permissions to the socket file, 777 allows all user access.
    7. processes (depend on the droplet)
    8. threads (depend on the droplets)
    9. harakiri (if one of the thread encounter a problem the emperor will kill it after this time in sec
    10. callable is the app variable in the run.py
    11. Place to log the python app output logs

## Start the Ubuntu App service to run the Flask App

 `#sudo systemctl start uwsgi_items_rest`

## Tail nginx, uwsgi and postgres log for real time info

 `sudo tail -f /var/log/nginx/access.log /var/log/nginx/error.log /var/www/html/items-rest/log/uwsgi.log /var/log/postgresql/postgresql-9.5-main.log`
