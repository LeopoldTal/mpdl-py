mpdl-py
=======

MPDL interpreter for Python

MPDL
----

MPDL (Mondrian Painting Description Language) is an esoteric language
`created by Arnaud Marguerat`_ to describe `Piet Mondrian`_ abstract paintings.

.. _`created by Arnaud Marguerat`: https://codegolf.stackexchange.com/questions/40741/mondrian-painting-description-language
.. _`Piet Mondrian`: https://en.wikipedia.org/wiki/Piet_Mondrian

Syntax
~~~~~~

MPDL operates on a stack of rectangles and outputs a square image. The stack
is initialised with a single rectangle filling the whole image. There are 3
commands:

1. ``v<integer 0-100>``: Pop a rectangle and split it vertically at the
   position given by the argument as percentage, rounded down. Push the left
   and right rectangles, in this order.

2. ``h<integer 0-100>``: Split horizontally. Push the top and bottom
   rectangles, in this order.

3. ``c<integer 1-4>``: Pop a rectangle and paint it a colour:
   
   - 1: white
   
   - 2: red
   
   - 3: blue
   
   - 4: yellow

Rectangles are drawn with a black border.

Example
~~~~~~~

The sample program::

    v25 h71 v93 h50 c4 c1 c1 c2 h71 c3 h44 c1 c1

run with canvas size 256px and border width 3px, outputs

.. image:: mondrian_composition.png

How to install
--------------

Installing from binaries
~~~~~~~~~~~~~~~~~~~~~~~~

TODO

Installing from source
~~~~~~~~~~~~~~~~~~~~~~~

TODO

Running the tests
~~~~~~~~~~~~~~~~~

Run tests in the root directory with::

    py.test

How to use
----------

TODO

Licence
-------

MIT. See LICENSE_ file.

.. _LICENSE: LICENSE

Credits
-------

Developer
~~~~~~~~~

mpdl-py is developed by `Leopold T. de Gaillande`_.

.. _`Leopold T. de Gaillande`: https://github.com/LeopoldTal/

Language author
~~~~~~~~~~~~~~~

MPDL is the work of `Arnaud Marguerat`_.

.. _`Arnaud Marguerat`: https://codegolf.stackexchange.com/users/13798/arnaud

Dependencies
~~~~~~~~~~~~

* setuptools
* pytest
* unittest
