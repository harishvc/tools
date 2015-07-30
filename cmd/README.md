Unix Command Line Tools
=======================
##Table of Contents
  * [Unix Command Line Tools](#unix-command-line-tools)
      * [Q1: Generate a sorted list of unique email addresses from a text file with email address seperated by comma.](#q1-generate-a-sorted-list-of-unique-email-addresses-from-a-text-file-with-email-address-seperated-by-comma)
      * [Q2: How can I split a text file with few thousand email addresses into smaller files?](#q2-how-can-i-split-a-text-file-with-few-thousand-email-addresses-into-smaller-files)
      * [Q3: How can I test bash shell for "Shellshock" vulnerability?](#q3-how-can-i-test-bash-shell-for-shellshock-vulnerability)
      * [Q4: How long does it take for a webpage to respond?](#q4-how-long-does-it-take-for-a-webpage-to-respond)
      * [Q5: Parse email address into generate custom output in CSV format](#q5-parse-email-address-into-generate-custom-output-in-csv-format)
      * [Q6: How to generate timestamp year-month-year hours:minutes:seconds (example: 2014-10-23 21:43:48)](#q6-how-to-generate-timestamp-year-month-year-hoursminutesseconds-example-2014-10-23-214348)
      * [Q7: How to replace all occurrence of a word in a file?](#q7-how-to-replace-all-occurrence-of-a-word-in-a-file)
      * [Q8: How much space is my folder taking up?](#q8-how-much-space-is-my-folder-taking-up)
      * [Q9: List all directories](#q9-list-all-directories)
      * [Resources](#resources)


###Q1: Generate a sorted list of unique email addresses from a text file with email address seperated by comma.

    $>cat email-list.txt
    abcd@a.com,efgh@b.com
    123@c.org, abcd@a.com
    bcd@t.org
    $>cat email-list.txt | tr "," "\n" | sort | uniq
    123@c.org
    abcd@a.com
    bcd@t.org
    efgh@b.com

###Q2: How can I split a text file with few thousand email addresses into smaller files?
   
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
 
###Q3: How can I test bash shell for "Shellshock" vulnerability?

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

###Q4: How long does it take for a webpage to respond?

    #Total time in seconds for google.com to respond
    $>curl -o /dev/null -s -w  %{time_total}\\n  http://google.com
    0.093

###Q5: Parse email address into generate custom output in CSV format

    $>cat test.txt
    harish.chakravarthy@aboutme.com
    $>cat test.txt | awk '{split($0,a,"@"); print a[1]}' | awk '{split($0,b,".");  print b[1],"\t",$0"@aboutme.com","\t","about.me/"$0}' | sed 's/^./\U&\E/'
    Harish  harish.chakravarthy@aboutme.com   about.me/harish.chakravarthy

###Q6: How to generate timestamp year-month-year hours:minutes:seconds (example: 2014-10-23 21:43:48)

	#!/bin/bash
	mydate=`date '+%Y-%m-%d %H:%M:%S'`
	echo $mydate

###Q7: How to replace all occurrence of a word in a file?

	$>find -type f -name filename.conf | xargs sed -i "s/old/new/g"
        

###Q8: How much space is my folder taking up?

        $> du -sk * | sort -rn     #sort by kilo bytes in descending order

###Q9: List all directories
     
        $> ls -d */

###Resources
1. [GitHub Markdown Viewer](http://notepag.es/)
2. [Github Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 
3. [GitHub emoji] (http://www.emoji-cheat-sheet.com/)

[![Analytics](https://ga-beacon.appspot.com/UA-55381661-1/tools/cmd/readme)](https://github.com/igrigorik/ga-beacon)
