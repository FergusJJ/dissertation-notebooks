from setuptools import find_packages, setup


def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


deps = read_requirements("requirements.txt")
dev_deps = []
try:
    dev_deps = read_requirements("requirements-dev.txt")
except FileNotFoundError:
    pass

setup(
    name="dissertation-notebooks",
    version="0.1",
    packages=find_packages(),
    install_requires=deps,
    extras_require={
        "dev": dev_deps,
    },
)
