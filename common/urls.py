from django.urls import path
from common.views import CommonIndexView

app_name = 'common'


urlpatterns = [
    path('common/',CommonIndexView.as_view(), name='index')
]