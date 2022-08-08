
from django.urls import path
from . import views


app_name='backsite'
urlpatterns=[
    path('',views.landing),
    path('brand/',views.brandApi),
    path('brand/<int:pk>/',views.brandApi),
    path('brand/<int:bk>/model/',views.modelApi),
    path('brand/<int:bk>/model/<int:mk>/',views.modelApi),
    path('brand/<int:bk>/model/<int:mk>/bike/',views.bikeApi),
    path('brand/<int:bk>/model/<int:mk>/bike/<int:bbk>/',views.bikeApi),
    path('savefile/',views.savefile),
]
