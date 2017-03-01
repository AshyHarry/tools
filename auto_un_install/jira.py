# -*- coding: utf-8 -*-
import os
from pprint import pprint

import requests

url = 'http://jira.leoers.com'
url = 'http://jira.leoers.com/secure/Dashboard.jspa'
url = 'http://jira.leoers.com/secure/IssueNavigator.jspa?mode=hide&requestId=10968'
url = 'http://jira.leoers.com/secure/IssueNavigator.jspa?mode=hide&reset=true&jqlQuery=project+%3D+POST+AND+issuetype+%3D+Story+AND+fixVersion+%3D+%221.0%22'
jira_page = requests.get(url)
print(jira_page.cookies)
fp = open('jira.html','wb')
fp.write(jira_page.content)
fp.close()
pprint(jira_page.headers)
print(jira_page.url)
print(jira_page.status_code)
print(jira_page.content)