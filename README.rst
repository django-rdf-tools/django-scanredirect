django-scanredirect
===================

A little Django app thats adds URL rules to redirect scripts looking for webapps exploits to their own IP

Add `scanredirect` (with an underscore) to INSTALLED_APPS in your django project settings.

Add the following line at the top of your project's urls.py file::
        (r'^', include('scanredirect.urls')),

