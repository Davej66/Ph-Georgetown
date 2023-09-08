from django.urls import path 
from . import views

urlpatterns = [
    path('', views.indexa, name='indexa'),
    path('bookinga', views.bookinga, name='bookinga'),
    path('booking-submita', views.bookingSubmit, name='bookingSubmita'),
    path('user-panel', views.userPanel, name='userPanel'),
    path('user-update/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submita/<int:id>', views.userUpdateSubmita, name='userUpdateSubmita'),
    path('staff-panela', views.staffPanel, name='staffPanela'),
]
