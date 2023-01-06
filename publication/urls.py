from django.urls import path
from . import views

urlpatterns = [
    path('', views.PublicaionsView.as_view(), name='publication'),
    path('add_publication/', views.PublicaionAddView.as_view(), name='add_publication'),
    path('publication/<int:id>/', views.PublicationDetailView.as_view(), name='publication_detail'),
    path('publication/<int:id>/delete/', views.PublicationDeleteView.as_view(), name='delete_publication'),
    path('publication/<int:id>/update/', views.PublicationUpdateView.as_view(), name='update_publication'),
]