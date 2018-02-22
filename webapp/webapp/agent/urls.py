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

#代理商
url(r'^$','webapp.agent.views.index'),
url(r'^(\w+)/agent/$','webapp.agent.views.agent'),
url(r'^agent/$','webapp.agent.views.agent'),
url(r'^(\w+)/dev/$','webapp.agent.views.dev'),
url(r'^dev/$','webapp.agent.views.dev'),
url(r'^(\d+)/add/$','webapp.agent.views.scenic_add'),
url(r'^(\d+)/user/$','webapp.agent.views.scenic_user'),
url(r'^(\d+)/username/$','webapp.agent.views.scenic_username'),
url(r'^(\d+)/(\d+)/user_del/$','webapp.agent.views.user_del'),
url(r'^(\d+)/(\d+)/edit/$','webapp.agent.views.scenic_add'),
url(r'^(\d+)/del/$','webapp.agent.views.scenic_del'),
url(r'^(\d+)/dev_add/$','webapp.agent.views.dev_add'),
url(r'^(\d+)/(\d+)/dev_add/$','webapp.agent.views.dev_add'),

url(r'^(\d+)/region/$','webapp.agent.views.region'),
url(r'^(\d+)/label/$','webapp.agent.views.label'),
url(r'^(\d+)/dellabel/$','webapp.agent.views.dellabel'),
url(r'^(\d+)/area/$','webapp.agent.views.area'),
url(r'^(\d+)/arealabel/$','webapp.agent.views.arealabel'),
url(r'^(\d+)/delarea/$','webapp.agent.views.delarea'),
url(r'^(\d+)/point_add/$','webapp.agent.views.area_manage'),
url(r'^(\d+)/point_name/$','webapp.agent.views.point_name'),
url(r'^(\d+)/scenic_map/$','webapp.agent.views.scenic_mapp'),
url(r'^(\d+)/(\d+)/agent_map/$','webapp.agent.views.agent_map'),
url(r'^(\d+)/add_map/$','webapp.agent.views.scenic_map'),

url(r'^(\d+)/save_dev/$','webapp.agent.views.save_dev'),
url(r'^(\d+)/(\d+)/export/$','webapp.agent.views.export'),
url(r'^(\d+)/(\d+)/scenic_export/$','webapp.agent.views.scenic_export'),
url(r'^(\d+)/import/$','webapp.agent.views.dev_import'),
url(r'^(\d+)/(\d+)/dev_edit/$','webapp.agent.views.dev_edit'),
url(r'^(\d+)/dev_del/$','webapp.agent.views.dev_del'),
url(r'^(\d+)/(\d+)/(\w+)/su/$','webapp.agent.views.su'),
url(r'^(\d+)/scenic_d/$','webapp.agent.views.scenic_d'),
url(r'^(\d+)/setting/$','webapp.agent.views.scenic_setting'),


url(r'^(\d+)/(\w+)/dev_latiude/$','webapp.agent.views.dev_latiude'),
url(r'^(\d+)/dev_lng/$','webapp.agent.views.dev_lng'),

]
