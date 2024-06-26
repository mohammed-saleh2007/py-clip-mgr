from setuptools import setup, find_packages

setup(
    name='pyclipmgr',
    packages=['pyclipmgr'],
    scripts=['pyclipmgr.py'],
    version='5.0.2',
    include_package_data=True,
    package_data={'': ['./bin/*']},
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='sudo man',
    author_email='supertechman@yahoo.com',
    description="this lib check for your machine's platform and use system commands to contact with clipboard (copy or paste) in python",
    url='https://github.com/mohammed-saleh2007/py-clip-mgr',
)
