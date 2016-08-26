from functools import wraps
from collections import defaultdict
import logging
logger = logging.getLogger(__name__)

class Pump(object):
	def __init__(self, fqname, run='every 1min', currency=None, addr_pool=None, addr_cooldown=None):
		self.fqname = fqname
		self.schedule = run
		self.payout = dict(currency=currency, addr_pool=addr_pool or False, addr_cooldown=addr_cooldown)

	def run(self, f):
		self.run_function = f
		return f