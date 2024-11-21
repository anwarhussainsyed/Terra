from django.urls import path
from . import views
urlpatterns=[
      path("",views.home,name="home"),
      path('login/',views.login_page,name='login'),
      path('register/',views.signup,name='register'),
      path('management/',views.management,name='management'),
      path('logout/',views.logout_page,name='logout'),
      path('createblog/',views.submit,name='submit'),
      path('blogs/',views.blogs_page,name="blog"),
      path('delete/<str:pk>',views.delete_order,name='delete'),
      path('deleteblog/<str:pk>',views.delete_blog,name='deleteblog'),
      path('contact/',views.contact,name='contact'),
      path('cloud/',views.cloudcomputing,name='cloud'),
      path('devops/',views.devops,name='devops'),
      path('code/',views.coding,name='coding'),
      path('web/',views.webtechnology,name='web'),
      path('cyber/',views.cybersecurity,name='cyber'),
      path('datascience/',views.datascience,name='data'),
       path('viewuser/<str:pk>',views.customer,name='viewuser'),
       path('profile<str:pk>/',views.profile,name='viewuser'),
]