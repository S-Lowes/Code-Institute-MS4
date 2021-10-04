# Forking, Cloning, Deployment

[Back to README](README.md)

### Forking the GitHub Repository

By forking the GitHub Repository we are making a copy of the original repository on a GitHub account to view and/or make changes without affecting the original repository. This is done with the following steps:

- Log in to [GitHub](https://github.com/) and locate the GitHub Repository.
- At the top of the Repository just above the "Settings" button on the menu, locate the "Fork" button.
- Click the button and now you should have a copy of the original repository in your GitHub account.

### Making a Local Clone

- Log in to [GitHub](https://github.com/) and locate the GitHub Repository.
- Under the repository name, click "Clone or download".
- To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
- Open Git Bash
- Change the current working directory to the location that you want the cloned directory to be made.
- Type `git clone`, and then paste the URL you copied earlier.

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for a more detailed explanation of the cloning process.

### Deploying to Heroku

##### Gunicorn
Gunicorn is used as the server when the app is deployed to Heroku. To install Gunicorn run `pip3 install Gunicorn` and then add the package to the apps `requirements.txt` file using `pip3 freeze > requirements.txt`

##### Procfile
Heroku needs a 'Procfile' to know how to run the app. In this instance, a Profile was created in the root directory with the code `web: gunicorn amphii.wsgi:application` saved within.

##### Create Application

1. Navigate to Heroku.com and login.
1. Click on the "New" button in the top right of the page and select "Create new app."
1. Enter the name of the app, select the region and click "Create app."

##### Connect to GitHub Repository

1. Click the deploy tab and select "GitHub - Connect to GitHub."
1. Under the section "Search for a repository to connect to" enter the repository name in the box provided.
1. Once the repository has been found, click the "Connect" button.
1. Once connected, you can choose to automatically deploy any updates made in the GitHub repository or to do so manually by selecting the branch you wish to deploy and clicking on the appropriate button.
1. Following this, click on the 'Settings' tab and then click 'Reveal Config Vars'
1. Within the 'Reveal Config Vars' section, add the variables which would be found in your local environment variables. These variables are kept here because they contain sensitive data.
1. Add the new app url and `localhost` to the project's `settings.py` file in the:
    * `ALLOWED_HOSTS = ['app-name.herokuapp.com', 'localhost']`

#### Set up Heroku Postgres
Heroku provides a Postgres database to be used in the project which can be accessed from Gitpod. To set up the database I followed these steps:

1. On Heroku, within the app dashboard, click on the resources tab at the top of the page.
1. In the 'Add-ons' search bar, type in 'Heroku Postrgres' and click on the resulting option.
1. Ensure 'Hobby Dev' is selected as the plan name and click on 'Submit Order Form'. This will automatically attach the database to the app and add the database URL to the app's 'Config Vars' on the settings page. 
1. Navigate to the 'Settings' tab and within the 'Config Vars' section ensure the `DATABASE_URL` variable has been set and add a new variable set to:
    `DISABLE_COLLECTSTATIC: 1`

This is to temporarily stop Heroku from collecting the app's static files as these will later be hosted using Amazon's S3 service.

1. Back in the IDE, install the packages required to integrate the app and database using pip:
    * `pip3 install dj_database_url`
    * `pip3 install psycopg2_binary`
1. Add the packages to a `requirements.txt` file in the root directory to ensure Heroku knows which dependencies are required to run the app:
    * `pip3 freeze > requirements.txt`
1. Since I used two PostgreSQL Databases (One for Development, One for Production) I had to specify which I wanted to use and when. So, the following statement was added to the projects `settings.py` file having imported `dj_database_url` at the top of the file:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get(
            'HEROKU_POSTGRESQL_CYAN_URL'))
    }
```

#### Push the code to Github and Deploy to Heroku
With the previous steps complete, in the terminal run `python3 manage.py makemigrations` and then `python3 manage.py migrate` to ensure any outstanding migrations have been made and are ready to use in the deployed app. You can use the `--dry-run` flag when making migrations to check what migrations are about to be made.

1. Commit all changes and push to Github
1. If automatic deploys are not enabled then you will need to visit the 'Deploy' tab of the Heroku dashboard and click on 'Deploy Branch' with 'master' selected.
1. Once the application has been built, click on the 'more' button at the top right of the page and click on 'Run Console'. With the console running, type the command `python3 manage.py migrate` to apply migrations to the Heroku Postgres database.
1. Following the migrate command, create a new superuser for the deployed app using `python3 manage.py createsuperuser` and follow the on-screen instructions.

You can migrate and create the superuser for the production database from the development enviroment by connecting to that specific database within your enviroment.

### Host and serve static files using Amazon's S3
#### Create an S3 bucket and set up bucket permissions
1. Navigate to `aws.amazon.com` and login.
1. Search for 'S3' in the search bar at the top of the page and click the 'S3' option.
1. On the next page, click 'Create Bucket' and then name the bucket and select the appropriate region. Under 'Block Public Access settings for this bucket', untick the 'Block all public access' option and click 'Create bucket' at the bottom of the page.
1. In the following 'buckets' page, click on the newly created bucket and in the 'properties' tab, navigate to the bottom of the page and click on 'Edit' under 'Static website hosting', setting the option to enable. Add some values to the 'Index Document' and 'Error Document' and saving the changes (these values can be any valid input as they are not used for this app).
1. Click on the 'Permissions' tab and scroll down to 'Cross-origin resource sharing (CORS)', click edit. Paste the following into the text field and click 'Save changes'

```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```

1. Still in the 'Permissions' tab, navigate to the 'Bucket policy' section and click on 'Edit'. Copy the 'Bucket ARN' from this page before clicking on the 'Policy generator' button.
1. In the policy generator, make the following changes:
    * Step 1: Select Policy Type
        * `'Select Type of Policy' : 'S3 Bucket Policy'`
    * Step 2: Add Statement(s)
        * `'Principal': '*'`
        * `'Actions': 'GetObject'`
        * `'Amazon Resource Name (ARN)':` Paste the ARN copied in step 8.
    * Click on 'Add Statement' and then 'Generate Policy'.
        * Copy the policy and paste it into the 'Edit Bucket Policy' input back on the main S3 bucket page.
        * Before saving, add `/*` to the 'Resource' attribute to allow access to all resources.
        `"Resource": "arn:aws:s3:::<your_bucket_name>/*"`
1. Within the 'Permissions' tab of the bucket, find the 'Access control list (ACL)' section and click on 'Edit'.
    * Next to 'Everyone (public access)', click on the 'list' checkbox before saving the changes.

#### Create a user to access the bucket
1. Navigate to the AWS Services menu and search for 'AIM', selecting the resulting IAM option.
1. Click on 'User Groups' in the menu on the left side of the page and then click 'Create group'.
1. Name the new group, giving it a name that relates to the S3 bucket created in the last section and then click 'Create group'.
1. Click on 'Policies' in the menu on the left side of the page and then click 'Create policy'.
1. Click on the 'JSON' tab and then click 'Import managed policy'. Search for 'S3' in the search bar and then click on the 'AmazonS3FullAccess' policy. Click 'Import' at the bottom of the page.
1. Find and copy the bucket ARN in the 'properties' section of the S3 buckets page.
1. Back in the 'JSON' tab on the 'Create policy' page, add the following to the resource section:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource":  [
                "arn:aws:s3:::<your bucket name>",
                "arn:aws:s3:::<your bucket name>/*"
            ]
        }
    ]
}
```

This allows access to both the bucket, and any files and folders within the bucket.

1. Click on the 'Tags' button at the bottom of the page and then the 'Next: Review' button before giving the policy a suitable name and description and clicking 'Create policy'.
1. Return to the 'User groups' by clicking the link in the menu on the left side of the page. Click on the 'Permissions' tab and then 'Add permissions'. In the 'Add permissions' dropdown, click 'Attach Policies' and select the policy created in the previous step before clicking 'Add permissions' at the bottom of the page.
1. On the 'Users' page found through the left side menu, click 'Add Users'. Give the user a name that relates to the bucket and click on 'Programmatic access' under the 'Access type' section before clicking 'Next: Permissions' at the bottom of the page.
1. Select the group created in step 3, click 'Next' and click 'Next' again on the 'Add tags (optional)' page, before clicking 'Create User'.
1. Click 'Download .csv' and ensure the downloaded file is saved as this file contains the access credentials required to use the S3 bucket. 

#### Configure Django to use S3 
1. Install the package `boto3` using `pip3 install boto3` in the terminal.
1. Install the package `django-storages` using `pip3 install django-storages`.
1. Add the packages to the `requirements.txt` file using `pip3 freeze > requirements.txt`.
1. Add `storages` to the `INSTALLED_APPS` list in `settings.py`
1. To ensure the S3 bucket is only used in production, the following `if` statement and additional settings should be added to `settings.py`:

    ```
        if 'USE_AWS' in os.environ:
        # Cache control
        AWS_S3_OBJECT_PARAMETERS = {
            'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
            'CacheControl': 'max-age=94608000',
        }

        # Bucket Config
        AWS_STORAGE_BUCKET_NAME = 'bucket-name'
        AWS_S3_REGION_NAME = 'eu-west-1'
        AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
        AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

        # Static and media files
        STATICFILES_STORAGE = 'custom_storages.StaticStorage'
        STATICFILES_LOCATION = 'static'
        DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
        MEDIAFILES_LOCATION = 'media'

        # Override static and media URLs in production
        STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
        MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
    ```

1. In the Heroku config vars in the app's settings page, add the following variables using the credentials found in the .csv file downloaded in a prior step: 
    ```
    USE_AWS: True
    AWS_ACCESS_KEY_ID: <YOUR AWS ACCES KEY>
    AWS_SECRET_ACCESS_KEY_ID: <YOUR SECRET ACCESS KEY>
    ```
1. Remove the `DISABLE_COLLECTSTATIC` variable from the config vars.
1. In the root directory of the Django app, add a file called `custom_storages.py` and insert the following code:
    ```
    from django.conf import settings
    from storages.backends.s3boto3 import S3Boto3Storage


    class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION


    class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
    ```
1. Add, commit and push changes to Gitpod:
1. If automatic deployment is not activated on Heroku, you will need to manually deploy. Heroku will collect static files and uplaod them to S3 Bucket.

### Sending emails
The application sends emails to users after the user completes several actions.

In development, emails are logged to the console. This is achieved with the following settings in `settings.py`:

    ```
    if 'DEVELOPMENT' in os.environ:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'amphii@example.com'
    ```

In production, emails are sent using a Gmail account which can be set up using the following process:

1. Create a Gmail account.
1. In the menu at the top right of the page click on 'Account'.
1. Click on 'Security' in the menu on the left of the page. On this page, ensure '2-step Verification' is turned on and then click on 'App passwords'.
1. Create a new app password in the 'App passwords' screen, selecting 'Mail' from the 'Select app' dropdown and giving the password a suitable name.
1. Click 'Generate' and copy the newly created app password.
1. Within the main email page, click on the icon in the top right of the page and then click 'See all settings'. Under the 'Forwarding and POP/IMAP' tab, ensure the 'Enable IMAP' setting is enabled in 'IMAP access'.
1. On Heroku and in the app's settings page, add the following variables to the 'Config vars':
    ```
    EMAIL_HOST_PASSWORD: <The Generated Password>
    EMAIL_HOST_USER: <The Gmail Address>
    ```
1. Back in the `settings.py` file in the Django app, add the following code in an `else` statement under the existing email settings:
    ```
    if 'DEVELOPMENT' in os.environ:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        DEFAULT_FROM_EMAIL = 'amphii@example.com'
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_USE_TLS = True
        EMAIL_PORT = 587
        EMAIL_HOST = 'smtp.gmail.com'
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
        DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')
    ```

9. Emails will now be sent to real email addresses when users interact with the app on Heroku, and emails will be logged to the console in development.

[Back to README](README.md)