// Popup Angularjs
var appM = angular.module ('popupModule', [ ]);

// controller
appM.controller ('popupController', function($scope) {
	$scope.data = bodyText;

	$scope.updateData = function (){
		$scope.apply();
	}

	$scope.loadBody = function ( str ){
		bodyText = {'graph':
			{kek:[
				{name:'kekplex', id: 'kg:/m/03bby1', description: 'Building complex'},
				{name:'kek', id: 'kg:/m/045c7b', description: 'Technology company'},
				{name:'kek Chrome', id: 'kg:/m/04j7cyf', description: 'Web browser'},
				{name:'kek X', id: 'kg:/m/0hhrhd0', description: 'Research and development company'},
				{name:'kek Lively', id: 'kg:/m/04dzy3n', description: 'Video game'}
			]},
			'sentiment': 0.2, 'joke': ''
		};

		$scope.data = bodyText;
		$scope.$apply();
	};

});
// end controller

var bodyText = {'graph':
	{google:[
		{name:'Googleplex', id: 'kg:/m/03bby1', description: 'Building complex'},
		{name:'Google', id: 'kg:/m/045c7b', description: 'Technology company'},
		{name:'Google Chrome', id: 'kg:/m/04j7cyf', description: 'Web browser'},
		{name:'Google X', id: 'kg:/m/0hhrhd0', description: 'Research and development company'},
		{name:'Google Lively', id: 'kg:/m/04dzy3n', description: 'Video game'}
	]},
	'sentiment': 0.2, 'joke': ''};


function loadData ( str ) {
    angular.element(document.getElementById('PopupBody')).scope().loadBody(str);
	/*
    scope.$apply(function () {
    	scope.loadBody ( str );
    });*/
}




/*,
'montreal':
	{'Montreal Canadiens': {id: 'kg:/m/0bszz', description: 'Ice hockey team'},
	'Montr\xe9al\u2013Pierre Elliott Trudeau International Airport': {id: 'kg:/m/01n2nr', description: 'Airport'},
	'Montreal Alouettes': {id: 'kg:/m/0j8sq', description: 'Football team'},
	'Montreal': {id: 'kg:/m/052p7', description: 'Municipality'},
	'Washington Nationals': {id: 'kg:/m/03lpp_', description: 'Baseball Team'}
	}
}*/
