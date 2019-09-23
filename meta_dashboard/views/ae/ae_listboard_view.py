from edc_adverse_event.view_mixins import AeListboardViewMixin
from meta_ae.pdf_reports import AeReport


class AeListboardView(AeListboardViewMixin):
    navbar_name = "meta_dashboard"
    listboard_back_url = "meta_dashboard:ae_home_url"
    ae_report_cls = AeReport
