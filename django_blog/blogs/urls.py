# @Time    : 18-6-5 下午2:19
# @Author  : wengwenyu
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from .views import index,lists,Search,detail

urlpatterns = [
    url(r'^index/$', index, name='index'),
    url(r'^list/$', lists, name='list'),
    url(r'^search/$', Search.as_view(), name='search'),
    url(r'^tags/(?P<tid>[0-9]+)/$', lists, name='tags'),
    url(r'^category/(?P<cid>[0-9]+)/$', lists, name='category'),
    url(r'^detail/(\d)+/$', detail, name='detail'),
]
