"""
HTTP Server for Sandnet experiments
"""

import os

from core.service import CoreService, addservice

from .. import SandnetService

class Service(SandnetService):
    _name = "HTTP"
    _configs = (
      '/etc/apache2/apache2.conf',
      '/var/www/index.html',
      '/etc/apache2/envvars',
    )
    _dirs = (
      '/etc/apache2',
      '/var/run/apache2',
      '/var/log/apache2',
      '/var/lock/apache2',
      '/run/lock/apache2',
      '/var/www',
    )
    _startup = ('apache2ctl start',)
    _shutdown = ('apache2ctl stop',)
    _validate = ('pidof apache2',)

    @classmethod
    def generateconfig(cls, node, filename, services):
      if filename == cls._configs[0]:
        with open('apache2.conf') as f:
          return f.read()
      elif filename == cls._configs[1]:
        with open('index.html') as f:
          return f.read()
      elif filename == cls._configs[2]:
        with open('envvars') as f:
          return f.read()

# vim: syntax=python ts=2 sw=2 sts=4 et
