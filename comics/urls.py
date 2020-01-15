from django.urls import path
from .views import EntryList, EntryDetail

urlpatterns = [
	path('post/<int:pk>/', EntryDetail.as_view(), name = 'post_detail'),
	path('', EntryList.as_view(), name = 'home'),
]