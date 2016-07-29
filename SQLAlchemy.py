#!/usr/bin/env python

import os
from random import randrange as rrange
from sqlalchemy import *
from ushuffle_db import NAMES, randName

FIELDS = ('login', 'uid', 'prid')
