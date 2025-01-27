# Copyright Cartopy Contributors
#
# This file is part of Cartopy and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.

import matplotlib
import packaging.version


_MPL_VERSION = packaging.version.parse(matplotlib.__version__)
_MPL_36 = _MPL_VERSION.release[:2] >= (3, 6)
_MPL_38 = _MPL_VERSION.release[:2] >= (3, 8)
