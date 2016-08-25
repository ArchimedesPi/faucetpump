from faucetpump.pump_api import PumpAPI

def test_creation():
	api = PumpAPI()

	@api.faucet(fqname='foo')
	def foo():
		pass

	print api.faucets
	assert api.faucets[foo]['fqname'] == 'foo'

def test_schedule_set():
	api = PumpAPI()

	@api.faucet()
	@api.schedule('every 1m')
	def foo():
		pass

	print api.faucets
	assert api.faucets[foo]['schedule'] == 'every 1m'

def test_payout_set():
	api = PumpAPI()

	@api.faucet()
	@api.payout('bitcoin', addr='abad1dea')
	def foo():
		pass

	assert api.faucets[foo]['payout']['type'] == 'bitcoin'
	assert api.faucets[foo]['payout']['to_addr'] == 'abad1dea'
