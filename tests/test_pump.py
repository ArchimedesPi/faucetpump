from faucetpump.pump import Pump

def test_creation():
	pump = Pump('A Test Pump', run='every 1m', currency='btc', addr_pool=True,
		addr_cooldown='3d')

	@pump.run
	def foo():
		pass

	assert pump.fqname == 'A Test Pump'
	assert pump.schedule == 'every 1m'
	assert pump.payout['currency'] == 'btc'
	assert pump.run_function == foo