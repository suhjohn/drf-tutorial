from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from ..views.cbv import SnippetList, SnippetDetail, UserList, UserDetail

urlpatterns = [
    url(r'^$', SnippetList.as_view(), name='snippet_list'),
    url(r'^(?P<pk>\d+)/$', SnippetDetail.as_view(), name='snippet_detail'),
    url(r'^users/$', UserList.as_view(), name='user_list'),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(), name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
