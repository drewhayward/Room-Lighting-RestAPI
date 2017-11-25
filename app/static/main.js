(function () {

  'use strict';

  angular.module('mpApp', [])

  .controller('appController', ['$scope', '$log',
    function($scope, $log) {
    $scope.getResults = function() {
      $log.log("test");
    };
  }

  ]);

}());
