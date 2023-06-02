from setuptools import find_packages, setup


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='shaggy',
    version='1.0.1',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Mauro Baladés',
    author_email='mauro.balades@tutanota.com',
    description='Discover and connect with social media accounts across multiple platforms using just a username with SocialTrackr, the ultimate account hunting software.',
    url='https://github.com/mauro-balades/shaggy',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'shaggy = shaggy.__main__:main',
        ],
    },
)
