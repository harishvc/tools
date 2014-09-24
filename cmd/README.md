Unix Command Line Tools
=======================

###Problem 1
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

###Credits
http://notepag.es/
