What is it?
==========================

Python3 compatible package for transforming [Cobertura](http://cobertura.github.io/cobertura/) test coverage XML into [Clover](https://www.atlassian.com/software/clover/overview) format.

This package can be used to convert [coverage.py](http://nedbatchelder.com/code/coverage/) output to a format [Bamboo](https://www.atlassian.com/software/bamboo) can display.

Install
------
Install lxml dependency (more info at http://lxml.de/installation.html):

    $ sudo apt-get install libxml2-dev libxslt-dev python3-dev
    $ sudo pip install lxml

Install cobertura-clover-transform:

    $ sudo pip install git+git://github.com/AlexKorovyansky/cobertura-clover-transform.git@python3

Usage
------
    $ python -m cobertura_clover_transform.converter [-h] [-o OUTPUT] coverage_xml

For example, command to transform coverage.xml to clover.xml:  

    $ python -m cobertura_clover_transform.converter -o clover.xml coverage.xml

The XML
-------

The transform is actually defined using an XSLT, which is inside
this repository. Feel free to use it for other purposes.

Dependencies
-------
* lxml - http://lxml.de/installation.html