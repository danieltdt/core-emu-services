''' Sandnet services
'''

import os

from core.service import addservice

from sandnet import dns, http, smtp

addservice(dns.Service)
addservice(http.Service)
addservice(smtp.Service)
