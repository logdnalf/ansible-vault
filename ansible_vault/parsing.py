#
# Copyright (C) 2021, Tomohiro NAKAMURA <quickness.net@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
from abc import ABCMeta, abstractmethod

import ansible
from pkg_resources import parse_version

from ._compat import VaultLib


class VaultLibABC(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def encrypt(self, plaintext):
        raise NotImplementedError

    @abstractmethod
    def decrypt(self, vaulttext):
        raise NotImplementedError


class AnsibleVaultLib(VaultLibABC):
    """Default encrypt/decrypt lib."""

    def __init__(self, secret, vault_id=None):
        self.vault_id = vault_id
        self.vault = VaultLib(make_secrets(secret))

    def encrypt(self, plaintext, vault_id=None):
        return self.vault.encrypt(plaintext, vault_id=self.vault_id or vault_id)

    def decrypt(self, vaulttext):
        return self.vault.decrypt(vaulttext)


def make_secrets(secret):
    """Create ansible compatible secret."""
    if parse_version(ansible.__version__) < parse_version("2.4"):
        return secret

    from ansible.constants import DEFAULT_VAULT_ID_MATCH
    from ansible.parsing.vault import VaultSecret

    return [(DEFAULT_VAULT_ID_MATCH, VaultSecret(secret))]
