// ========== SEARCH BAR ==========
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

// ========== SIDENAV OPEN/CLOSE ==========
 function openNav() {
   document.getElementById("mySidebar").style.width = "280px";
   document.getElementById("mySidebar").style.transition = "0.1s";
   document.getElementById("pageOverlay").style.visibility = "visible";
   document.getElementById("pageOverlay").style.transition = "none";
}

function closeNav() {
   document.getElementById("mySidebar").style.width = "0";
   document.getElementById("mySidebar").style.transition = "0.1s";
   document.getElementById("pageOverlay").style.visibility = "hidden";
   document.getElementById("pageOverlay").style.transition = "0.3s";
   // ----- Incase they are left open -----
   document.getElementById("eventNav").style.height = "0";
   document.getElementById("moreNav").style.height = "0";
}

// ========== EVENT OPEN/CLOSE ==========
function eOpenClose(){
   x = document.getElementById("eventNav").style.height;
   if (x == "100%") {
       return eClose();
   }
   return eOpen();
}

function eOpen() {
      document.getElementById("eventButton").setAttribute("aria-expanded", true);
      document.getElementById("eventNav").style.height = "100%";
}

function eClose() {
      document.getElementById("eventButton").setAttribute("aria-expanded", false);
      document.getElementById("eventNav").style.height = "0";
}

// ========== MORE OPEN/CLOSE ==========
function mOpenClose(){
   y = document.getElementById("moreNav").style.height;
   if (y == "100%") {
       return mClose();
   }
   return mOpen();
}

function mOpen() {
      document.getElementById("moreButton").setAttribute("aria-expanded", true);
      document.getElementById("moreNav").style.height = "100%";
}

function mClose() {
      document.getElementById("moreButton").setAttribute("aria-expanded", false);
      document.getElementById("moreNav").style.height = "0";
}