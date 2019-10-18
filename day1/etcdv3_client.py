import sys
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages')
import etcd3
import base64

etcd = etcd3.client(host='47.94.82.211', port=2379)

#print(etcd.get('/registry/zhang'))
etcd.put('/registry/services/specs/tusdao/switch-monitor-fe-test', '{"ip": "192.168.1.1","port": 8090,"protocol": "tcp"}')
etcd.put('/registry/services/specs/tusdao/switch-monitor-fe-dev', '{"ip": "192.168.1.2","port": 8090,"protocol": "tcp"}')
etcd.put('/registry/services/specs/tusdao/switch-monitor-fe-prod', '{"ip": "192.168.1.3","port": 8090,"protocol": "tcp"}')

print(etcd.get('/registry/services/specs/tusdao/'))





#etcd.delete('bar')

#print(base64.decode('a'))




