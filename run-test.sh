#!/usr/bin/env bash
#
# This file is part of Python Client Library for the LCCS Web Service.
# Copyright (C) 2019 INPE.
#
# Python Client Library for the LCCS Web Service is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#

pydocstyle lccs && \
isort --check-only --diff --recursive **/*.py && \
check-manifest --ignore ".travis-*" --ignore ".readthedocs.*" && \
pytest && \
sphinx-build -qnW --color -b doctest doc/sphinx/ doc/sphinx/_build/doctest
