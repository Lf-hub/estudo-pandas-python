from django.urls import path
from common.views import CommonIndexView, ImportFile, SummaryView, SummaryDetail, PlaygameView

app_name = 'common'


urlpatterns = [
    path('common/',CommonIndexView.as_view(), name='index'),
    path('',ImportFile.as_view(), name='import_file'),
    path('summary/',SummaryView.as_view(), name='summary'),
    path('detail/',SummaryDetail.as_view(), name='summary_detail'),
    path('playgame/',PlaygameView.as_view(), name='playgame'),
]