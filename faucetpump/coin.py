"""money money money money money money motherfuckers"""

from collections import defaultdict
from datetime import timedelta, datetime
import random
import pytimeparse

"""Describes a pot of potential cryptocoin addresses to deliver to and ranks fatigue on them"""
class Moneypot(object):
	def __init__(self, addresses, addr_fatigue_threshold=None, addr_cooldown_time=None):
		self.address_pool = addresses
		self.address_fatigue = defaultdict(int)
		self.address_lastused = dict()

		self.addr_fatigue_threshold = addr_fatigue_threshold or 5
		self.addr_cooldown_time = timedelta(seconds=pytimeparse.parse(addr_cooldown_time or '3d'))

	def get_addr(self):
		addr = random.choice([a for a in self.address_pool if self.address_fatigue[a] < self.addr_fatigue_threshold])
		self.address_fatigue[addr] += 1
		self.address_lastused[addr] = datetime.now()

		return addr

	def cooldown(self):
		pass