#!/usr/bin/env python
import django
import logging
import os
import sys

from django.conf import settings
from django.test.runner import DiscoverRunner
from edc_test_utils import DefaultTestSettings
from os.path import abspath, dirname, join


app_name = 'meta_dashboard'
base_dir = dirname(abspath(__file__))

DEFAULT_SETTINGS = DefaultTestSettings(
    calling_file=__file__,
    APP_NAME=app_name,
    BASE_DIR=base_dir,
    COUNTRY="tanzania",
    SITE_ID=10,
    ETC_DIR=os.path.join(base_dir, app_name, "tests", "etc"),
    EDC_BOOTSTRAP=3,
    ADVERSE_EVENT_ADMIN_SITE="meta_ae_admin",
    ADVERSE_EVENT_APP_LABEL="meta_ae",
    SUBJECT_VISIT_MODEL="meta_subject.subjectvisit",
    SUBJECT_REQUISITION_MODEL="meta_subject.subjectrequisition",
    SUBJECT_CONSENT_MODEL='meta_consent.subjectconsent',
    RANDOMIZATION_LIST_PATH=join(
        base_dir, app_name, "tests", "etc", "randomization_list.csv"),
    INSTALLED_APPS=[
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.messages",
        "django.contrib.sessions",
        "django.contrib.sites",
        "django.contrib.staticfiles",
        "django_crypto_fields.apps.AppConfig",
        "django_revision.apps.AppConfig",
        "edc_action_item.apps.AppConfig",
        "edc_adverse_event.apps.AppConfig",
        "edc_auth.apps.AppConfig",
        "edc_consent.apps.AppConfig",
        "edc_dashboard.apps.AppConfig",
        "edc_device.apps.AppConfig",
        "edc_lab.apps.AppConfig",
        "edc_lab_dashboard.apps.AppConfig",
        "edc_locator.apps.AppConfig",
        "edc_metadata_rules.apps.AppConfig",
        "edc_model_wrapper.apps.AppConfig",
        "edc_navbar.apps.AppConfig",
        "edc_notification.apps.AppConfig",
        "edc_offstudy.apps.AppConfig",
        "edc_pharmacy.apps.AppConfig",
        "edc_pharmacy_dashboard.apps.AppConfig",
        "edc_randomization.apps.AppConfig",
        "edc_reference.apps.AppConfig",
        "edc_registration.apps.AppConfig",
        "edc_review_dashboard.apps.AppConfig",
        "edc_sites.apps.AppConfig",
        "edc_subject_dashboard.apps.AppConfig",
        "edc_timepoint.apps.AppConfig",
        "edc_visit_schedule.apps.AppConfig",
        "meta_ae.apps.AppConfig",
        "meta_labs.apps.AppConfig",
        "meta_lists.apps.AppConfig",
        "meta_prn.apps.AppConfig",
        # "meta_rando.apps.AppConfig",
        "meta_reference.apps.AppConfig",
        "meta_screening.apps.AppConfig",
        "meta_consent.apps.AppConfig",
        "meta_sites.apps.AppConfig",
        "meta_subject.apps.AppConfig",
        "meta_visit_schedule.apps.AppConfig",
        "meta_dashboard.apps.EdcProtocolAppConfig",
        "meta_dashboard.apps.EdcAppointmentAppConfig",
        "meta_dashboard.apps.EdcFacilityAppConfig",
        "meta_dashboard.apps.EdcIdentifierAppConfig",
        "meta_dashboard.apps.EdcMetadataAppConfig",
        "meta_dashboard.apps.EdcVisitTrackingAppConfig",
        "meta_dashboard.apps.AppConfig",
    ],
    add_dashboard_middleware=True,
    add_lab_dashboard_middleware=True,
    use_test_urls=True,
).settings


def main():
    if not settings.configured:
        settings.configure(**DEFAULT_SETTINGS)
    django.setup()
    tags = [t.split('=')[1] for t in sys.argv if t.startswith('--tag')]
    failures = DiscoverRunner(failfast=True, tags=tags).run_tests(
        [f'{app_name}.tests'])
    sys.exit(failures)


if __name__ == "__main__":
    logging.basicConfig()
    main()
