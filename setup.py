"""
WeatherApp
==========
"""
from setuptools import setup, find_packages
import re
import ast

_version_re = re.compile(r'__version__\s+=\s+(.*)')
with open('weatherapp/version.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    name='weatherapp',
    version=version,
    url='http://weatherapp.readthedocs.org',
    license='MIT license',
    author='Saifali Saiyyad',
    author_email='saifsayyad@provider.com',
    description="Package for hosting groundwork apps and plugins like weatherapp_app or weatherapp_plugin.",
    long_description=__doc__,
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    platforms='any',
    setup_requires=[],
    tests_require=[],
    install_requires=['groundwork', ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': ["weatherapp = "
                            "weatherapp.applications.weatherapp_app:start_app"],
        'groundwork.plugin': ["YahooApiPlugin = "
                              "weatherapp.plugins.yahoo_api_plugin.yahoo_api_plugin:"
                              "YahooApiPlugin"],
    }
)
