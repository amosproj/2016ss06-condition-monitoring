#!/usr/bin/env python
# encoding: utf-8

# File to maintain all constants which will be used in all DataProcessing Scripts

# Length of one Drive
DRIVE_LENGTH = 4
# Length of all drives
LINE_LENGTH = 12
# Amount of Carriers
AMOUNT_OF_CARRIERS = 15
# Wait time of the Simulator in Seconds used in compressInitialData.py
WAIT_TIME_IN_SECONDS_DPPY = 0.001
#Session of the demonstrator setting
SESSION = 1
# WaitTime of writeCarrierDataToDataBase.py
WAIT_TIME_IN_SECONDS_MPY = 5
# Separator of the CSV-Files
CSV_SEPARATOR = ";"

# Path of SQLITEDB
PATH_OF_SQLLITE_DB = '/srv/django/db.sqlite3'

NAME_TABLE_PROCESSED_DATA = 'helloWorld_timestampdata'
NAME_TABLE_COM_DATA = 'helloWorld_iterationdata'

NAME_TABLE_CARRIER = 'helloWorld_carrier'
NAME_TABLE_ITERATION = 'helloWorld_iteration'
NAME_TABLE_ITERATION = 'helloWorld_session'
