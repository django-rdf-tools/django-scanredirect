#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import patterns, include

urlpatterns = patterns('',

    (r'main.php$', 'scanredirect.views.back_home'),
    (r'index.php$', 'scanredirect.views.back_home'),

    (r'phpMyAdmin', 'scanredirect.views.back_home'),
    (r'phpMyAdmin', 'scanredirect.views.back_home'),
    (r'phpmyadmin', 'scanredirect.views.back_home'),
    (r'phpadmin', 'scanredirect.views.back_home'),
    (r'php-myadmin', 'scanredirect.views.back_home'),
    (r'php-my-admin', 'scanredirect.views.back_home'),

    (r'^admin/phpmanager/', 'scanredirect.views.back_home'),
    (r'^admin/pma2005/', 'scanredirect.views.back_home'),
    (r'^admin/PMA2005/', 'scanredirect.views.back_home'),
    (r'^admin/pma2006/', 'scanredirect.views.back_home'),
    (r'^admin/PMA2006/', 'scanredirect.views.back_home'),
    (r'^admin/p/m/a/', 'scanredirect.views.back_home'),
    (r'^admin/modules/', 'scanredirect.views.back_home'),
    (r'^admin/pMA/', 'scanredirect.views.back_home'),
    (r'^admin/pma/', 'scanredirect.views.back_home'),
    (r'^admin/web/', 'scanredirect.views.back_home'),
    (r'^admin/db/', 'scanredirect.views.back_home'),


    (r'sqladmin/', 'scanredirect.views.back_home'),
    (r'sysadmin/', 'scanredirect.views.back_home'),
    (r'mysqladmin/', 'scanredirect.views.back_home'),
    (r'mysql-admin/', 'scanredirect.views.back_home'),
    (r'mysql/', 'scanredirect.views.back_home'),
    (r'sqlmanager/', 'scanredirect.views.back_home'),
    (r'mysqlmanager/', 'scanredirect.views.back_home'),
    (r'sqlweb/', 'scanredirect.views.back_home'),
    (r'webdb/', 'scanredirect.views.back_home'),
    (r'websql/', 'scanredirect.views.back_home'),
    (r'webadmin/', 'scanredirect.views.back_home'),
    (r'myadmin/', 'scanredirect.views.back_home'),
    (r'dbadmin/', 'scanredirect.views.back_home'),

    (r'^db/', 'scanredirect.views.back_home'),
    (r'^database/', 'scanredirect.views.back_home'),
    (r'^components/', 'scanredirect.views.back_home'),
    (r'^administrator/', 'scanredirect.views.back_home'),
    (r'^xampplite/', 'scanredirect.views.back_home'),
    (r'^xampp/', 'scanredirect.views.back_home'),
    (r'^MyAdmin/', 'scanredirect.views.back_home'),

)

