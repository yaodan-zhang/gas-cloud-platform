#!/usr/bin/env python

# run_gas_dev.py
#
# Copyright (C) 2024 Yaodan Zhang
# University of Chicago
#
# Rns the GAS app using Flask's WSGI server for development/testing purposes
#
##
__author__ = 'Yaodan Zhang <katherinezh@uchicago.edu>'

from gas import app

if __name__ == '__main__':
  app.run(
    host=app.config['GAS_APP_HOST'],
    port=app.config['GAS_HOST_PORT'],
  )

### EOF
