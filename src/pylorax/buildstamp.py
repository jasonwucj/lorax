#
# buildstamp.py
#
# Copyright (C) 2010  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Red Hat Author(s):  Martin Gracik <mgracik@redhat.com>
#

import logging
logger = logging.getLogger("pylorax.buildstamp")

import datetime
from sysutils import *


class BuildStamp(object):

    def __init__(self, workdir, product, version, bugurl, is_beta, buildarch):
        self.path = joinpaths(workdir, ".buildstamp")

        self.product = product
        self.version = version
        self.bugurl = bugurl
        self.is_beta = is_beta

        now = datetime.datetime.now()
        now = now.strftime("%Y%m%d%H%M")
        self.uuid = "{0}.{1}".format(now, buildarch)

    def write(self):
        logger.info("writing .buildstamp file")
        with open(self.path, "w") as fobj:
            fobj.write("[Main]\n")
            fobj.write("BugURL={0.bugurl}\n".format(self))
            fobj.write("IsBeta={0.is_beta}\n".format(self))
            fobj.write("Product={0.product}\n".format(self))
            fobj.write("UUID={0.uuid}\n".format(self))
            fobj.write("Version={0.version}".format(self))