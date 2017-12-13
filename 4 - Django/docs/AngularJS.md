
# AngularJS

## Resources

- [w3schools tutorial](https://www.w3schools.com/angular/)
- [official tutorial](https://docs.angularjs.org/tutorial)
- [code school course](https://www.codeschool.com/courses/shaping-up-with-angularjs)
- [API reference](https://docs.angularjs.org/api)


## Simple Example

```html
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.4/angular.min.js"></script>
    </head>
    <body>
    
    <div ng-app="">
      <p>Name : <input type="text" ng-model="name"></p>
      <h1>Hello {{name}}</h1>
    </div>
    
    </body>
</html>
```


## Todo App

```html
<html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.5.6/angular.min.js"></script>
    </head>
    <body>
        <div ng-app="todo_app" ng-controller="todo_ctrl">
          <input type="text" ng-model="todo_text"/>
          <button ng-click="add_todo()">add</button>
          <ul>
            <li ng-repeat="todo_item in todo_items">
              {{todo_item}}
              <button ng-click="complete_item($index)">✓</button>
            </li>
          </ul>
          <ul id="completed_list">
            <li ng-repeat="completed_item in completed_items">
              {{completed_item}}
            </li>
          </ul>
        </div>
        <script>
            var app = angular.module('todo_app', []);
            app.controller('todo_ctrl', function($scope) {
              $scope.todo_text = '';
              $scope.todo_items = ['wash the dog', 'butter the cat'];
              $scope.completed_items = [];
              
              $scope.add_todo = function() {
                $scope.todo_items.push($scope.todo_text);
              }
              
              $scope.complete_item = function(index) {
                var todo_text = $scope.todo_items[index];
                $scope.todo_items.splice(index, 1);
                $scope.completed_items.push(todo_text);
              }
              
            });
        </script>
    </body>
</html>
```

## Doing AJAX with $http


```html
<div ng-app="myApp" ng-controller="myCtrl"> 

<p>Today's welcome message is:</p>
<h1>{{myWelcome}}</h1>

</div>

<script>
var app = angular.module('myApp', []);
app.controller('myCtrl', function($scope, $http) {
    $http.get("welcome.htm")
    .then(function(response) {
        $scope.myWelcome = response.data;
    });
});
</script>
```