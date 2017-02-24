function isEmpty(name) {
   var element = document.getElementById(name);
   var lenElement = element.value.length;
   var isvalid = element.getAttribute("data-isvalid");
   if (lenElement <= 0) {
       element.style.borderColor = "rgb(255, 0, 0)";
       element.setAttribute('data-isvalid','False');
   } else {
       element.style.borderColor = "rgb(0, 255, 0)";
       element.setAttribute('data-isvalid','True');
   }
}

function isChecked(name) {
    var buttons = document.getElementsByClassName(name);
    var count = 0;
    for (i = 0; i < buttons.length; i++) {
        if (buttons[i].checked == true){
            count++;
        }
    }
    if (buttons.length == count){
        return true
    }else {
        return false
    }
}


function checkInputs(inputs) {
   var validCount = 0;
   for (i = 0; i < inputs.length; i++) {
       var form = document.getElementById(inputs[i]).getAttribute("data-isvalid");
       if (form == "True") {
           validCount++;
       }
   }
   if (validCount == inputs.length) {
       return true
   } else {
       return false
   }
}

function toggleButtonRadioForm(name, nameClass) {
    var button = document.getElementById(name);
    if (isChecked(nameClass)){
        button.removeAttribute("disabled");
    } else {
        button.setAttribute("disabled", "disabled");
    }
}

function toggleButton(name, inputs) {
   var button = document.getElementById(name);
   var state = checkInputs(inputs);
   if (state) {
       button.removeAttribute("disabled");
   } else {
       button.setAttribute("disabled", "disabled");
   }
}