from setuptools import setup


def readme():
    """Fetch readme content for long description of package."""
    with open('README.md') as f:
        return f.read()

setup(
    name='linkheader_parser',
    version='0.6',
    description='Python parser for LinkHeader',
    url='https://github.com/FlorianLouvetRN/linkheader_parser',
    author='Florian Louvet',
    license='Apache License 2.0',
    packages=['linkheader_parser'],
    install_requires=[],
    zip_safe=False,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords='link header parser python linkheader',
    include_package_data=True
)