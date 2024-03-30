//Given unsorted array whose number range is [1, n] use cyclic sort.

//Algo

//[3, 5, 2, 1, 4]
//after soring index=val-1
// check index=arr[index] and swap if not at correct position or go to next element if its in correct position.
function cyclicSort() {
    let arr = [3, 5, 2, 1, 4];
    let len = arr.length;

    for (let i = 0; i < len;) {
        if (arr[i] !== i + 1) {
            let temp = arr[i];
            arr[i] = arr[temp - 1];
            arr[temp - 1] = temp;
        } else {
            i++;
        }
    }

    console.log(arr);
}

cyclicSort()