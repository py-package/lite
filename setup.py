from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lite-gs",
    version="0.1.2",
    description="Lite-gs is a lightweight Python web framework designed for simplicity and ease of use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Yubaraj Shrestha",
    author_email="yubaraj@py-package.com",
    url="https://github.com/py-package/lite",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "waitress",
        "click",
        "jinja2",
        "hupper",
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
            "coverage",
            "pytest",
            "pytest-cov",
            "twine>=1.5.0",
            "wheel",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
    keywords="Python, Framework, Lite, Web, Web Framework, Python Framework",
    entry_points={
        "console_scripts": [
            "lite=lite.cli:lite",
        ],
    },
    package_data={
        '': [],
    },
)