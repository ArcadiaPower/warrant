import os

from setuptools import setup, find_packages
from pip._internal.req import parse_requirements

parsed_install_reqs = parse_requirements('requirements.txt', session=False)
install_reqs = []
for ir in parsed_install_reqs:
    if hasattr(ir, 'req'):
        install_reqs.append(str(ir.req))
    else:
        install_reqs.append(str(ir.requirement))

parsed_test_reqs = parse_requirements('requirements_test.txt', session=False)
test_reqs = []
for ir in parsed_test_reqs:
    if hasattr(ir, 'req'):
        test_reqs.append(str(ir.req))
    else:
        test_reqs.append(str(ir.requirement))

version = '0.1'

README="""Python class to integrate Boto3's Cognito client so it is easy to login users. With SRP support."""

setup(
    name='notthatwarrant',
    version=version,
    description=README,
    long_description=README,
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ],
    keywords='aws,cognito,api,gateway,capless',
    author='Capless.io',
    author_email='opensource@capless.io',
    maintainer='Brian Jinwright',
    packages=find_packages(),
    url='https://github.com/ArcadiaPower/warrant',
    license='Apache License 2.0',
    install_requires=install_reqs,
    extras_require={'test': test_reqs},
    include_package_data=True,
    zip_safe=True,

)
