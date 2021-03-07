from importlib.machinery import SourceFileLoader
from pathlib import Path

from setuptools import setup, find_packages

constants = SourceFileLoader('constants', 'vien/constants.py').load_module()


def readDocText():
    """Reads README.md and returns the text after first empty line.
    It helps to skip the header with badges intended only for GitHub.
    """
    doctext = (Path(__file__).parent / 'README.md').read_text()

    # skipping until first empty line
    lines = [l.strip() for l in doctext.splitlines()]
    firstEmptyLineIndex = lines.index("")
    lines = lines[firstEmptyLineIndex + 1:]

    return "\n".join(lines)


setup(
    name="vien",
    version=constants.__version__,

    author="Art Galkin",
    author_email="ortemeo@gmail.com",
    url='https://github.com/rtmigo/vien',

    packages=find_packages(),
    install_requires=[],

    description="Command-line shortcuts for Python virtual environments",

    long_description=readDocText(),
    long_description_content_type='text/markdown',

    license=constants.__license__,

    entry_points={
        'console_scripts': [
            'vien = vien:main_entry_point',
        ]},

    keywords="virtual-environment venv virtualenv python command-line shell terminal bash run create delete execute".split(),

    # https://pypi.org/classifiers/
    classifiers=[
        # "Development Status :: 4 - Beta",
        # "Development Status :: 2 - Pre-Alpha",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: BSD License',
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Topic :: Software Development :: Build Tools",
        "Operating System :: POSIX"
    ],

    # test_suite='nose.collector',
    # tests_require=['nose'],
    # zip_safe=False
)
