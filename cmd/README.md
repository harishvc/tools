Unix Command Line Tools
=======================

###Question 1
Generate a sorted list of unique email addresses from a text file with email address seperated by comma.

    $>cat email-list.txt
    abcd@a.com,efgh@b.com
    123@c.org, abcd@a.com
    bcd@t.org
    $>cat email-list.txt | tr "," "\n" | sort | uniq
    123@c.org
    abcd@a.com
    bcd@t.org
    efgh@b.com

###Question 2
How can I split a text file with few thousand email addresses into smaller files?
   
    $>cat all-emails.txt 
    1@a.com
    2@a.com
    3@a.com
    4@a.com
    5@a.com
    6@a.com
    #Split all-emails.txt into files beginning with the name small-email.txt containing 2 lines of text
    $>cat all-emails.txt | split  -l 2  - small-email.txt
    $>less small-email.txtaa    
    1@a.com
    2@a.com
    $>less small-email.txtab
    3@a.com
    4@a.com
 
###Question 3
How can I test bash shell for "Shellshock" vulnerability?

    #Source: http://arstechnica.com/security/2014/09/bug-in-bash-shell-creates-big-security-hole-on-anything-with-nix-in-it/
    $>env x='() { :;}; echo vulnerable' bash -c "echo this is a test"

    #Affected
    vulnerable
    this is a test
   
    #Not affected
    #Resource: http://unix.stackexchange.com/questions/157329/what-does-env-x-something-bash-c-command-do-and-why-is-it-insecure
    bash: warning: x: ignoring function definition attempt
    bash: error importing function definition for `x'
    this is a test

###Question 4
How long does it take for a webpage to respond?

    #Total time in seconds for google.com to respond
    $>curl -o /dev/null -s -w  %{time_total}\\n  http://google.com
    0.093

###Question 5
Parse email address into generate custom output in CSV format

    $>cat test.txt
    harish.chakravarthy@aboutme.com
    $>cat test.txt | awk '{split($0,a,"@"); print a[1]}' | awk '{split($0,b,".");  print b[1],"\t",$0"@aboutme.com","\t","about.me/"$0}' | sed 's/^./\U&\E/'
    Harish  harish.chakravarthy@aboutme.com   about.me/harish.chakravarthy

###Question 6
How to generate timestamp year-month-year hours:minutes:seconds (example: 2014-10-23 21:43:48)

	#!/bin/bash
	mydate=`date '+%Y-%m-%d %H:%M:%S'`
	echo $mydate

###Resources
1. [GitHub Markdown Viewer](http://notepag.es/)
2. [Github Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 

[![Analytics](https://ga-beacon.appspot.com/UA-55381661-1/tools/cmd/readme)](https://github.com/igrigorik/ga-beacon)
