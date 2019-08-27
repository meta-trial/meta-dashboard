from edc_navbar import NavbarItem, site_navbars, Navbar
from edc_review_dashboard.navbars import navbar_item as review_navbar_item


no_url_namespace = False  # True if settings.APP_NAME == "meta_dashboard" else False

navbar = Navbar(name="meta_dashboard")

navbar.append_item(
    NavbarItem(
        name="screened_subject",
        title="Screening",
        label="Screening",
        fa_icon="fas fa-user-plus",
        codename="edc_navbar.nav_screening_section",
        url_name="screening_listboard_url",
        no_url_namespace=no_url_namespace,
    )
)

navbar.append_item(
    NavbarItem(
        name="consented_subject",
        title="Subjects",
        label="Subjects",
        fa_icon="far fa-user-circle",
        codename="edc_navbar.nav_subject_section",
        url_name="subject_listboard_url",
        no_url_namespace=no_url_namespace,
    )
)

navbar.append_item(review_navbar_item)

navbar.append_item(
    NavbarItem(
        name="ae_home",
        label="AE",
        title="Adverse Events",
        codename="edc_navbar.nav_ae_section",
        url_name="meta_dashboard:ae_home_url",
        no_url_namespace=no_url_namespace,
    )
)

navbar.append_item(
    NavbarItem(
        name="data_manager_home",
        title="Data Management",
        label="DM",
        codename="edc_navbar.nav_data_manager_section",
        url_name="meta_dashboard:dm_home_url",
    )
)


site_navbars.register(navbar)
