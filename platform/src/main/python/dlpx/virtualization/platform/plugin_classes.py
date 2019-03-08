#
# Copyright (c) 2019 by Delphix. All rights reserved.
#

import enum

"""Classes used for Plugin Operations

This module defines the non autogenerated classes used as input/output for
plugin operations. These are used instead of protobuf generated classes to
hide the implemenatation details for protobufs and also to provide the
correct types. For example, protobufs store the plugin defined properties
as json. However the plugin operations get these properties as an instance
of the autogenerated classes from the schemas (e.g. VirtualSourceDefinition)
"""

__all__ = [
    "VirtualSource",
    "StagedSource",
    "DirectSource",
    "RemoteConnection",
    "Status",
    "Mount",
    "OwnershipSpec",
    "MountSpec"]

class VirtualSource(object):

    def __init__(self, guid, connection, parameters):
        self._guid = guid
        self._connection = connection
        self._parameters = parameters

    @property
    def guid(self):
        """str: The unique guid identifier of this VirtualSource."""
        return self._guid

    @property
    def connection(self):
        """RemoteConnection: The RemoteConnection for this VirtualSource."""
        return self._connection

    @property
    def parameters(self):
        """VirtualSourceDefinition: The parameters of this VirtualSource."""
        return self._parameters

class StagedSource(object):

    def __init__(self, guid, connection, parameters, mount):
        self._guid = guid
        self._connection = connection
        self._parameters = parameters
        self._mount = mount

    @property
    def guid(self):
        """str: The unique guid identifier for this StagedSource."""
        return self._guid

    @property
    def connection(self):
        """SourceConnection: The RemoteConnection for this StagedSource."""
        return self._connection

    @property
    def parameters(self):
        """LinkedSourceDefinition: The LinkedSourceDefinition for this StagedSource."""
        return self._parameters

    @property
    def mount(self):
        """MountSpecification: The MountSpecification for this StagedSource."""
        return self._mount


class DirectSource(object):

    def __init__(self, guid, connection, parameters):
        self._guid = guid
        self._connection = connection
        self._parameters = parameters

    @property
    def guid(self):
        """str: The unique guid identifier for this DirectSource."""
        return self._guid

    @property
    def connection(self):
        """RemoteConnection: The RemoteConnection for this DirectSource."""
        return self._connectiongc

    @property
    def parameters(self):
        """LinkedSourceDefinition: The LinkedSourceDefinition for this DirectSource."""
        return self._parameters


class RemoteConnection(object):

    def __init__(self, environment, user):
        self._environment = environment
        self._user = user

    @property
    def environment(self):
        """RemoteEnvironment: The RemoteEnvironment for this RemoteConnection."""
        return self._environment

    @property
    def user(self):
        """RemoteUser: The RemoteUser for this RemoteConnection."""
        return self._user


class Status(enum.Enum):
    ACTIVE = 0
    INACTIVE = 1


class Mount(object):
    def __init__(self, remote_environment, mount_path, shared_path):
        self._remote_environment = remote_environment
        self._mount_path = mount_path
        self._shared_path = shared_path

    @property
    def remote_environment(self):
        """RemoteEnvironment: The RemoteEnvironment for this Mount."""
        return self._remote_environment

    @property
    def mount_path(self):
        """str: The path on the environment to mount to for this Mount."""
        return self._mount_path

    @property
    def shared_path(self):
        """str: The subset of the ZFS filesystem to mount on the mount_path."""
        return self._shared_path


class OwnershipSpec(object):
    def __init__(self, uid, gid):
        self._uid = uid
        self._gid = gid

    @property
    def uid(self):
        """int: The user id for this OwnershipSpec."""
        return self._uid

    @property
    def gid(self):
        """int: The group id for this OwnershipSpec."""
        return self._gid


class MountSpec(object):
    def __init__(self, mounts, ownership_spec):
        self._mounts = mounts
        self._ownership_spec = ownership_spec

    @property
    def mounts(self):
        """list of Mount: List of mounts for this MountSpec"""
        return self._mounts

    @property
    def ownership_spec(self):
        """OwnershipSpec: The OwnershipSpec for this MountSpec."""
        return self._ownership_spec
