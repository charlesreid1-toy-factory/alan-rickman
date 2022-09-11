from setuptools import setup, find_packages
from src import __version__

with open("requirements.txt") as f:
    all_deps = [x for x in f.read().splitlines() if not x.startswith("#")]
with open("requirements-test.txt") as f:
    test_deps = [x for x in f.read().splitlines() if not x.startswith("#")]

setup(
    name="alan-rickman",
    version=__version__,
    description="",
    author="Chaz Reid",
    author_email="charlesreid1@gmail.com",
    url="https://github.com/charlesreid1-toy-factory/alan-rickman",
    packages=["alan_rickman"],
    package_dir={"alan_rickman": "src"},
    license="MIT",
    install_requires=all_deps,
    extras_require={
        "test": test_deps,
    }
)

