all: test

test:
	python3 -m doctest battle.py

clean:
	rm -rf __pycache__