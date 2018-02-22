#coding:utf-8
"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

urlpatterns = [

#总部
url(r'^$','webapp.headquar.views.index'),
url(r'^(\w+)/agent/$','webapp.headquar.views.agent'),
url(r'^agent/$','webapp.headquar.views.agent'),
url(r'^dev/$','webapp.headquar.views.dev'),
url(r'^scenic/$','webapp.headquar.views.scenic_manage'),
url(r'^scenic_add/$','webapp.headquar.views.scenic_add'),
url(r'^(\d+)/scenic_edit/$','webapp.headquar.views.scenic_edit'),
url(r'^(\d+)/scenic_delete/$','webapp.headquar.views.scenic_delete'),
url(r'^(\w+)/dev/$','webapp.headquar.views.dev'),
url(r'^add/$','webapp.headquar.views.add_agent'),
url(r'^(\d+)/edit/$','webapp.headquar.views.add_agent'),
url(r'^(\d+)/del/$','webapp.headquar.views.agent_del'),
url(r'^(\d+)/user/$','webapp.headquar.views.agent_user'),
url(r'^(\d+)/username/$','webapp.headquar.views.agent_username'),
url(r'^(\d+)/(\d+)/user_del/$','webapp.headquar.views.user_del'),
url(r'^(\d+)/export/$','webapp.headquar.views.export'),
url(r'^(\d+)/agent_export/$','webapp.headquar.views.agent_export'),
]
