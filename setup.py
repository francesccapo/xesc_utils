from setuptools import setup

setup(name='xesc',  # This is the name of your PyPI-package.
      version='1.1',  # Update the version number for new releases
      packages=['xesc', 'xesc.plotly'],#, 'xesc.pre_proces', 'xesc.feat_eng', 'xesc.dim_reduction',
                #'xesc.models'],  # The name of your scipt, and also the command you'll be using for calling it
      install_requires=['pandas', 'numpy', 'matplotlib', 'plotly', 'dash', 'sklearn'],
      include_package_data=True)
