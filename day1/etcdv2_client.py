

import etcd

client = etcd.Client(host='47.94.82.211', port=2379)


client.write('/nodes/n1', '{"ip": "192.168.1.1","port": 8090,"protocol": "tcp"}')

client.write('/nodes/n2', 2, ttl=4)  # sets the ttl to 4 seconds
client.set('/nodes/n2', 1) # Equivalent, for compatibility reasons.


print(client.read('/nodes/n1').value)

