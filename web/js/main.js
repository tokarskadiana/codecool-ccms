/**
 * Check if input is empty and change color to red if yes otherwise change color to green.
 * @param {id} name - markup
 */
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

/**
 * Check if buttons with given class is checked.
 * @param {class} name - class name of buttons
 * @return {boolean}
 */
function isChecked(name) {
    var buttons = document.getElementsByClassName(name);
    var count = 0;
    for (i = 0; i < buttons.length; i++) {
        if (buttons[i].checked == true){
            count++;
        }
    }
    if ((buttons.length/2) == count){
        return true
    }else {
        return false
    }
}

/**
 * Check if inputs have True value in data-isvalid parameter in given array of inputs.
 * @param {array} inputs - array with id
 * @return {boolean} return true if all of given inputs have True value in data-isvalid parameter
 *  otherwise return false.
 */
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

/**
 * Disable given button with id given in name parameter when isChecked
 *  return False with given class of radio buttons otherwise enable button.
 * @param {id} name - id of button
 * @param {class} nameClass - class name of radio buttons
 */
function toggleButtonRadioForm(name, nameClass) {
    var button = document.getElementById(name);
    if (isChecked(nameClass)){
        button.removeAttribute("disabled");
    } else {
        button.setAttribute("disabled", "disabled");
    }
}

/**
 * Disable given button with id given in name parameter when checkInputs
 *  return False with given array of id inputs otherwise enable button.
 * @param {id} name - class name of buttons
 * @param {array} inputs - array of id inputs
 */
function toggleButton(name, inputs) {
   var button = document.getElementById(name);
   var state = checkInputs(inputs);
   if (state) {
       button.removeAttribute("disabled");
   } else {
       button.setAttribute("disabled", "disabled");
   }
}