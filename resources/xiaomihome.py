import logging
import sys
import time
from connector import *
from yeelight import *
import thread
import requests

def push_data(gateway, model, sid, short_id, cmd, data):
	r = requests.post(str(sys.argv[1]) + '&type=aquara&gateway=' + str(gateway) + '&model=' + str(model) + '&short_id=' + str(short_id) + '&sid=' + str(sid) + '&cmd=' + str(cmd), json=data, timeout=(0.5, 120), verify=False)

cb = lambda g, m, i, s, c, d: push_data(g, m, i, s, c, d)

def push_data2(gateway, data):
	r = requests.post(str(sys.argv[1]) + '&type=yeelight&yeelight=' + str(gateway), json=data, timeout=(0.5, 120), verify=False)

cb2 = lambda g, d: push_data2(g, d)

connector = XiaomiConnector(data_callback=cb)
yeelight = YeelightConnector(data_callback=cb2)
while True:
    connector.check_incoming()
    yeelight.check_incoming()
    time.sleep(0.05)
