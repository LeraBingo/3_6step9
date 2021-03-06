import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en")



@pytest.fixture(scope='session')
def browser(request):
    lang_value = request.config.option.language

    if lang_value is None:
        lang_value = 'en'    #default language. if no language has been entered
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang_value})
    browser = webdriver.Chrome(options=options)
    yield browser            #here the test_items.py code will be executed
    browser.quit()
