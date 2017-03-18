function getWord(info,tab){
 console.log("Word " + info.selectionText + " was clicked.");
  sendPost(info.selectionText)        
}

chrome.contextMenus.create({
  title: "Antisocial: %s", 
  contexts:["selection"], 
  onclick: getword,
});

sendPost = function(sel){
	var url = "http://localhost/";
	var method = "POST";
	var postData = sel;

	var request = new XMLHttpRequest();

	request.onload = function () {
		var status = request.status; // HTTP response status, e.g., 200 for "200 OK"
	    var data = request.responseText; // Returned data, e.g., an HTML document.
	}

	request.open(method, url);

	request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
	request.send(postData);

	document.getElementById('debug').innerHTML = "kek" ;
}
