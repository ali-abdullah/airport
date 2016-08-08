
setup(
    name = 'airport',
    version = __version__,
    description = 'CLI program to change directory easily. ',
    url = 'https://github.com/ali-abdullah/airport',
    author = 'Ali Abdullah',
    author_email = 'ali.abdullah.salahuddin@gmail.com',
    license = 'MIT',
    keywords = 'cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = ['docopt'],
    extras_require = {
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points = {
        'console_scripts': [
            'airport=airport.cli:main',
        ],
    },
)