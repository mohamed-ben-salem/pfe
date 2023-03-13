from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gestion_de_paiment/__init__.py
from gestion_de_paiment import __version__ as version

setup(
	name="gestion_de_paiment",
	version=version,
	description="gestion de paiment",
	author="Mohamed Ben Salem && Samar Othmeni",
	author_email="bensalem1901@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
