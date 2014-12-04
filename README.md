cobertura-clover-transform
==========================

Tools for transforming Cobertura test coverage XML into Clover-style XML

As it turns out, the coverage created by [coverage.py](http://nedbatchelder.com/code/coverage/)
outputs in Cobertura.

[Bamboo](https://www.atlassian.com/software/bamboo) has built in
support for displaying Clover test coverage output.

This tool can be used to convert Coverage.py output to a format
Bamboo can display.

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