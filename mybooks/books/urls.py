from django.conf.urls import url

from . import views


urlpatterns = [

    url(regex=r'^$',
        view=views.BookListView.as_view(),
        name='book_list'),

    url(regex=r'^(?P<pk>[0-9]+)/$',
        view=views.BookDetailView.as_view(),
        name='book_detail')
]
