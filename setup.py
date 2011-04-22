#!/usr/bin/env python
#
# $Id: setup.py 921 2005-02-15 16:32:23Z warnes $

CVS=0

from distutils.core import setup, Command, Extension
from SOAPpy.version import __version__

url="http://pywebsvcs.sf.net/"

long_description="SOAPpy provides tools for building SOAP clients and servers.  For more information see " + url


if CVS:
    import time
    __version__ += "_CVS_"  + time.strftime('%Y_%m_%d')


setup(name="SOAPpy",
      version=__version__,
      description="SOAP Services for Python",
      maintainer="Gregory Warnes",
      maintainer_email="Gregory.R.Warnes@Pfizer.com",
      url = url,
      long_description=long_description,
      packages=['SOAPpy','SOAPpy/wstools']
     )

