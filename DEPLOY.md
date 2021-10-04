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

[Back to README](README.md)