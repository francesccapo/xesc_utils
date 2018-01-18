import distutils.core

distutils.core.setup(
    name='xesc',  # This is the name of your PyPI-package.
    version='1.1',  # Update the version number for new releases
    packages=['xesc', 'xesc.plotly', 'xesc.pre_proces', 'xesc.feat_eng', 'xesc.dim_reduction',
              'xesc.models'],  # The name of your scipt, and also the command you'll be using for calling it
    requires=['pandas', 'numpy', 'matplotlib', 'plotly']
)
