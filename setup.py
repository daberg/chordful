from setuptools import setup

setup(
    name='chordful',
    author='daberg',
    description="A Web App to manage song chords.",
    packages=['chordful'],
    include_package_data=True,
    install_requires=[ 'flask' ],
    version='0.0.1'
)
