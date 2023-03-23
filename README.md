<p align="center">
  
  <img alt="GitHub Workflow Status" src="https://github.com/py-package/lite/actions/workflows/pythonapp.yml/badge.svg">

  <img alt="PyPI" src="https://img.shields.io/pypi/v/lite-gs">
  <img alt="issues" src="https://img.shields.io/github/issues/py-package/lite">
  <img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python Version">
  <img alt="GitHub release (latest by date including pre-releases)" src="https://img.shields.io/github/v/release/py-package/lite">
  <img alt="License" src="https://img.shields.io/github/license/py-package/lite">
  <a href="https://github.com/py-package/lite-gs/stargazers"><img alt="star" src="https://img.shields.io/github/stars/py-package/lite" /></a>
  <img alt="downloads" src="https://img.shields.io/pypi/dm/lite?style=flat" />
  <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

## Lite Framework

Lite is a lightweight Python web framework designed for simplicity and ease of use. It provides a minimalistic approach to web development with basic routing and request/response handling.

### Getting Started

#### Installation

```bash
pip install lite
```

#### Basic Usage

```python
lite craft app_name
```

This will create a new app in the current directory with the following structure:

    -- app_name
        -- app
            -- controllers
            -- middlewares
            -- models
            -- views
        -- config
            -- config.py
            -- database.py
            -- storage.py
        -- storage
        -- routes
            -- routes.py
        -- .env

#### Running the App

```bash
lite serve
```

This will start the app on port 8080 by default. You can change the port by setting the `PORT` environment variable.
