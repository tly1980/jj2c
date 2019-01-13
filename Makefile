
test:
	pytest

package:
	python setup.py sdist bdist_wheel

clean:
	rm -rvf build
