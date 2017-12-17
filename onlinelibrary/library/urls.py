from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.index,name='index'),
    url(r'^mainpage/', views.mainpage,name='mainpage'),
    url(r'^signup/', views.signup,name='signup'),
    url(r'^add_user/', views.add_user,name='add_user'),
    url(r'^login/', views.login,name='login'),
    url(r'^login_new/', views.login_new,name='login_new'),
    url(r'^logout/', views.logout,name='logout'),
    url(r'^tech/', views.tech,name='tech'),
    url(r'^non_tech/', views.non_tech,name='non_tech'),
    url(r'^mech/', views.mech,name='mech'),
    url(r'^tech_book/(?P<Book_id>[0-9]+)/$',views.tech_book_details,name='tech_book_details'),
    url(r'^non_tech_book/(?P<Book_id>[0-9]+)/$',views.non_tech_book_details,name='non_tech_book_details'),
    url(r'^comp/', views.comp,name='comp'),
    url(r'^entc/', views.entc,name='entc'),
    url(r'^fiction/', views.fiction,name='fiction'),
    url(r'^non_fiction/', views.non_fiction,name='non_fiction'),
    url(r'^magazines/', views.magazines,name='magazines'),
    url(r'^users/(?P<User_name>[a-zA-z0-9]+)/$',views.user_details,name='user_details'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^analysis/$',views.analysis,name='analysis'),


    url(r'^add_book_tech/', views.add_book_tech,name='add_book_tech'),
    url(r'^add_book_non_tech/', views.add_book_non_tech,name='add_book_non_tech'),
    url(r'^add_tech/', views.add_tech,name='add_tech'),
    url(r'^add_non_tech/', views.add_non_tech,name='add_non_tech'),

    url(r'^delete_book_tech/', views.delete_book_tech,name='delete_book_tech'),
    url(r'^delete_book_non_tech/', views.delete_book_non_tech,name='delete_book_non_tech'),
    url(r'^delete_tech/', views.delete_tech,name='delete_tech'),
    url(r'^delete_non_tech/', views.delete_non_tech,name='delete_non_tech'),
    url(r'^search/tech/(?P<Book_id>[0-9]+)/$', views.tech_search,name='tech_search'),
    url(r'^search/', views.search,name='search'),
    url(r'^search_non/(?P<Book_id>[0-9]+)/$', views.non_tech_search,name='non_tech_search'),


]
