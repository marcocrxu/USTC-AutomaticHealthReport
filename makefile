all: report

report:
	python main.py > log.txt

clean:
	rm -rf __pycache__