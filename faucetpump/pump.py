from functools import wraps
from collections import defaultdict
import logging
logger = logging.getLogger(__name__)

class Pump(object):
	def __init__(self, fqname, run='every 1min', currency=None):
		self.fqname = fqname
		self.schedule = run
		self.payout = dict(currency=currency)

	def run(self, f):
		self.run_function = f
		return f