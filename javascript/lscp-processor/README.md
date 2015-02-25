# LSCP Processor Utils
This module contains utilities for processing lead score files provided by Call Source.
## The CSV to JavaScript Object parser
Parses specified csv files into a Javascript object.
## Mongodb Storage Utilities
Contains functions which allow the storage of the Javascript objects which are parsed using the CSV to Javascript object parser. This also contains functions which ensures the contents of csv files wouldn’t be duplicated in the database. It also has functions for determining whether a calls processed file is Enhanced or not, and upserts it to the database if it is. Another feature of this module includes a mechanism which includes scores which are scored more than once in a separate database called `weirdScores` to ensure that all data will be counted as is (while also ensuring the uniqueness of these scores).
