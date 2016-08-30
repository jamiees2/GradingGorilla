https://gist.github.com/Garviell/cd5e3c220e9d9940cc1c
```
var list = true;
var jq = document.createElement('script');
jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);
data = []
$(".ruTable").find("tr").each(function(){ var x = $(this).find("td"); if(typeof x[1] === "undefined") return; data.push([$(x[1]).text(), $(x[4]).text()]) })
if(list){
  du="";
  for(var i = 0; i < data.length; ++i){
    du += data[i][0] + " " + data[i][1] + "\n";
  }
  copy(du);
} else {
  copy(JSON.stringify(data))
}
```

https://gist.github.com/jamiees2/91878ef5047da14e26a6
```
var jq = document.createElement('script');
jq.src = "https://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js";
document.getElementsByTagName('head')[0].appendChild(jq);
data = []
$(".ruTable").find("tr").each(function(){ var x = $(this).find("td"); if(typeof x[1] === "undefined") return; data.push([$(x[1]).text(), $(x[4]).text()]) })
JSON.stringify(data)
```
