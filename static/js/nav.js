function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }
  
  let sideBar = document.querySelector(".sideBar");
  let sideBarBtn = document.querySelector(".sideBarBtn");
  sideBarBtn.addEventListener("click",()=>{
    sideBar.style.display=="block"?sideBar.style.display ="none":sideBar.style.display="block";
    })
