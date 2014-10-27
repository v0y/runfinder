import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

requires = [
    'deform==2.0a2',
    'pyramid==1.5.1',
    'pyramid_debugtoolbar',
    'pyramid_webassets==0.8',
    'python-active-com-api==0.1.4',
    'SQLAlchemy==0.9.8',
    'waitress',
]

setup(
    name='runfinder',
    version='0.0',
    description='runfinder',
    long_description=README,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Rafał Mirończyk',
    author_email='rafal.mironczyk@lolwtf.pl',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    tests_require=requires,
    test_suite="runfinder",
    entry_points=(
        '[paste.app_factory]\n'
        'main = runfinder:main'
    ))
