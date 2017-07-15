from anon_browser import *
ab = anonBrowser(proxies=[], user_agents=[('User-agent', 'superSecretBrowser')])
for attempt in range(1, 5):
    ab.anonymize()
    print '[*] Fetching page'
    response = ab.open('http://www.facebook.com')
    for cookie in ab.cookie_jar:
        print cookie
