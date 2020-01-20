from django.urls import path
from .views import EntryList, EntryDetail

urlpatterns = [
	path('', EntryList.as_view(), name = 'home'),
	path('detail/<int:pk>/', EntryDetail.as_view(), name = 'detail'),
]