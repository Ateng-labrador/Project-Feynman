window.addEventListener('scroll', function(){
    var scroll = this.window.screenY;
    this.document.getElementById("myBody").style.marginTop = (-100 - 0.5*scroll) + "px";

    if(scroll >= 100){
        document.getElementById("myNav").classList.add("scrolled");
    }
    else{
        document.getElementById("myNav").classList.remove("scrolled");
    }
});