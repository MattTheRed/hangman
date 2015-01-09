var app = angular.module('hangman', []);

app.config(function($interpolateProvider) {
    // Change the template symbol so it doesn't clash with Django
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.controller('MainCtrl', ['$scope',
    function($scope) {
        $scope.abc = [
            'A',
            'B',
            'C',
            'D',
            'E',
            'F',
            'G',
            'I'
        ];

        $scope.letters = ['B', 'A', ' '];

        $scope.score = 0;

    }
]);


app.directive('hangman', function() {
  return {
    restrict: 'E',
    scope: {
      customerInfo: '=info'
    },
    template: 'my-customer-iso.html'
  };
});
