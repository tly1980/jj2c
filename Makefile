
test:
	pytest

package:
	python setup.py sdist bdist_wheel

clean:
	rm -rvf build

pypi:
	python setup.py bdist_wheel --universal upload -r pypi
