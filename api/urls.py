from django.urls import path
from . import views

urlpatterns = [
    path('notes/',views.getNotes),
    path('notes/<int:id>',views.getNote),
    path('notes/add',views.addNote),
    path('notes/update/<int:id>',views.updateNote),
    path('notes/delete/<int:id>',views.deleteNote),
    
    #image urls
    #path('notes/<int:id>/upload_image',views.uploadImage),
    
]
