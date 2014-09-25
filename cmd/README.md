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

    $> export mytest='() { cat ~/.bash_history ; }'   #create env variable with function definition!
    $> bash -c 'mytest'                               #run the command mytest

    #Affected
    cd ..           #lines from ~/.bash_history    
    mkdir abcd      #lines from ~/.bash_history
   
    #Not affected
    #Source: http://arstechnica.com/security/2014/09/bug-in-bash-shell-creates-big-security-hole-on-anything-with-nix-in-it/
    #Resource: http://unix.stackexchange.com/questions/157329/what-does-env-x-something-bash-c-command-do-and-why-is-it-insecure
    bash: warning: x: ignoring function definition attempt
    bash: error importing function definition for `x'


###Resources
1. [GitHub Markdown Viewer](http://notepag.es/)
2. [Github Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 
