(function() {
	var app = angular.module('chatRoom', [ ]);	// create the module

    // controller syntax:
	app.controller ('chatController', function($http) {
		this.messages = defaultMsgs;            // set default msgs

        // HTTP POST
		$http.post('http://localhost/', "Hello from decode montreal with Google!",
            config).then( function (data) {		// IMPORTANT! Angular 1.4.8+ use .then, not .success
			             console.log(data);		// print PHP data in console
		});

        this.addMsg = function (sender, msg){
            var newMsg = {sender, msg};
            this.messages.push( newMsg );
        };

	});

    // default messages
    var defaultMsgs = [
        {sender:0, msg:"Welcome to the Antisocial Social App!"},
        {sender:0, msg:"You can talk to yourself, because you're lonely as hell."},
        {sender:1, msg:"lol kms"}
    ];

    var config = {					// HTTP post config - UTF-8 encoding
        headers : {
            'Content-Type': 'charset=utf-8;'
        }
    };

})();
