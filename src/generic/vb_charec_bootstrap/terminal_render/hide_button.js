// where do we store the dynamic content?
// request it from the web? nice but dumb! we need to be dynamic.
function myFunction(){
var plnrep="data:text/plain,This will be printed as poster\n\rThis in second line";
document.getElementById("main_player_window").setAttribute("poster",plnrep);}
