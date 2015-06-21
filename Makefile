clean:
	@find . -name "*.pyc" -delete
test:
	py.test tests/
