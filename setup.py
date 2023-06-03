from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='shaggy',
    version='1.0.6',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Mauro Baladés',
    author_email='mauro.balades@tutanota.com',
    description='Discover and connect with social media accounts across multiple platforms using just a username with SocialTrackr, the ultimate account hunting software.',
    url='https://github.com/mauro-balades/shaggy',
    packages=["shaggy"],
    install_requires=required,
    entry_points={
        'console_scripts': [
            'shaggy = shaggy:main',
        ],
    },
    license="MIT",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
