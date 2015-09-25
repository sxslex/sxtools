alias ll='ls -la $1'
mynosetests() {
	clear
	nosetests -dsv --with-yanc --with-coverage --cover-package $1 "$2"
}
alias nt=mynosetests
