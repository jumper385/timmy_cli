.PHONY: clean build upload

clean:
	rm -rf build dist *.egg-info
	rm -rf build *.sqlite

build:
	python3 -m build --sdist 

upload:
	twine upload dist/*

all: clean build upload
