.PHONY: list
list:
	@LC_ALL=C $(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/(^|\n)# Files(\n|$$)/,/(^|\n)# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

shellcheck:
	shellcheck -x init.sh
doctest:
	python3 -m doctest project/proj.py
build:
	source .venv/bin/activate; mkdocs build
serve:
	source .venv/bin/activate; mkdocs serve

gh-deploy:
	source .venv/bin/activate; mkdocs gh-deploy


pre-commit:
	source .venv/bin/activate; pre-commit run --all-files

test:
	#source .venv/bin/activate; pytest tests/*
	source .venv/bin/activate; pytest --cov-report html --cov=project tests


bootstrap_cdk:  # prepare cdk to deploy to aws
	cdk bootstrap --cloudformation-execution-policies arn:aws:iam:aws:policy/AdministratorAccess	

clean:
	/bin/rm -fR site htmlcov 
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf
