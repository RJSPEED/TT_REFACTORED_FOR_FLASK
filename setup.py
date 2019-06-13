#! /usr/bin/env python3
from datetime import datetime, timedelta
from data.schema import schema
from data.seed import seed

schema()
seed()

