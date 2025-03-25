import sys , os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from keywords.browser_setup import BrowserSetup
from keywords.login_keyword import LoginPage
from resources.testdata.testdata import TestData
from resources.config.config_web import Config
from tests.auto_generate_report import run_tests