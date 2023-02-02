from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gym_management/__init__.py
from gym_management import __version__ as version

setup(
	name="gym_management",
	version=version,
	description="A gym management system is a software application that helps gym owners and managers to manage their daily operations and administration of a gym. It is designed to streamline tasks such as member management, billing, scheduling, class management, and equipment management. The system typically integrates various features such as member database management, membership plans and packages, payment processing, and reporting. It can also include features like member check-in, class scheduling and management, and workout tracking. The goal of a gym management system is to automate routine tasks, reduce manual errors, and provide actionable insights to help gyms grow and improve their offerings.",
	author="Mohseen Habib",
	author_email="mohseen@dlisaudi.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
