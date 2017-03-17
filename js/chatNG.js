(function() {
	var app = angular.module('chatRoom', [ ]);			// create the module

    // controller syntax:
	app.controller ('chatController', function() {
		this.messages = defaultMsgs;                    // set default msgs

        this.addMsg = function (sender, msg){
            var newMsg = {sender, msg};
            this.messages.push( newMsg );
        };

	});

    var defaultMsgs = [
        {sender:0, msg:"Welcome to the Antisocial Social App!"},
        {sender:0, msg:"You can talk to yourself, because you're lonely as hell."}
    ];

})();
