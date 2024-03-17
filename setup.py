from setuptools import setup, find_packages

setup(
   name='TwitchBots',
   version='1.0',
   description='Wrapper utilities to make instantiating bots with common configurations easier. Wraps TwitchIO ',
   author='Houdini111',
   author_email='xela.notnef@gmail.com',
   packages = find_packages(),
   install_requires=['twitchio', 'pyyaml'], #external packages as dependencies
)