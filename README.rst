
Introduction
============

``collective.recipe.bluebream`` is a simple ``zc.buildout`` recipe you can use to bootstrap a Bluebream project. In fact, it is so simple that it contains no recipe functionality at all. It simply requires the packages that Bluebream 1.0 requires (based on the sample project setup described here: http://bluebream.zope.org/doc/1.0/gettingstarted.html). It may do more in the future, though.


Installation
============

Create a buildout::

    $ bin/easy_install zc.buildout
    $ bin/buildout init

Then edit buildout.cfg; use ``collective.recipe.bluebream`` like any recipe: just add a part and configure the ``recipe`` parameter. You should also configure a known good set of packages via the extends parameter::

    [buildout]
    extends = http://download.zope.org/bluebream/bluebream-1.0.cfg
    parts =
        bluebream

    [bluebream]
    recipe = collective.recipe.bluebream

Then run buildout::

    $ bin/buildout

Configuration
=============

By now you should have a ``bin/paster`` script. To run ``bluebream``, you will also need a WSGI configuration file and a Zope configuration file.

Here are some sample configuration files to get you started.

bluebream.ini
-------------

XXX Finish me

zope.conf
---------

XXX Finish me

Execution
=========

Now you can run paster::

    $ bin/paster serve bluebream.ini

And open ``http://localhost:8080`` in your browser.

Completion
==========

That's it! Checkout http://bluebream.zope.org for more information about Bluebream.
