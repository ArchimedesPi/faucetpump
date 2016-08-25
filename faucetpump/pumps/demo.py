import logging
logger = logging.getLogger(__name__)

pump = Pump('Demo Faucet Pump', run='every 1min', currency='fakecoin')

@pump.run
def do_the_pumpy_thing():
	logger.info('Demo faucet pump hit')