#Solving problems using Python 

##Table of Contents
  * [Solving problems using Python](#solving-problems-using-python)
    * [Q1: Join elements in an array](#q1-join-elements-in-an-array)
    * [Q2: Pop elements in an array](#q2-pop-elements-in-an-array)
    * [Q3: Print n elements in a string](#q3-print-n-elements-in-a-string)
    * [Q4: Get more information about python modules](#q4-get-more-information-about-python-modules)
    * [Q5: String concatenation](#q5-string-concatenation)
    * [Q6: One line if else statement](#q6-one-line-if-else-statement)
    * [Q7: Time now is epoch milliseconds](#q7-time-now-in-epoch-milliseconds)
    * [Q8: Find if substring exists in a string](#q8-find-if-substring-exists-in-a-string)

##Q1: Join elements in an array
    a1 = ['this','is','a','sentence']      
    a2 = '### '.join(a1)      
    print a2

##Q2: Pop elements in an array
    a1 = ['this','is','a','sentence']
    print a1.pop(-1) #last element in array
    print a1.pop(0) #first element in array
    print a1.pop(1) #new second element in array

##Q3: Print n elements in a string
    a1 = "Hello World!"
    #print 5 characters starting from position 0
    print a1[0:5] #Hello  

##Q4: Get more information about python modules
    $>pip freeze   #list all python modules and their version
    $>pip freeze > requirements.txt #generate requirements file
    $>pip show py2neo  #show information about py2neo; output includes version #
    
##Q5: String concatenation
    $>a = "Hello"
    $>b = "World"
    $>c = a + " " + b     
    $>print c  #Hello World

##Q6: One line if else statement
a = 1 if (b > 1) else 0  
#same as
if (b >1):
	a = 1
else:
	a = 0

##Q7: Time now in epoch milliseconds
    import datetime
    print int(datetime.datetime.now().strftime("%s")) * 1000    

##Q8: Find if substring exists in a string
    a = "Hello world" #string
    b = "world"       #sub-string
    if b in a:
	print "found"

##Q9: What is the data type?
    a = []
    print type(a)
    b = {}
    print type(b)



[![Analytics](https://ga-beacon.appspot.com/UA-55381661-1/tools/cmd/readme)](https://github.com/igrigorik/ga-beacon)
