from faucetpump import scheduler

def test_parse_job():
	assert scheduler.parse_job('every 1s')['interval'] == 1
	assert scheduler.parse_job('every 1m')['interval'] == 60
	assert scheduler.parse_job('every 1h')['interval'] == 60 * 60

	assert scheduler.parse_job('every 1s')['run_mode'] == 'repeating'
	assert scheduler.parse_job('in 1s')['run_mode'] == 'oneshot'
	assert scheduler.parse_job('at 1s')['run_mode'] == 'oneshot'

