Spike Solution - Facebook Integration with Django

Installation
---

- Install the required Python packages from the requirements.txt file
- Create a local.py file in the settings directory with at least the following fields

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG
    SECRET_KEY = [Insert your project SECRET_KEY here] 
    FACEBOOK_APP_ID = [Insert your Facebook App ID here]
    FACEBOOK_APP_SECRET = [Insert your Facebook App Secret here]
    SITE_URL = [Insert the URL of the running site here without the trailing slash]
    
- Facebook only allows authentications from the domain registered in the app settings (no localhost), so edit your hosts file and add an alias for localhost. For example, map demo.pichanguea.com to localhost so that you can access your app at http://demo.pichanguea.com:8000

- Run manage.py syncdb

- Access the site using the domain you registered

Test Running
---

- For the Selenium test to run you must have Chrome and ChromeDriver installed in your computer, in particular for Linux "/usr/bin/google-chrome" must be a symbolic link to the binary and the ChromeDirver executable must be in your PATH.

- Run the tests with

    python manage.py test spike

