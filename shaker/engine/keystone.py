# Copyright (c) 2015 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from keystoneclient import discover as keystone_discover
from keystoneclient.v2_0 import client as keystone_v2
from keystoneclient.v3 import client as keystone_v3


def create_keystone_client(args):
    discover = keystone_discover.Discover(**args)
    for version_data in discover.version_data():
        version = version_data["version"]
        if version[0] <= 2:
            return keystone_v2.Client(**args)
        elif version[0] == 3:
            return keystone_v3.Client(**args)
    raise Exception(
        'Failed to discover keystone version for url %(auth_url)s.', **args)
