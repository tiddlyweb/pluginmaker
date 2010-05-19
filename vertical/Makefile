# Simple Makefile for some common tasks. This will get
# fleshed out with time to make things easier on developer
# and tester types.
.PHONY: test dist release pypi clean

test:
	py.test -x test

remotes:
	./cacher

dist: clean remotes test
	python setup.py sdist

release: clean pypi

pypi: dist
	python setup.py sdist upload

clean:
	find . -name "*.pyc" | xargs rm || true
	rm -r dist || true
	rm -r build || true
	rm -r *.egg-info || true
