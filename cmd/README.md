Unix Command Line Tools
=======================

###Problem 
Text file with email address seperated by comma. There can be multiple occurances of an email address
```$>cat email-list.txt
abcd@a.com,efgh@b.com
123@c.org, abcd@a.com
bcd@t.org
````
###Solution
````$>cat email-list.txt | tr "," "\n" | sort | uniq    
123@c.org
abcd@a.com
bcd@t.org
efgh@b.com
````


