
test:
	pytest

package:
	python setup.py sdist bdist_wheel

clean:
	rm -rvf build

pypi:
	twine upload dist/*
	#python setup.py bdist_wheel --universal upload -r pypi
