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


 // Needs adjustment for different screen size!
 function openNav() {
   document.getElementById("mySidebar").style.width = "280px";
   document.getElementById("pageOverlay").style.visibility = "visible";
   document.getElementById("pageOverlay").style.transition = "none";
}

function closeNav() {
   document.getElementById("mySidebar").style.width = "0";
   document.getElementById("pageOverlay").style.visibility = "hidden";
   document.getElementById("pageOverlay").style.transition = "0.5s";
}