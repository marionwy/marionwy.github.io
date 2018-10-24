    /*
      still missing:
        shorter?
        comments are missing
        result: center vertically 
    */
   
let firstNr = document.getElementById('firstnr');
let btnPlus = document.getElementById('btnplus');
let btnMinus = document.getElementById('btnminus');
let btnTimes  = document.getElementById('btntimes');
let btnDiv  = document.getElementById('btndiv');
let secondNr  = document.getElementById('secondnr');
let btnEquals = document.getElementById('btnequals');
let result = document.querySelector('output');   

let operation;

window.onload = firstNr.focus();
    
btnPlus.onclick = function() {
  operation = "plus";
  focusAfterOperation();
}
btnMinus.onclick = function() {
  operation = "minus";
  focusAfterOperation();
}
btnTimes.onclick = function() {
  operation = "times";
  focusAfterOperation();
}
btnDiv.onclick = function() {
  operation = "divide";
  focusAfterOperation();
}

function focusAfterOperation() {
  if(secondNr.value === '') {
    secondNr.focus();
  } else {
    btnEquals.focus(); /* style white instead of no colour: makes focus on button visible */
  }
} 

btnEquals.onclick = function() {
  if(operation === "plus") {
    result.value = parseFloat(firstNr.value)+parseFloat(secondNr.value);
  } else if(operation === "minus") {
    result.value = parseFloat(firstNr.value)-parseFloat(secondNr.value);
  } else if(operation === "times") {
    result.value = parseFloat(firstNr.value)*parseFloat(secondNr.value);
  } else if(operation === "divide") {
    result.value = parseFloat(firstNr.value)/parseFloat(secondNr.value);
  } 
  firstNr.value = result.value;
  firstNr.focus();
  secondNr.value = '';
}
