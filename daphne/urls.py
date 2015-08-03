from django.conf.urls import include, url
from api import router
urlpatterns = [
    # url(r'', 'daphne.views.react_playground'),
    url(r'', 'daphne.views.test')
]
