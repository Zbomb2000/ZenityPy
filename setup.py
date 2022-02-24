from setuptools import find_packages, setup
setup(
    name='zenitypy',
    packages=find_packages(include=['mypythonlib']),
    version='0.1.0',
    description='library test',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='test',
)
