alias ll='ls -la $1'
mynosetests() {
	clear
	rm ./resp.txt
	nosetests -dsv --with-yanc --with-coverage --cover-package . $1 1>> resp.txt 2>> resp.txt >> resp.txt
	cat resp.txt
}
alias nt=mynosetests
