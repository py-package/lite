from setuptools import setup, find_packages

setup(
    name="lite-gs",
    version="0.1.0",
    description="Lite-gs is a lightweight Python web framework designed for simplicity and ease of use.",
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
            "isort",
            "pytest-cov",
            "twine>=1.5.0",
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