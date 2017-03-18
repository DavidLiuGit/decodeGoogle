function getword(info,tab) {
  //alert("Get word");
  console.log("Word " + info.selectionText + " was clicked.");
  sendPost(info.selectionText);
  /*chrome.tabs.create({  
    url: "http://www.google.com/search?q=" + info.selectionText,
  });  */         
}
chrome.contextMenus.create({
  title: "Get suggestions for: %s", 
  contexts:["selection"], 
  onclick: getword,
});

sendPost = function(sel){
	var url = "http://localhost/";
	var method = "POST";
	var postData = sel;

	//var request = new XMLHttpRequest();
	var request = createCORSRequest(method, url);

	request.onload = function() {
		var status = request.status; // HTTP response status, e.g., 200 for "200 OK"
	    var data = request.responseText; // Returned data, e.g., an HTML document.
		console.log(data);
		alert("Onload");

		// Convert response to html
		//
		alert(data.toString());
	}

	//request.open(method, url, true);
	//request.setRequestHeader('Access-Control-Allow-Origin', '*')
	//request.setRequestHeader('Access-Control-Allow-Methods', 'POST, OPTIONS')

	request.setRequestHeader("Content-Type", "text/plain;charset=UTF-8");
	request.send(postData);

	//document.getElementById('debug').innerHTML = "kek" ;
}

function createCORSRequest(method, url) {
  var xhr = new XMLHttpRequest();
  if ("withCredentials" in xhr) {

    // Check if the XMLHttpRequest object has a "withCredentials" property.
    // "withCredentials" only exists on XMLHTTPRequest2 objects.
    xhr.open(method, url, true);

  } else if (typeof XDomainRequest != "undefined") {

    // Otherwise, check if XDomainRequest.
    // XDomainRequest only exists in IE, and is IE's way of making CORS requests.
    xhr = new XDomainRequest();
    xhr.open(method, url);

  } else {

    // Otherwise, CORS is not supported by the browser.
    xhr = null;

  }
  return xhr;
}

