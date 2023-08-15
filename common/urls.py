from django.urls import path
from common.views import CommonIndexView, ImportFile, SummaryView

app_name = 'common'


urlpatterns = [
    path('common/',CommonIndexView.as_view(), name='index'),
    path('',ImportFile.as_view(), name='import_file'),
    path('summary/',SummaryView.as_view(), name='summary')
]