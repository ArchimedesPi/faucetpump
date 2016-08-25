from functools import wraps
from collections import defaultdict
import logging
logger = logging.getLogger(__name__)

class PumpAPI(object):
	"""PumpAPI is a convenient mixin for providing the pumping decorators on any part of the faucetpump hierarchy.
	It makes it easier to test and reason about rather than stuffing it all in a main class directly.
	"""

	def __init__(self):
		self.faucets = defaultdict(dict)

	def faucet(self, fqname=None):
		def decorator(f):
			self.faucets[f].update(fqname=fqname, do=f)
			return f
		return decorator

	def schedule(self, when):
		def decorator(f):
			self.faucets[f].update(schedule=when, do=f)
			return f
		return decorator

	def payout(self, type, addr=None):
		def decorator(f):
			self.faucets[f].update(payout=dict(type=type, to_addr=addr), do=f)
			return f
		return decorator