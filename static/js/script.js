window.onload = function(){
    let search = document.getElementById("search");

     search.onfocus = function() {
        document.getElementById("searchborder").style.backgroundColor = "#f8f9fa";
        document.getElementById("searchbutton").style.color = "rgba(33, 37, 41, 0.5)";
        document.getElementById("searchbutton").style.transition = "none";
     }

     search.onblur = function() {
        document.getElementById("searchborder").style.backgroundColor = "";
        document.getElementById("searchbutton").style.color = "";
        document.getElementById("searchbutton").style.transition = "none";
     }
 };