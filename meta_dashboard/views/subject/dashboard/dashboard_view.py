from edc_subject_dashboard.views import SubjectDashboardView


class DashboardView(SubjectDashboardView):

    consent_model = "meta_consent.subjectconsent"
    navbar_name = "meta_dashboard"
    navbar_selected_item = "consented_subject"
    visit_model = "meta_subject.subjectvisit"
