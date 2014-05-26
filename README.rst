onoff
=====

onoff is a Python module that provides the `OnOffMixin` class which can be used
to add ``on()``, ``off()``, and ``trigger()`` style events to any Python class.

.. note::

    * For the latest, complete documentation: http://liftoff.github.io/onoff/
    * For the latest code: https://github.com/liftoff/onoff

Example
--------
.. code-block:: python

    >>> from onoff import OnOffMixin
    >>> class Foo(OnOffMixin):
    ...     def __init__(self):
    ...         self.on("hello", self.hello)
    ...     def hello(self, *args):
    ...         print("Hello: %s" % args)
    ...     def test(self, *args):
    ...         self.trigger("hello", *args)
    ...
    >>> f = Foo()
    >>> f.test("Triggered events rock!")
    Hello: Triggered events rock!
