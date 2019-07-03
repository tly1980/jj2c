VER=$(shell python -c 'import jj2c; print(jj2c.__VERSION__)')

test:
	PYTHONPATH=. pytest

doc:
	jj2c README.md.tpl -V "version: $(VER)" -e 'jinja2.ext.do' -o README.md
	pandoc --from=markdown --to=rst --output=README.rst README.md

package: clean doc
	echo "current jj2c version: $(VER)"
	python setup.py sdist bdist_wheel

clean:
	rm -rvf build dist

pypi:
	twine upload dist/*
	#python setup.py bdist_wheel --universal upload -r pypi
