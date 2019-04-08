from django.urls import path
from . import views

urlpatterns = {
    path('getRequest/post', views.choose_method),
    path('APItest/upload', views.save_excel),
    path('APItest/runTest', views.run_api_test),
    path('APItest/delete_file_by_name', views.handle_remove),
    path('Case/buildData', views.build_case),
    path('Case/download', views.download_case),
    path('Case/upload', views.upload_case_to_zt),
    path('DBcheck/upload', views.save_DDL),
    path('DBcheck/returnContent', views.upload_DDL),
    path('DBcheck/resole', views.resole_DDL),
    path('charts/getMonthBugNum', views.get_month_bug_num),
    path('charts/getBugStyle', views.get_bug_style),
    path('card/setData', views.get_bug_module)
}
