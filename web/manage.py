# manage.py
#
# Copyright (C) 2024 Yaodan Zhang
# University of Chicago
#
# Utilities for managing Flask project
#
##
__author__ = 'Yaodan Zhang <katherinezh@uchicago.edu>'

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from gas import app, db

app.config.from_object(os.environ['GAS_SETTINGS'])

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()

### EOF