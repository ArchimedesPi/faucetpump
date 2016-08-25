import logging
logger = logging.getLogger(__name__)


@faucet(fqname='Demo Faucet')
@schedule('every 1min')
def pump():
	logger.info('Demo faucet pump hit')