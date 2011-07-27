from setuptools import setup, find_packages

setup(
    name='collective.recipe.bluebream',
    description='zc.buildout recipe to install bluebream',
    long_description=open('README.rst').read(),
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=[
        'collective',
        'collective.recipe',
    ],
    install_requires=[
        'setuptools',
        'Paste',
        'PasteDeploy',
        'PasteScript',
        'zope.securitypolicy',
        'zope.component',
        'zope.annotation',
        'zope.browserresource',
        'zope.app.dependable',
        'zope.app.appsetup',
        'zope.app.content',
        'zope.publisher',
        'zope.app.broken',
        'zope.app.component',
        'zope.app.generations',
        'zope.app.error',
        'zope.app.publisher',
        'zope.app.security',
        'zope.app.form',
        'zope.app.i18n',
        'zope.app.locales',
        'zope.app.zopeappgenerations',
        'zope.app.principalannotation',
        'zope.app.basicskin',
        'zope.app.rotterdam',
        'zope.app.folder',
        'zope.app.wsgi',
        'zope.formlib',
        'zope.i18n',
        'zope.app.pagetemplate',
        'zope.app.schema',
        'zope.app.container',
        'zope.app.debug',
        'z3c.evalexception>=2.0',
        'z3c.testsetup',
        'zope.app.testing',
        'zope.testbrowser',
        'zope.login',
        'zope.keyreference',
        'zope.intid',
        'zope.contentprovider',
        'zope.app.zcmlfiles',
    ],
    entry_points={
        'paste.app_factory': 'main = collective.recipe.bluebream:application_factory',
        'zc.buildout': 'default = collective.recipe.bluebream:Recipe',
    },
    author='Alex Clark',
    author_email='aclark@aclark.net',
    license='ZPL',
)
