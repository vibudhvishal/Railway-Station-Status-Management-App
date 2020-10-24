//argument object - no longer bound with arrow functions. 

const add = (a,b) => {
   // console.log(arguments);
    return a + b;
};
console.log(55,1,1001);

//this keyword - no longer bound.

const user = {
    name: 'Andrew',
    cities: ['Singrauli','delhi','goa'],
    printPlacesLived() {
        return this.cities.map((city) => this.name + 'has lived in ' +city);
    }
};
console.log(user.printPlacesLived());

//challenge

const multiplier = {
    numbers: [1,2,3,4],
    multiplyBy: 3,
    finalNumbers () {
        return this.numbers.map((num) => num * this.multiplyBy);
    }
};
console.log(multiplier.finalNumbers());
