# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from __future__ import unicode_literals
from . import CountryReverseConverter
from ..exceptions import CountryConvertError, CountryReverseError
from ..country import COUNTRY_MATRIX


class CountryNameConverter(CountryReverseConverter):
    def __init__(self):
        self.codes = set()
        self.to_name = {}
        self.from_name = {}
        for alpha2, name in COUNTRY_MATRIX:
            self.codes.add(name)
            self.to_name[alpha2] = name
            self.from_name[name] = alpha2

    def convert(self, alpha2):
        if alpha2 not in self.to_name:
            raise CountryConvertError(alpha2)
        return self.to_name[alpha2]

    def reverse(self, name):
        if name not in self.from_name:
            raise CountryReverseError(name)
        return self.from_name[name]
