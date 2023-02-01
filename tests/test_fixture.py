import pytest
from selene.support.shared import browser


@pytest.fixture(params=[pytest.param('1300*1000', '390*844', '1900*1200')])
def size_web(request):
    if request.param == '1300*1000':
        browser.config.window_width = 1300
        browser.config.window_height = 1000
        pass
    else:
        pytest.skip('Неверный размер окна браузера')


@pytest.mark.parametrize('size_web', ['1300*1000', '390*844', '1900*1200'], ids=['Desktop', 'Mobile', 'Large Desktop'], indirect=True)
def test_desktop(size_web):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.quit()


@pytest.fixture(params=[pytest.param('1300*1000', '390*844', '1900*1200')])
def size_mobil(request):
    if request.param == '390*844':
        browser.config.window_width = 390
        browser.config.window_height = 844
        pass
    else:
        pytest.skip('Неверный размер окна браузера')


@pytest.mark.parametrize('size_mobil', ['1300*1000', '390*844', '1900*1200'], ids=['Desktop', 'Mobile', 'Large Desktop'], indirect=True)
def test_mobile(size_mobil):
    browser.open('https://github.com/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.quit()