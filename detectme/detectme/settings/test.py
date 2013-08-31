from base import *

########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
########## IN-MEMORY TEST DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

INSTALLED_APPS += (
    'django_jenkins',
)

#For the report explanation refer to: https://github.com/kmmbvnr/django-jenkins

JENKINS_TASKS = (
    'django_jenkins.tasks.with_coverage',  # produces XML coverage report for Jenkins
    'django_jenkins.tasks.django_tests',  # discovers standard Django test suite from test.py files
    'django_jenkins.tasks.dir_tests',  # discover tests from all test*.py files in app subdirectories
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    # 'django_jenkins.tasks.run_jshint',
    # 'django_jenkins.tasks.run_csslint',  # runs CSS lint tools over app/static/*/*.css files. Creates CSS Lint compatible report for Jenkins     
    # 'django_jenkins.tasks.run_sloccount',    
    # 'django_jenkins.tasks.lettuce_tests',
)

