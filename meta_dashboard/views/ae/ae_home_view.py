from edc_adverse_event.views import HomeView


class AeHomeView(HomeView):

    navbar_name = "meta_dashboard"
    navbar_selected_item = "ae_home"
