.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
init: ## Install package dependencies
	pip install --upgrade pip
	# install test project and package dependencies
	pip install -r requirements.txt
	# install package and dev dependencies (see setup.py)
	pip install '.[dev]'
lint: ## Run code linting
	python -m flake8 src
format: ## Format code with Black
	black src
	black tests
publish: ## Publish package to pypi
	python setup.py sdist bdist_wheel
	twine upload dist/* --verbose
	rm -fr build dist .egg src/lite_gs.egg-info
pypirc: ## Copy the template .pypirc in the repo to your home directory
	cp .pypirc ~/.pypirc