import mechanize
import cookielib


def print_cookies(url):
    browser = mechanize.Browser()
    cookie_jar = cookielib.LWPCookieJar()
    browser.set_cookiejar(cookie_jar)
    page = browser.open(url)
    for cookie in cookie_jar:
        print cookie

url = 'http://www.syngress.com/'
print_cookies(url)

def test_user_agent(url, user_agent):
    browser = mechanize.Browser()
    browser.addheaders = user_agent
    page = browser.open(url)
    source_code = page.read()
    print source_code


def test_proxy(url, proxy):
    browser = mechanize.Browser()
    browser.set_proxies(proxy)
    page = browser.open(url)
    source_code = page.read()
    print source_code

# url = 'http://www.google.com'
# hide_me_proxy = {'http': '35.184.53.121:3128'}
# test_proxy(url, hide_me_proxy)

def view_page(url):
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    page = browser.open(url)
    source_code = page.read()
    print source_code

# view_page('http://www.syngress.com/')
# url = 'http://whatismyuseragent.dotdoh.com/'