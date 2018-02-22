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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
#from webapp.utils.decorator_include import decorator_include
urlpatterns = [
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'duobeitong.html'}),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
 #   url(r'^admin/$', decorator_include(lonin_required,'webapp.utils')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
    url(r'^admin/$', 'webapp.tiku.views.index'),
    url(r'^admin/(\w+)/cha/$', 'webapp.tiku.views.cha'),
    url(r'^admin/(\w+)/add/$', 'webapp.tiku.views.luru'),
    url(r'^admin/people/$', 'webapp.tiku.views.people'),
    url(r'^admin/(\w+)/edit/(\d+)/$', 'webapp.tiku.views.luru'),
    url(r'^admin/(\w+)/(\w+)/user/$', 'webapp.tiku.views.user'),
    url(r'^admin/(\d+)/(\w+)/del/$', 'webapp.tiku.views.subject_del'),
    url(r'^admin/upload/(\d+)/(\w+)/$', 'webapp.tiku.views.upload'),
    url(r'^admin/upload_pic/(\d+)/(\w+)/$', 'webapp.tiku.views.upload_pic'),
    url(r'^admin/paper_add/$', 'webapp.tiku.views.paper_add'),
    url(r'^admin/paper/(\d+)/$', 'webapp.tiku.views.paper'),
    url(r'^admin/(\w+)/cha_paper/$', 'webapp.tiku.views.cha_paper'),
    url(r'^admin/interview_sces/$', 'webapp.tiku.views.interview_sces'),
    url(r'^admin/(\d+)/(\w+)/people_view/$', 'webapp.tiku.views.people_view'),
    url(r'^admin/time_text/$', 'webapp.tiku.views.time_text'),
    url(r'^admin/(\d+)/paper_people/$', 'webapp.tiku.views.paper_people'),
    url(r'^admin/student_index/$', 'webapp.tiku.views.student_index'),
    url(r'^admin/(\w+)/user_edit/$', 'webapp.tiku.views.user_edit'),
    
    url(r'^admin/create_paper/$', 'webapp.tiku.views.create_paper'),
    url(r'^admin/people_user/(\d+)/(\w+)/$', 'webapp.tiku.views.people_user'),
    url(r'^admin/add_people/(\d+)/(\w+)/$', 'webapp.tiku.views.add_people'),
    url(r'^admin/paper_status/$', 'webapp.tiku.views.paper_status'),
    url(r'^admin/paper_answer/(\d+)/$', 'webapp.tiku.views.paper_answer'),
    url(r'^admin/start_exam/$', 'webapp.tiku.views.start_exam'),
    url(r'^admin/student_paper/$', 'webapp.tiku.views.student_paper'),
    url(r'^admin/(\d+)/(\w+)/look_paper/$', 'webapp.tiku.views.look_paper'),
    url(r'^admin/paper_text/$', 'webapp.tiku.views.paper_text'),
    url(r'^admin/paper_answer_q/(\w+)/$', 'webapp.tiku.views.paper_answer_q'),
    url(r'^admin/paper_answer_q1/$', 'webapp.tiku.views.paper_answer_q1'),
    url(r'^admin/paper_answer_c/(\w+)/$', 'webapp.tiku.views.paper_answer_c'),
    url(r'^admin/paper_answer_j/(\w+)/$', 'webapp.tiku.views.paper_answer_j'),
    url(r'^admin/paper_answer_aq/(\w+)/$', 'webapp.tiku.views.paper_answer_aq'),
    url(r'^admin/Marking_paper/$', 'webapp.tiku.views.Marking_paper'),
    url(r'^admin/interview/$', 'webapp.tiku.views.interview'),
    url(r'^admin/interview_paper_answer/$', 'webapp.tiku.views.interview_paper_answer'),
    url(r'^admin/interview_paper_choose/(\w+)/$', 'webapp.tiku.views.interview_paper_choose'),
    url(r'^admin/interview_paper_text/(\w+)/$', 'webapp.tiku.views.interview_paper_text'),
    url(r'^admin/interview_paper/(\w+)/$', 'webapp.tiku.views.interview_paper'),
    url(r'^admin/interview_paper_nu/(\d+)/(\d)/$', 'webapp.tiku.views.interview_paper_nu'),
    url(r'^admin/(\w+)/student_paper_text/$', 'webapp.tiku.views.student_paper_text'),
    url(r'^admin/(\w+)/(\d+)/paper_edit/$', 'webapp.tiku.views.paper_edit'),
    url(r'^admin/(\d+)/(\d+)/(\d+)/(\w+)/interview_paper_edit/$', 'webapp.tiku.views.interview_paper_edit'),
    url(r'^admin/interview_paper_list/$', 'webapp.tiku.views.interview_paper_list'),
    url(r'^admin/interview_paper_mylist/$', 'webapp.tiku.views.interview_paper_mylist'),
    url(r'^admin/(\d+)/(\d+)/(\w+)/change_title/$', 'webapp.tiku.views.change_title'),
    url(r'^admin/(\d+)/(\d+)/(\d+)/(\w+)/interview_marking/$', 'webapp.tiku.views.interview_marking'),
    url(r'^admin/(\d+)/interview_del/$', 'webapp.tiku.views.interview_del'),
    url(r'^admin/(\w+)/(\d+)/fraction/$', 'webapp.tiku.views.fraction'),
    url(r'^admin/(\w+)/(\d+)/interview_fraction/$', 'webapp.tiku.views.interview_fraction'),
    url(r'^admin/ready_status/(\w+)/$', 'webapp.tiku.views.ready_status'),
    url(r'^admin/interview_paper_check/(\w+)/$', 'webapp.tiku.views.interview_paper_check'),
    url(r'^admin/interview_admin_paper/(\d+)/(\d+)/(\d+)/$', 'webapp.tiku.views.interview_admin_paper'),
    url(r'^admin/interview_add/(\d+)/(\d+)/$', 'webapp.tiku.views.interview_add'),
    url(r'^admin/interview_paper_luru/(\d+)/(\d+)/$', 'webapp.tiku.views.interview_paper_luru'),
    url(r'^admin/interview_create_paper/(\d+)/$', 'webapp.tiku.views.interview_create_paper'),
    url(r'^admin/interview_add_paper/(\d+)/$', 'webapp.tiku.views.interview_add_paper'),
    url(r'^admin/interview_deng/$', 'webapp.tiku.views.interview_deng'),
    url(r'^admin/(\d+)/fraction_view/$', 'webapp.tiku.views.fraction_view'),
    url(r'^admin/(\w+)/(\d+)/(\d+)/replace_id/$', 'webapp.tiku.views.replace_id'),
    url(r'^admin/(\w+)/(\d+)/(\d+)/interview_paper_add/$', 'webapp.tiku.views.interview_paper_add'),
    url(r'^admin/save_paper_answer/$', 'webapp.tiku.views.save_paper_answer'),
    url(r'^_admin/', include(admin.site.urls)),
]

urlpatterns += [
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':'/tmp/', 'show_indexes':True}),
]
