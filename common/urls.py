from django.urls import path
from common.views import CommonIndexView, ImportFile

app_name = 'common'


urlpatterns = [
    path('common/',CommonIndexView.as_view(), name='index'),
    path('',ImportFile.as_view(), name='import_file')
]