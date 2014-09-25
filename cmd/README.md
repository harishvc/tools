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
How can I test bash shell for "Shellshock" vulnerability?

    $>cat test.sh
    #!/bin/bash
    env x='() { :;}; echo vulnerable' bash -c "echo testing ... ; cat ~/.bash_history"

    #Affected
    $>./test.sh
    vulnerable      #need to patch
    testing ...     
    cd ..           #lines from ~/.bash_history    
    mkdir abcd      #lines from ~/.bash_history
   
    #Not affected
    #Source: http://arstechnica.com/security/2014/09/bug-in-bash-shell-creates-big-security-hole-on-anything-with-nix-in-it/
    $>./test.sh
    bash: warning: x: ignoring function definition attempt
    bash: error importing function definition for `x'
    testing ...


###Resources
[GitHub Markdown Viewer](http://notepag.es/)
[Github Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 
