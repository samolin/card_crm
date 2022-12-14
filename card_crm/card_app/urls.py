from django.urls import path

from card_app import views 


urlpatterns = [
    path('', views.index, name='home'),
    path('changestatus/<int:pk>', views.change_status, name='changestatus'),
    path('deletecard/<int:pk>', views.delete_card, name='deletecard'),
    path('generate-card', views.generate_card, name='generate-card'),
]