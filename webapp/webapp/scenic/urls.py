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

#景区
url(r'^$','webapp.scenic.views.index'),
url(r'^(\d+)/$','webapp.scenic.views.index'),
url(r'^dev/$','webapp.scenic.views.dev'),
url(r'^(\w+)/dev/$','webapp.scenic.views.dev'),
url(r'^(\d+)/num/$','webapp.scenic.views.num'),
url(r'^(\d+)/(\d+)/details/$','webapp.scenic.views.details'),
url(r'^(\d+)/(\d+)/export/$','webapp.scenic.views.export'),
url(r'^(\d+)/(\d+)/region_modify/$','webapp.scenic.views.region_modify'),
url(r'^(\d+)/(\d+)/region_del/$','webapp.scenic.views.region_del'),
url(r'^text/$','webapp.scenic.views.text'),
url(r'^(\d+)/text_del/$','webapp.scenic.views.text_del'),
url(r'^(\d+)/text_content/$','webapp.scenic.views.text_content'),
url(r'^(\d+)/content_add/$','webapp.scenic.views.content_add'),
url(r'^(\d+)/content_edit/$','webapp.scenic.views.content_edit'),
url(r'^(\d+)/content_del/$','webapp.scenic.views.content_del'),
url(r'^real_time/$','webapp.scenic.views.real_time'),
url(r'^commodity/$','webapp.scenic.views.commodity'),
url(r'^commodity/ajax/(\d+)/$','webapp.scenic.views.commodity_ajax'),
url(r'^order/$','webapp.scenic.views.order'),
url(r'^commodity/add_sales/(\d+)/$','webapp.scenic.views.add_sales'),
url(r'^commodity/edit_sales/(\d+)/(\d+)/$','webapp.scenic.views.add_sales'),
url(r'^commodity/add_sales/ajax/(\d+)/$','webapp.scenic.views.add_sales_ajax'),
url(r'^commodity/edit_sales/ajax/(\d+)/(\d+)/$','webapp.scenic.views.add_sales_ajax'),
url(r'^commodity/down_sales/ajax/$','webapp.scenic.views.down_sales_ajax'),
url(r'^commodity/up_sales/ajax/$','webapp.scenic.views.up_sales_ajax'),
url(r'^commodity/delete_sales/ajax/$','webapp.scenic.views.delete_sales_ajax'),
url(r'^commodity/add_group/ajax/(\d+)/$','webapp.scenic.views.add_group_ajax'),
url(r'^commodity/edit_group/ajax/(\d+)/$','webapp.scenic.views.add_group_ajax'),
url(r'^commodity/delete_group/ajax/(\d+)/$','webapp.scenic.views.del_group_ajax'),


#统计表探针终端
url(r'^tanzclient/$','webapp.scenic.views.tclient'),
url(r'^tanz/$','webapp.scenic.views.tanz'),

#探针数据
url(r'^probe/$','webapp.scenic.views.probe'),
#认证
url(r'^kaitong/$','webapp.scenic.views.kaitong'),
url(r'^weikaitong/$','webapp.scenic.views.weikaitong'),

#门店
url(r'^ifkaitong/$','webapp.scenic.views.ifkaitong'),
url(r'^mendianinfo/$','webapp.scenic.views.mendianxinxi'),
url(r'^mendianinfo2/$','webapp.scenic.views.mendianxinxi2'),
url(r'^set_success/$','webapp.scenic.views.set_success'),
url(r'^setting/$','webapp.scenic.views.setting'),
url(r'^shop_index/$','webapp.scenic.views.shop_index'),
url(r'^temlist/$','webapp.scenic.views.temlist'),
url(r'^tembind/$','webapp.scenic.views.tembind'),



]
