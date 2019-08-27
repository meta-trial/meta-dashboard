from meta_rando.view_mixins import RandomizationListViewMixin
from edc_subject_dashboard.views import SubjectDashboardView


class DashboardView(RandomizationListViewMixin, SubjectDashboardView):

    consent_model = "meta_subject.subjectconsent"
    navbar_name = "meta_dashboard"
    navbar_selected_item = "consented_subject"
    visit_model = "meta_subject.subjectvisit"
