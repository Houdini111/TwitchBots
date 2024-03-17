from setuptools import setup, find_packages

setup(
   name='TwitchBots',
   version='1.0',
   description='Wrapper utilities to make instantiating bots with common configurations easier. Wraps TwitchIO ',
   author='Houdini111',
   author_email='xela.notnef@gmail.com',
   packages = find_packages(),
   install_requires=['twitchio >= 2.9.0', 'PyYAML >= 5.4.1', 'setuptools >= 69.2.0'], #external packages as dependencies
   include_package_data=True
)