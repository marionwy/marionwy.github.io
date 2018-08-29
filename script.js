/*
USE ARRAY:

Easy Version without errors of the website-user:
first click: is digit
second click: 
  if the second click is digit combine digits into strings 
    and convert to number again, same with third etc.
  if second (or later) click is operation use operation
continue until "=" is clicked --> operation is performed
always: click on "C": removes everything, fresh start

Fields on the website:
10 digit-fields: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
4 operation-fields: +, -, *, /
1 Clearance-field: C
*/

/* Tryout:
(var result = [];
if (click2 <= 9) ...)
/*


/* Example with only 2 digits and one operation (without HTML):*/


/* Variation: "plus": */

var plus = true;
var minus = false; 
var multi = false; 
var divi = false;

var click1 = 2;
var click2 = plus;
var click3 = 3;

if (click2 === plus) 
    {console.log (click1 + click3);
}
else if (click2 === minus)
    {console.log (click1 - click3);
}      
else if (click2 === multi)
    {console.log (click1 * click3);
}      
else if (click2 === divi)
    {console.log (click1 / click3);
}      

/* Variation: "minus": */

var plus = false;
var minus = true; 
var multi = false; 
var divi = false;

var click1 = 2;
var click2 = minus;
var click3 = 3;

if (click2 === plus) 
    {console.log (click1 + click3);
}
else if (click2 === minus)
    {console.log (click1 - click3);
}      
else if (click2 === multi)
    {console.log (click1 * click3);
}      
else if (click2 === divi)
    {console.log (click1 / click3);
}      

/* Variation: "multi": */

var plus = false;
var minus = false; 
var multi = true; 
var divi = false;

var click1 = 2;
var click2 = multi;
var click3 = 3;

if (click2 === plus) 
    {console.log (click1 + click3);
}
else if (click2 === minus)
    {console.log (click1 - click3);
}      
else if (click2 === multi)
    {console.log (click1 * click3);
}      
else if (click2 === divi)
    {console.log (click1 / click3);
}      

/* Variation: "divi": */

var plus = false;
var minus = false; 
var multi = false; 
var divi = true;

var click1 = 2;
var click2 = divi;
var click3 = 3;

if (click2 === plus) 
    {console.log (click1 + click3);
}
else if (click2 === minus)
    {console.log (click1 - click3);
}      
else if (click2 === multi)
    {console.log (click1 * click3);
}      
else if (click2 === divi)
    {console.log (click1 / click3);
}      


/* 10 Number-fields for clicking: */

var cero = 0;
var one = 1; 
var two = 2;
var three = 3;
var four = 4;
var five = 5;
var six = 6;
var seven = 7;
var eight = 8;
var nine = 9;










