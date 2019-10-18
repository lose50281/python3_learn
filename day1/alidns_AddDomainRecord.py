#!/usr/bin/env python3
#coding=utf-8

import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


client = AcsClient('LTAIOtZ4XVOzYwel', 'Fu35BvMZj7ox6OoiqCak0xzAvts0xT', 'default')
request = CommonRequest()
request.set_accept_format('json')
request.set_domain('alidns.aliyuncs.com')
request.set_method('POST')
request.set_version('2015-01-09')
request.set_action_name('DescribeDomainRecords')

request.add_query_param('DomainName', 'tusdao.com')
request.add_query_param('PageNumber', '1')
request.add_query_param('PageSize', '500')
request.add_query_param('RRKeyWord', sys.argv[1])

response = client.do_action(request)
# python2:  print(response)

#print(str(response, encoding = 'utf-8'))

text=json.loads(str(response, encoding = 'utf-8'))
#print(text['DomainRecords']['Record'])
#print(str(response, encoding = 'utf-8'))

Dns_record = text['DomainRecords']['Record']

if Dns_record:
    print('%s.tusdao.com dnsRecord is exist' % (sys.argv[1]))
else:
    client = AcsClient('LTAIOtZ4XVOzYwel', 'Fu35BvMZj7ox6OoiqCak0xzAvts0xT', 'default')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_version('2015-01-09')
    request.set_action_name('AddDomainRecord')

    request.add_query_param('DomainName', 'tusdao.com')
    request.add_query_param('RR', sys.argv[1])
    request.add_query_param('Type', 'A')
    request.add_query_param('Value', '106.75.17.46')

    response = client.do_action(request)
    # python2:  print(response)
    print(str(response, encoding='utf-8'))

