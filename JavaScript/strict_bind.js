'use strict'

var assert = require('assert');

let y = {
    x: 200,
    name: 'y',
};

console.log('y');
console.log(y);

let x = 100;
let test_module = {
    x: 0,
    addX: function() {
        console.log(this);
        this.x += 1;
        return this.x;
    },
    arrowAddX: () => {
        console.log(this)
        this.x += 1;
        return this.x
    },
};

//this = test_module; 
test_module.addX();
assert.equal(2, test_module.addX());

//this = y 
let bound = test_module.addX.bind(y);
bound();
assert.equal(2, test_module.x);
assert.equal(201, y.x);

//this = gobal
var m_b = test_module.addX;
//fail case x is undefined,
try {
    m_b();
} catch (e) {
    assert(true);
}

assert.equal(100, x);
assert.equal(201, y.x);


//[arrow_function](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Functions/Arrow_functions)
// **arrow function's this always who call method,**
var a_b = test_module.arrowAddX

this.x = 300;
assert.equal(2, test_module.x);
assert.equal(301, a_b());

var a_b_bound = test_module.arrowAddX.bind(this);
assert.equal(2, test_module.x);
assert.equal(302, a_b_bound());

var boundArrow = test_module.arrowAddX.bind(y)
assert.equal(2, test_module.x);
assert.equal(303, boundArrow());
