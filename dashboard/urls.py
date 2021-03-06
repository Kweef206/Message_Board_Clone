from django.urls import path
from . import views
urlpatterns = [
    # localhost8000/posts/
    path('', views.dashboard, name="dashboard"),
    # localhost:8000/posts/<post_id>/delete
    path('<int:post_id>/delete', views.delete, name="delete"),
    path('post_message', views.post_mess, name="post_mess"),
    path('add_comment/<int:id>', views.post_comment, name="post_comment"),
    path('like/<int:id>', views.add_like, name="add_like"),
    path('delete/<int:id>', views.delete_comment, name="delete_comment"),
    path('user_profile/<int:id>', views.profile, name="view_profile"),
    path('edit/<int:id>', views.edit, name="edit"),

]


"{% url 'post_mess' %}"