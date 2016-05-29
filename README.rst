Python Separator Separated Values Package
=========================================

.. image:: https://img.shields.io/pypi/v/ssv.svg
        :target: https://pypi.python.org/pypi/ssv

.. image:: https://img.shields.io/travis/sfischer13/python-ssv.svg
        :target: https://travis-ci.org/sfischer13/python-ssv

Summary
-------

SSV stands for separator-separated values. It sounds like a joke, but it can actually be useful.

Description
-----------

SSV is a format for saving tabular data (`flat-file databases`__) as `delimiter-separated values`__ in a plain text file. In contrast to other formats, e.g. `CSV`__ or `TSV`__, `delimiter collision`__ is virtually impossible. Instead of using commas (CSV), tabs (TSV) and newlines, SSV relies on the record separator ``RS`` and the unit separator ``US`` for `data structuring`__, which should not occur at all in textual data.

__ https://en.wikipedia.org/wiki/Flat_file_database
__ https://en.wikipedia.org/wiki/Delimiter-separated_values
__ https://en.wikipedia.org/wiki/Comma-separated_values
__ https://en.wikipedia.org/wiki/Tab-separated_values
__ https://en.wikipedia.org/wiki/Delimiter#Delimiter_collision
__ https://en.wikipedia.org/wiki/Control_character#Data_structuring

The format is an example of `ASCII delimited text`__. As there is no official standard, SSV makes decisions that might be considered controversial. In general, simplicity and ease of implementation are preferred to other considerations. For example, SSV does not support escaping of ``RS`` and ``US``.

__ https://en.wikipedia.org/wiki/Delimiter#ASCII_delimited_text

Format
------

SSV files can be formally described by the following `W3C EBNF`__:

__ https://www.w3.org/TR/REC-xml/#sec-notation

.. code:: bnf

    SSV      ::= Record (RS Record)*
    Record   ::= Unit (US Unit)*
    Unit     ::= UnitChar*
    
    UnitChar ::= Char - (RS | US)
    Char     ::= /* see http://www.w3.org/TR/xml#NT-Char */
    RS       ::= #x1E
    US       ::= #x1F

Table records (rows) are separated by the record separator ``RS``. Each record contains one or more units (fields), which are separated by the unit separator ``US``. A unit may contain zero or more characters, excluding RS and US. As a consequence, an empty file is a valid SSV file and represents a 1-by-1 table containing a single empty field.

API Example
-----------

.. code:: python

    import ssv

    # simple table
    table = [['A1', 'B1', 'C1'],
             ['A2', 'B2', 'C2']]

    # encode table as SSV string
    ssv.dumps(table)  # 'A1\x1fB1\x1fC1\x1eA2\x1fB2\x1fC2'

    # write table to SSV file
    ssv.dumpf(table, 'data.ssv')
    # load table from SSV file
    new_table = ssv.loadf('data.ssv')
    assert table == new_table
