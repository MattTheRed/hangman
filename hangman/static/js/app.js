var app = angular.module('hangman', []);

app.config(function($interpolateProvider) {
    // Change the template symbol so it doesn't clash with Django
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});


app.factory('gameDataFactory', ['$http', function($http) {
    $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
    var url = 'game-data/';
    var dataFactory = {
        get: function() {
            return $http.get(url);
        },
        guess: function (letter) {
            var payload = {"guess": letter};
            return $http.post(url, payload);
        },
        newGame: function () {
            var payload = {"newGame": true};
            return $http.post(url, payload);
        }
    };

    return dataFactory;

}]);


app.controller('MainCtrl', ['$scope', 'gameDataFactory',
    function($scope, gameFactory) {

        gameFactory.get().success(function(gameData) {
            $scope.gameData = gameData;
        }).error();

        $scope.makeGuess = function (letter) {
            gameFactory.guess(letter).success(function (gameData) {
                $scope.gameData = gameData;
            });
        };

        $scope.newGame = function () {
            gameFactory.newGame().success(function (gameData) {
                $scope.gameData = gameData;
            });
        };

    }
]);


app.directive('hangman', function() {
  return {
    restrict: 'E',
    scope: {
      score: '=score'
    },
    link: function (scope, element) {
        var c = document.getElementById("hangman-canvas");
        var ctx = c.getContext("2d");

        function draw(score) {
            switch (score) {
                case 0:
                    ctx.clearRect(0,0,320, 280);
                    break;
                case 1: //Base
                    ctx.beginPath();
                    ctx.moveTo(150,250);
                    ctx.lineTo(250,250);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
                case 2: //Stand
                    ctx.beginPath();
                    ctx.moveTo(200,48);
                    ctx.lineTo(200,250);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
                case 3: //Stand top
                    ctx.beginPath();
                    ctx.moveTo(90,50);
                    ctx.lineTo(200,50);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
                case 4: // Stand hanging bit
                    ctx.beginPath();
                    ctx.moveTo(90,48);
                    ctx.lineTo(90,70);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
                case 5: // Head
                    ctx.beginPath();
                    ctx.arc(90,100,20,0,2*Math.PI);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
                case 6: // Body
                    ctx.beginPath();
                    ctx.moveTo(90,120);
                    ctx.lineTo(90,180);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
                case 7: // Left Arm
                    ctx.beginPath();
                    ctx.moveTo(40,130);
                    ctx.lineTo(90,140);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
                case 8: // Right Arm
                    ctx.beginPath();
                    ctx.moveTo(90,140);
                    ctx.lineTo(140,130);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
                case 9: // Left Leg
                    ctx.beginPath();
                    ctx.moveTo(40,230);
                    ctx.lineTo(90,178);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
                case 10: // Right Leg
                    ctx.beginPath();
                    ctx.moveTo(90,178);
                    ctx.lineTo(140,230);
                    ctx.lineWidth = 5;
                    ctx.strokeStyle = '#fff';
                    ctx.stroke();
                    break;
            }
        };

        scope.$watch(
            "score", function(score) {
                /* Looping up to current score so we redraw stickman state on
                page refresh */
                var i = 0;
                while (i < scope.score) {
                    draw(i);
                    i++;
                }
        });


    },
    template: '<canvas id="hangman-canvas" width="320" height="280"></canvas>'
  };
});
