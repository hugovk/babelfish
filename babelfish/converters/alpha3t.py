# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 the BabelFish authors. All rights reserved.
# Use of this source code is governed by the 3-clause BSD license
# that can be found in the LICENSE file.
#
from __future__ import unicode_literals
from . import LanguageEquivalenceConverter
from ..language import LANGUAGE_MATRIX

class Alpha3TConverter(LanguageEquivalenceConverter):
    CASE_SENSITIVE = True
    SYMBOLS = { alpha3: alpha3t
                for (alpha3, _, alpha3t, _, _, _, _, _) in LANGUAGE_MATRIX
                if alpha3t }
