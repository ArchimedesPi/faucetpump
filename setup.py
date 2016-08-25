try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Faucetpump: A cryptocurrency faucet gamer',
    'author': 'Liam Marshall',
    'url': 'https://github.com/archimedespi/faucetpump',
    'download_url': 'https://github.com/archimedespi/faucetpump',
    'author_email': 'liam@cpan.org',
    'version': '0.1',
    'install_requires': [],
    'packages': ['faucetpump'],
    'scripts': [],
    'name': 'faucetpump'
}

setup(**config)