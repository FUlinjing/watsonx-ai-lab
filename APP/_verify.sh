#!/bin/bash

t[0]="Checking if running on OSX";n[0]="Demo should be ran on Mac!"; c[0]='if [[ .`uname -a | grep "Darwin" | wc -l | xargs`. == .1. ]]; then exit 0; else exit 1; fi'
t[1]="Checking podman"           ;n[1]="Podman is not installed!"  ; c[1]='podman --version; exit $?'
t[2]="Checking git"              ;n[2]="Git is not installed!"     ; c[2]='git --version; exit $?'
t[3]="Checking node"             ;n[3]="Node.JS is not installed!" ; c[3]='node --version; exit $?'
t[4]="Checking npm"              ;n[4]="npm is not installed!"     ; c[4]='npm --version; exit $?'
t[5]="Checking python"           ;n[5]="python is not installed!"  ; c[5]='python --version; exit $?'
t[6]="Checking pip"              ;n[6]="pip is not installed!"     ; c[6]='pip --version; exit $?'
t[7]="Checking if ./API.en/service.WD.cred file exists";n[7]="Create ./API.en/service.WD.cred file from template!";c[7]='test -f ./API.en/service.WD.cred; exit $?'
t[8]="Checking if ./API.en/service.WX.cred file exists";n[8]="Create ./API.en/service.WX.cred file from template!";c[8]='test -f ./API.en/service.WX.cred; exit $?'
t[9]="Checking if ./GUI/settings.env file exists";n[9]="Create ./GUI/settings.env file from template!";c[9]='test -f ./GUI/settings.env; exit $?'

check () {
	text="$1"
	negative_statement="$2"
	cmd="$3"
	/bin/bash -c "${cmd}" >/dev/null 2>&1
	retVal=$?
	#echo $retVal
	printf "%s - " "${text}"
	if [[ .$retVal. == .0. ]]; then
		printdecor "green" "OK"; echo
		return 0
	else
		printdecor "red" "attention!"; printf " "; printdecor "orange" "$negative_statement";  echo
		return 1
	fi
}


printdecor () {
	color="$1"
	text="$2"
	
	R='\033[0;31m'
	G='\033[0;32m'
	B='\033[0;34m'
	Y='\033[0;33m'
	RES='\033[0m'

	case ${color} in
		'red') 
			printf "${R}"
			;;
		'green') 
			printf "${G}"
			;;
		'blue')
			printf "${B}"
			;;
		'orange')
			printf "${Y}"
			;;
		*)
			printf "${RES}"
			;;
	esac
	printf "${text} "
	printf "${RES}"
	}

exitCode=0
for (( i=0; i<${#t[@]}; i++ ));
do
  check "${t[$i]}" "${n[$i]}" "${c[$i]}"
  ((exitCode = exitCode + $?))
done

if [[ .${exitCode}. == .0. ]]; then
	printdecor "green" "Everything is OK, go ahead and build containers."; echo
	exit 0
else
	printdecor "orange" "Atention! Please check your local environment first."; echo 
	exit 1
fi
