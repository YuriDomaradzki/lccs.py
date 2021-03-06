#
# This file is part of Python Client Library for the LCCS Web Service.
# Copyright (C) 2019 INPE.
#
# Python Client Library for the LCCS Web Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""Python Client Library for the LCCS Web Service."""
from .utils import Utils


class ClassificationSystemClass(dict):
    """Class."""

    def __init__(self, data, validate=False):
        """Initialize instance with dictionary data.

        :param data: Dict with Class metadata.

        :param validate: true if the Class should be validate using its jsonschema. Default is False.
        :type bool
        """
        self._validate = validate
        super(ClassificationSystemClass, self).__init__(data or {})

    @property
    def id(self):
        """:return: the Class id."""
        return self['id']

    @property
    def description(self):
        """:return: the Class description."""
        return self['description']

    @property
    def name(self):
        """:return: the Class identifier (name)."""
        return self['name']

    @property
    def code(self):
        """:return: the Class code."""
        return self['code']


class ClassificationSystemClasses(dict):
    """Classifications System Classes."""

    def __init__(self, data, validate=False):
        """Initialize instance with dictionary data.

        :param data: Dict with Classes metadata.
        :param validate: true if the Classes should be validate using its jsonschema. Default is False.
        :type bool
        """
        self._validate = validate
        super(ClassificationSystemClasses, self).__init__(data or {})

    @property
    def get_class(self):
        """:return: list of classes."""
        return [ClassificationSystemClass(Utils._get(i['href'], self._validate), self._validate) for i in self['links'] if (i['rel'] == 'child')]
