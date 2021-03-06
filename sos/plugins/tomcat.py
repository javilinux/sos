# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

from sos.plugins import Plugin, RedHatPlugin


class Tomcat(Plugin, RedHatPlugin):
    """Apache Tomcat server
    """

    plugin_name = 'tomcat'
    profiles = ('webserver', 'java', 'services')

    packages = ('tomcat6',)

    def setup(self):
        self.add_copy_spec([
            "/etc/tomcat6",
            "/var/log/tomcat6/catalina.out"
        ])

    def postproc(self):
        self.do_file_sub(
            "/etc/tomcat6/tomcat-users.xml",
            r"password=(\S*)",
            r'password="********"'
        )

# vim: et ts=4 sw=4
