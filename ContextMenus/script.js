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
		//alert("Onload");

		// Convert response to html
		//
		data = data.toString()

		//Parse string for alert
		jsonData = data.substring(data.indexOf('{'),data.lastIndexOf('}') +1)
		console.log(jsonData)

		var obj = JSON.parse(jsonData)
		var str = parseObj(obj);
		
		alert(str)
/*
		alert(data.toString());

		//readTextFile("popup.html");

		var w = 440;
		var h = 220;
		var left = (screen.width/2)-(w/2);
		var top = (screen.height/2)-(h/2); 

		chrome.windows.create({'url': 'popup.html', 'type': 'popup', 'width': w, 'height': h, 'left': left, 'top': top} , function(window) {
			window.document.write(data.toString())

		});*/

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

function readTextFile(file)
{
	var rawFile = new XMLHttpRequest();
	rawFile.open("GET", file, false);
	rawFile.onreadystatechange = function ()
	{
		if(rawFile.readyState === 4)
		{
			if(rawFile.status === 200 || rawFile.status == 0)
			{
				var allText = rawFile.responseText;
				alert(allText);
				console.log(allText);
				document.body.appendChild(allText);
			}
		}
	}
	rawFile.send(null);
}

parseObj = function(obj){
	var formattedStr = ""

	formattedStr += parseGraph(obj.graph)
	formattedStr += parseSentiment(obj.sentiment)
	formattedStr += parseJoke(obj.joke)

	return formattedStr
}

parseGraph = function(obj){
	//var toReturn = obj.toString() + "\n"
	obj = JSON.parse(obj)
	var toReturn = ""
	
	for (var item in obj){
		if(obj.hasOwnProperty(item)) {
			toReturn += "Key word: "
			toReturn += item + "\n"

			toReturn += parseKeyWord(obj[item])

			//toReturn += obj[item]
		}
	}
	return toReturn +"\n"

}

parseKeyWord = function(obj){
	var text = ""
	text += "     Description: " + obj["description"] + "\n"
	text += "     Fun facts: " + "\n"
	return text
}

parseSentiment = function(num){
	if(num < -0.3){
		return "This message seems negative.\n"
	}else if(num < 0.3){
		return "This message seems neutral.\n"
	}else{
		return "This message seems positive.\n"
	}
}

parseJoke = function(joke){
	return joke + "\n"
}