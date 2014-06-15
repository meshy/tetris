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
            $scope.blocks.push(event.data);
        });
    };

    var url = "ws://" + window.location.host + window.location.pathname + "ws/";
    WebSocketFactory.connect(url);
}
