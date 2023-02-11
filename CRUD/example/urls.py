from django.urls import path
from django.urls.conf import include
from example import views
urlpatterns = [
    path('emp', views.emp),
    path('', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
    path('show', views.show),
]