from django.apps import apps as django_apps
from django.urls.conf import path
from edc_adverse_event.views import (
    ClosedTmgAeListboardView,
    NewTmgAeListboardView,
    OpenTmgAeListboardView,
    DeathListboardView as TmgDeathListboardView,
    SummaryListboardView as TmgSummaryListboardView,
)

from edc_data_manager.views import HomeView as DataManagerHomeView
from edc_review_dashboard.views import SubjectReviewListboardView

from .patterns import screening_identifier
from .views import (
    AeListboardView,
    DeathReportListboardView,
    ScreeningListboardView,
    SubjectDashboardView,
    SubjectListboardView,
)

app_name = "meta_dashboard"

subject_identifier_pattern = django_apps.get_app_config(
    "edc_identifier"
).subject_identifier_pattern  # "092\-[0-9\-]+"


urlpatterns = [
    # path("tmg/", TmgHomeView.as_view(), name="tmg_home_url"),
    # path("ae/", AeHomeView.as_view(), name="ae_home_url"),
    path("dm/", DataManagerHomeView.as_view(), name="dm_home_url")
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
    identifier_pattern=screening_identifier,
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
