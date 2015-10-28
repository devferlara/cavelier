from django.conf.urls import include, url, patterns
from .views import main

urlpatterns = patterns ('',
	url(r'^inicio/', 'general.views.main'),
)

