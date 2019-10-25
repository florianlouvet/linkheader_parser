from setuptools import setup


def readme():
    """Fetch readme content for long description of package."""
    with open('README.md') as f:
        return f.read()

setup(
    name='linkheader_parser',
    version='0.1',
    description='Python parser for LinkHeader',
    url='',
    author='Florian Louvet',
    license='Apache License 2.0',
    packages=['linkheader_parser'],
    install_requires=[],
    zip_safe=False,
    long_description=readme(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Link Header :: Parser :: Python',
    ],
    keywords='link header parser python linkheader',
    include_package_data=True
)