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
