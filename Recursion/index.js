// Recursion:- a function calling itself until a base condition is met.
// rescursion tree:- we represent all recurcive calls as function(variable) in their call order.

// //print name 5 times
// let nameCount=0
// function printName(){
//     if (nameCount==5){
//         return
//     }
//     nameCount++
//     console.log("Srinivas");
//     printName()
// }

// printName()

//print linearly from 1 to n
let i = 1
function print1ton(i, n){
    if (i>n){
        return
    }
    console.log(i)
    print1ton(++i, n)
}
print1ton(i, 10)