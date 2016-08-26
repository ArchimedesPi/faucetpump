import logging
import re
import pytimeparse

logger = logging.getLogger(__name__)

def parse_job(job_desc):
	desc_split = job_desc.split(' ')
	job = dict()
	job['run_mode'] = 'repeating' if desc_split[0] in ['every'] else 'oneshot'
	job['interval'] = pytimeparse.parse(desc_split[1])
	return job

class Scheduler(object):
	def __init__(self):
		self.actions = []

	def add_job(self, at, action):
		self.actions.append(dict(parse_job(at), action=action))

	"""Special job function for adding (usually recurring) pump jobs
	Of course, this entails tons of fancy scheduling and cooldown counts."""
	def add_pump_job(self, pump):
		pass