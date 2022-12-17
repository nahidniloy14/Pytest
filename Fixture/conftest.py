import pytest
driver=None #for ss properties
@pytest.fixture()
#@pytest.fixture(scope="class")  # will be executed in the class level
def setup():
    global driver  # should intialize this in the main fixture to take ss
    print("I am header")
    yield  # will wait until the header gets printed and then after it will to start working with the footer
    print("I am footer")


#used in dataDrivenFixture.py
def dataLoad():
    print("User Created")
    return ("name", "age", "gmail")

#used in multiple dataset.py
@pytest.fixture(params=["chrome","firefox","brave"])
#@pytest.fixture(params=[("chrome","1200"),("firefox","None","1300"),"brave"])
def browser(request):
    return request.param

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)


# conftest will be available to all fixture  related Tests
