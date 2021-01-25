# create your custom drupal image here, based of official drupal
FROM drupal:8.8.5

# -y will ensure yes is selected automatically when prompted. rm --force clean up is good practice as apt-get install creates a cache always which we dont need in out image.
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /var/www/html/themes

# Always select the required branch only to clone from a repo by using the --branch, --single-branch and only the latest commit in that branch (usually with the most recent data) using the --depth 1 options. This also decreases the final image size & reduces build time.

# All these commands will run as 'root', hence the bootstrap files will be copied in as 'root' but Apache expects them to have 'www-data' user permissions, so we must change the owner of the files from 'root' to 'www-data'
# -R applies recrusively all sub-folders and files.
# chown format > user:usergroup <folder_affect_permissions-for>
RUN git clone --branch 8.x-3.x --single-branch --depth 1  \
https://git.drupal.org/project/bootstrap.git && chown -R www-data:www-data bootstrap

# Applications launch from the Apcache root folder
WORKDIR /var/www/html

# Only specify EXPOSE & CMD stanzas if they are not inlcuded in the FROM for this image.
