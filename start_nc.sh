#! /bin/bash

ncat -lvkp 54321 -c "python xml_parser.py"