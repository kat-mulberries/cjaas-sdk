# coding: utf-8

"""
    Azure Functions OpenAPI Extension

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class IdentityById(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'organization': 'str',
        'namespace': 'str',
        'person_id': 'str',
        'aliases': 'list[str]',
        'last_seen': 'object'
    }

    attribute_map = {
        'id': 'id',
        'organization': 'organization',
        'namespace': 'namespace',
        'person_id': 'personId',
        'aliases': 'aliases',
        'last_seen': 'lastSeen'
    }

    def __init__(self, id=None, organization=None, namespace=None, person_id=None, aliases=None, last_seen=None):  # noqa: E501
        """IdentityById - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._organization = None
        self._namespace = None
        self._person_id = None
        self._aliases = None
        self._last_seen = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if organization is not None:
            self.organization = organization
        if namespace is not None:
            self.namespace = namespace
        if person_id is not None:
            self.person_id = person_id
        if aliases is not None:
            self.aliases = aliases
        if last_seen is not None:
            self.last_seen = last_seen

    @property
    def id(self):
        """Gets the id of this IdentityById.  # noqa: E501


        :return: The id of this IdentityById.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdentityById.


        :param id: The id of this IdentityById.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def organization(self):
        """Gets the organization of this IdentityById.  # noqa: E501


        :return: The organization of this IdentityById.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this IdentityById.


        :param organization: The organization of this IdentityById.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def namespace(self):
        """Gets the namespace of this IdentityById.  # noqa: E501


        :return: The namespace of this IdentityById.  # noqa: E501
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this IdentityById.


        :param namespace: The namespace of this IdentityById.  # noqa: E501
        :type: str
        """

        self._namespace = namespace

    @property
    def person_id(self):
        """Gets the person_id of this IdentityById.  # noqa: E501


        :return: The person_id of this IdentityById.  # noqa: E501
        :rtype: str
        """
        return self._person_id

    @person_id.setter
    def person_id(self, person_id):
        """Sets the person_id of this IdentityById.


        :param person_id: The person_id of this IdentityById.  # noqa: E501
        :type: str
        """

        self._person_id = person_id

    @property
    def aliases(self):
        """Gets the aliases of this IdentityById.  # noqa: E501


        :return: The aliases of this IdentityById.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this IdentityById.


        :param aliases: The aliases of this IdentityById.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def last_seen(self):
        """Gets the last_seen of this IdentityById.  # noqa: E501


        :return: The last_seen of this IdentityById.  # noqa: E501
        :rtype: object
        """
        return self._last_seen

    @last_seen.setter
    def last_seen(self, last_seen):
        """Sets the last_seen of this IdentityById.


        :param last_seen: The last_seen of this IdentityById.  # noqa: E501
        :type: object
        """

        self._last_seen = last_seen

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(IdentityById, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IdentityById):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
