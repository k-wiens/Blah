var services = angular.module('indexServices', ['ngResource']);

services.factory('Security', ['$resource', function ($resource) {
   return {
      SecurityToken: $resource('/GetSecurityToken.json', {}, {
         get: {
            method: 'GET'
         }
      }),

      ChangePassword: $resource('/ChangePassword.json', {}, {
         change: {
            method: 'POST'
         }
      }),

      GetLoginStatus: $resource('/GetLoginStatus.json', {}, {
         get: {
            method: 'GET'
         }
      })
   };
}]);


services.factory('Metrics', ['$resource', function ($resource) {
   return $resource('/logMetric.json', {}, {
      log: {
         method: 'GET'
      }
   });
}]);