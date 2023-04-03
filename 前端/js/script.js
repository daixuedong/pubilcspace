function updateClock(){
    var now=new Date();
    var h=now.getHours();
    var m=addZero(now.getMinutes());
    var s=addZero(now.getSeconds());

    document.querySelector('.h').innerHTML=h;
    document.querySelector('.m').innerHTML=m;
    document.querySelector('.s').innerHTML=s;
}

function addZero(num){
    return (num<10) ? '0' + num : num;
}

setInterval(updateClock,1000);