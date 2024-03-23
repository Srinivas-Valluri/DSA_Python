let arr = [1,2,3,4]

console.log(arr)
console.log(arr[0])

// negative indexes can be accesssed using .at() 
console.log(arr[-1])
// console.log(arr.at(-1))


console.log(arr.join(" + "))
console.log(arr.toString()) //gives comma seperated values

//add and remove at last
arr.push(5)
arr.pop(6)


//add and remove at start
arr.unshift(5)
arr.shift()

//delete leaves undefined holes in array. Always use pop or shift
// console.log(arr)
// delete arr[0]
// console.log(arr)

//add's elements of other array at the end. Can take any number of paramaters.
let arr2 = [5,6]
let allArr = arr.concat(arr2)
console.log(allArr)

//copies array elements to another position in an array
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.copyWithin(2, 0);
console.log(fruits)

const fruitss = ["Banana", "Orange", "Apple", "Mango", "Kiwi"];
fruitss.copyWithin(2, 0, 2);
console.log(fruitss)


//flatening array
const myArr = [[1,2],[3,4],[5,6]];
const newArr = myArr.flat();
console.log(newArr)


//The splice() method adds new items to an array.
const fruitsss = ["Banana", "Orange", "Apple", "Mango"];
fruitsss.splice(2, 0, "Lemon", "Kiwi"); //2->where to add; 0->how many items to remove while adding; next params are items to add.
console.log(fruitsss)
fruitsss.splice(0,1) // with splice we can also remove elements. Here we removed 1st element.
console.log(fruitsss)



//The slice() method slices out a piece of an array.
const fruitssss = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
const citrus = fruitssss.slice(2, 4);
console.log(citrus)

//-------------------Search
console.log("-------------- Search")

// array.indexOf(item, start); return -1 if not found
// array.lastIndexOf(item, start)
// array.includes(search-item)


//The find() method returns the value of the first array element that passes a test function.
const numbers = [4, 9, 16, 25, 29];
let first = numbers.find(myFunction); //
console.log(first)

function myFunction(value, index, array) {
  return value > 18;
}


//The findIndex() method returns the index of the first array element that passes a test function.
const numberss = [4, 9, 16, 25, 29];
let firstt = numberss.findIndex(myFunction);
console.log(firstt)

function myFunction(value, index, array) {
  return value > 18;
}

//findLast() method that will start from the end of an array and return the value of the first element that satisfies a condition.
// The findLastIndex() method finds the index of the last element that satisfies a condition.


//-------------------Sort
console.log("-------------- Sort")
const fruit = ["Banana", "Orange", "Apple", "Mango"];
fruit.sort();
console.log(fruit)
fruit.reverse()

//For numeric sort we have to provide a compare function
const points = [40, 100, 1, 5, 25, 10];
points.sort((a,b)=>a-b);
console.log(points)
console.log(Math.min(...points))
console.log(Math.max(...points))

//---------Array iteration
console.log("-------------------Iteration methods----------------")
let arr1 = [1,2,3,4]
arr1.forEach(myFunction)

function myFunction(val, index, arr){
  console.log(val, index, arr)
}

arr3 = arr1.map((value, index, array)=>{
  return value*value
})

console.log(arr3)

let arr4 = [1,2,3,4,5,6]
let arr5 = arr4.filter((val, index, arr)=>{
  return val>3
})

console.log(arr5)

let sum = arr4.reduce((sum, currVal, index, arr)=>{
  return sum+currVal
}, -26)
console.log(sum)

//every() - method checks if all array values pass a test.
let value = arr4.every((val)=>val>0)
console.log(value)

//some() - method checks if some array value pass a test.
let values = arr4.some((val)=>val>5)
console.log(values)

//Array.from() - returns an array from an iterable object
let v = Array.from("ABCDEF")
console.log(v)
let vv = Array(10).fill(0)      // -----------Create array of certain length with default values
console.log(vv)

//keys() - method returns an Array Iterator object with the keys of an array.
const keys = fruits.keys();

for (let x of keys) {
  process.stdout.write(x+ " ")    // ----------Print without newline
}

//entries - returns key value pair of key and array
const f = fruits.entries();

for (let x of f) {
  console.log(x)
}

//Array.with() - safe way to update elements in an array without altering the original array.
const months = ["Januar", "Februar", "Mar", "April"];
// const myMonths = months.with(2, "March");
// console.log(myMonths)

//... - Spread operator