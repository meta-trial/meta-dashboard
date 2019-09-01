from django.apps import apps as django_apps
from django.urls.conf import path

from .views import (
    AeHomeView,
    AeListboardView,
    DataManagerHomeView,
    DeathReportListboardView,
    ScreeningListboardView,
    SubjectDashboardView,
    SubjectListboardView,
    SubjectReviewListboardView,
)


app_name = "meta_dashboard"

urlpatterns = []

subject_identifier_pattern = django_apps.get_app_config(
    "edc_identifier"
).subject_identifier_pattern

screening_identifier_pattern = django_apps.get_app_config(
    "edc_identifier"
).screening_identifier_pattern


urlpatterns = [
    path("ae/", AeHomeView.as_view(), name="ae_home_url"),
    path("dm/", DataManagerHomeView.as_view(), name="dm_home_url"),
]

urlpatterns += SubjectListboardView.urls(
    namespace=app_name,
    label="subject_listboard",
    identifier_pattern=subject_identifier_pattern,
)
urlpatterns += ScreeningListboardView.urls(
    namespace=app_name,
    label="screening_listboard",
    identifier_label="screening_identifier",
    identifier_pattern=screening_identifier_pattern,
)
urlpatterns += SubjectDashboardView.urls(
    namespace=app_name,
    label="subject_dashboard",
    identifier_pattern=subject_identifier_pattern,
)


urlpatterns += SubjectReviewListboardView.urls(
    namespace=app_name,
    label="subject_review_listboard",
    identifier_pattern=subject_identifier_pattern,
)
urlpatterns += AeListboardView.urls(
    namespace=app_name,
    label="ae_listboard",
    identifier_pattern=subject_identifier_pattern,
)
urlpatterns += DeathReportListboardView.urls(
    namespace=app_name,
    label="death_report_listboard",
    identifier_pattern=subject_identifier_pattern,
)
