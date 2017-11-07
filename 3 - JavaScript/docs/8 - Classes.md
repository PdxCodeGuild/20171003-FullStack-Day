
# Classes


ES6 introduced a much easier way of writing classes, use it by default:

```javascript
class Animal {
    constructor(legs = 0) {
        this.legs = legs;
    }

    move() {
        if (this.legs > 0) {
            console.log('walk');
        }
        else {
            console.log('slither');
        }
    }
}

class Dog extends Animal {
    constructor(legs = 4, sound = 'ruff') {
        super(legs);
        this.sound = sound;
    }

    bark() {
        console.log(this.sound);
    }
}

let myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk'
myDog.bark(); // logs 'ruff'
```



The way to do classes is ES5 is much more awkward, but you may see it in the wild, so it's worth knowing.

```javascript
function Animal(legs) {
    this.legs = legs || 0;
}

Animal.prototype.move = function () {
    if (this.legs > 0) {
        console.log('walk');
    }
    else {
        console.log('slither');
    }
};

function Dog(legs, sound) {
    Animal.call(this, legs);
    this.sound = sound || 'ruff';
}

Dog.prototype = Object.create(Animal.prototype);

Dog.prototype.bark = function () {
    console.log(this.sound);
};

var myDog = new Dog(4);

console.log(myDog.legs); // logs 4
myDog.move(); // logs 'walk'
myDog.bark(); // logs 'ruff'
```

