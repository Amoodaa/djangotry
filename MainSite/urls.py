from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Mainsite import views
# ... your normal urlpatterns here

urlpatterns = [
    path('', views.index),
    path('article/<int:id>', views.articleView),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
