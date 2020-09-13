'''
import gevent
from gevent import socket

urls = ['www.google.com', 'www.example.com', 'www.python.org']

# this function is running async, wow
jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]

gevent.joinall(jobs, timeout=5)

res = [job.value for job in jobs]

print(res)
'''


import gevent
from gevent import monkey; monkey.patch_all()
import socket

hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com', 'www.google.com']
jobs = [gevent.spawn(socket.gethostbyname, host) for host in hosts]
gevent.joinall(jobs, timeout=5)

for job in jobs:
    print(job.value)
