#AWK: Quick Reference

#source: http://www.tutorialspoint.com/awk/awk_workflow.htm

    $>cat marks.txt
    1)    Amit     Physics    80
    2)    Rahul    Maths      90
    3)    Shyam    Biology    87
    4)    Kedar    English    85
    5)    Hari     History    89
    
    $>awk 'BEGIN{print "start ..."} {print} END{print "end ..."}' marks.txt
    start ...
    1)    Amit     Physics    80
    2)    Rahul    Maths      90
    3)    Shyam    Biology    87
    4)    Kedar    English    85
    5)    Hari     History    89
    end ...    	

#List all names
    $>awk 'BEGIN{printf "Name\n-----\n"} {print $2} ' marks.txt
    Name
    -----
    Amit
    Rahul
    Shyam
    Kedar
    Hari

#List names with letters `ar`
  $>awk 'BEGIN{printf "Names\n-----\n"} /ar/ {print $2} ' marks.txt 
  Names
  -----
  Kedar
  Hari
