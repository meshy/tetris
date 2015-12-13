/* http://css.dzone.com/articles/websocket-webmotion-and */
'use strict';

var app = angular.module('app', []);


app.factory('WebSocketFactory', function () {
    return {
        connect: function (url) {
            var self = this;
            this.connection = new WebSocket(url);

            this.connection.onopen = function () {
                if (this.onopen) {
                    self.onopen();
                }
            };
            this.connection.onclose = function () {
                if (this.onclose) {
                    self.onclose();
                }
            };
            this.connection.onerror = function (error) {
                if (this.onerror) {
                    self.onerror(error);
                }
            };
            this.connection.onmessage = function (event) {
                if (this.onmessage) {
                    self.onmessage(event);
                }
            };
        },

        send: function (message) {
            this.connection.send(message);
        },

        close: function () {
            this.connection.onclose = function () {};
            this.connection.close();
        }
    };
});


function MainCtrl($scope, WebSocketFactory) {
    $scope.connected = false;
    $scope.blocks = [];

    $scope.keydown = function (event) {
        var direction;
        switch (event.keyCode) {
        case 40:  // Down
            direction = 'mdown';
            break;
        case 37:  // Left
            direction = 'mleft';
            break;
        case 39:  // Right
            direction = 'mright';
            break;
        case 32:  // Space
            direction = 'rright';
            break;
        case 90:  // z
            direction = 'rleft';
            break;
        case 88:  // x
            direction = 'rright';
            break;
        default:
            break;
        }
        if (direction) {
            WebSocketFactory.send(direction);
        }
    };

    WebSocketFactory.onopen = function () {
        $scope.$apply(function () {
            $scope.connected = true;
        });
    };

    WebSocketFactory.onclose = function () {
        $scope.$apply(function () {
            $scope.connected = false;
        });
    };

    WebSocketFactory.onmessage = function (event) {
        $scope.$apply(function () {
            $scope.blocks = JSON.parse(event.data).blocks;
            console.log($scope.blocks);
        });
    };

    var url = "ws://" + window.location.host + window.location.pathname + "ws/";
    WebSocketFactory.connect(url);
}
