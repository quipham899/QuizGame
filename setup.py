import setuptools

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="GameProject"
    version="0.0.1",
    author="Qui Pham",
    author_email="qtpham191@stevenscollege.edu",
    url="https://github.com/thienqui-communistspy/GameProject",
    description="This project simulates ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require=[],
    tests_require=['pytest'],
    python_requires='>=3.6',
)
