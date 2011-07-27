# This recipe currently does ``nothing``[1] except require Bluebream packages.
# In the future, it may do ``something``.

# [1] Actually, it installs ``bin/paster``

from zc.buildout.easy_install import scripts
import pkg_resources

class Recipe(object):
    
    def __init__(self, buildout, name, options):
        self.buildout = buildout

    def install(self):
        # Generate paster script
        return scripts(['PasteScript'], pkg_resources.working_set,
            self.buildout['buildout']['executable'],
            self.buildout['buildout']['bin-directory'])

    def update(self):
        pass
