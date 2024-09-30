from setuptools import find_packages, setup

setup(
    name='unitTestSupport',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'textx[dev]'
    ],
    entry_points={
        'console_scripts': [
            'unitTestSupport=unitTestSupport.unit_test:main',
        ],
    },
    include_package_data=True,
    python_requires='>=3.6',
)
