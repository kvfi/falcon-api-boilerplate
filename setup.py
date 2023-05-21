from setuptools import setup, find_packages

req = ['falcon', 'pyjwt[crypto]', 'sqlalchemy', 'pyyaml', 'alembic', 'bcrypt',
       'falcon-multipart', 'psycopg2-binary', 'marshmallow',
       'marshmallow-dataclass[enum,union]', 'coloredlogs', 'click', 'jinja2', 'python-json-logger', 'simplejson']

EXTRA_REQUIRE = {
    'dev': [],
    'test': 'pytest>=5.3.1'
}

req.extend(('waitress', 'hupper', 'gunicorn', 'gevent'))

setup(
    name='falcon_api_boilerplate',
    version='0.1.0',
    author='kvfi',
    install_requires=req,
    extras_require=EXTRA_REQUIRE,
    packages=find_packages()
)
