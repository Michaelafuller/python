/* 
  Given two arrays, interleave them into one new array.
  The arrays may be different lengths. The extra items should be added to the
  back of the new array.
*/

const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
const expected2 = [1, 2, 3, 4, 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 4];
const expected3 = [1, 2, 3, 4, 5, 7];

const arrA4 = [];
const arrB4 = [42, 0, 6];
const expected4 = [42, 0, 6];



/**
 * Interleaves two arrays into a new array. Interleaving means alternating
 * the items starting from the first array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr1
 * @param {Array<any>} arr2
 * @returns {Array<any>} A new array of interleaved items.
 */
// function interleaveArrays(arr1, arr2) {}
/* 









// create a function feeds in two array
// create a array variable for final outcome
// check which array is longer -> turn the longer length as an int variable
// iterate through the longer length
// push index value into the fin_outcome variable
*/
function interleaveArrays(arr1, arr2) {
    var fin_outcome=[]
    // var temp_lengh=0
    if(arr1.length>arr2.length){
        for(var i=0;i<arr1.length;i++){
            if(i<arr2.length){
                fin_outcome.push(arr1[i])
                fin_outcome.push(arr2[i])
            }
            else{
                fin_outcome.push(arr1[i])
            }
        }
    }
    else if(arr2.length>arr1.length){
        for(var i=0;i<arr2.length;i++){
            if(i<arr1.length){
                fin_outcome.push(arr1[i])
                fin_outcome.push(arr2[i])
            }
            else{
                fin_outcome.push(arr2[i])
            }
        }
    }
    else{
        for(var i=0;i<arr1.length;i++){
                fin_outcome.push(arr1[i])
                fin_outcome.push(arr2[i])
        }
    }
    return fin_outcome
}

console.log(interleaveArrays(arrA3, arrB3))
/*
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
function binarySearch(sortedNums, searchNum) {}









function binarySearch(sortedNums, searchNum) {
    var start = 0
    var end = sortedNums.length - 1
    var middle = Math.floor((start + end) /2)
    var found = false
    while (end >= start) {
        // console.log(sortedNums[middle]);
        if (sortedNums[middle] == searchNum) {
            found = true
            break
        } else if (sortedNums[middle] > searchNum) {
            end = middle - 1
        } else { // searchNum is greater
            start = middle + 1
        }
        middle = Math.floor((start + end) /2)
    }
    if (!found) {
        return false
    }
    // find all appearances
    var appearance = 1
    var i = middle + 1
    while(sortedNums[i] == searchNum) {
        appearance++
        i++
    }
    var j = middle - 1
    while(sortedNums[j] == searchNum) {
        appearance++
        j--
    }
    return appearance
}



/* 
  Given a SORTED array of integers, dedupe the array 
  Because array elements are already in order, all duplicate values will be grouped together.
  Ok to use a new array
  Bonus: do it in O(n) time (no nested loops, new array ok)
  Bonus: Do it in-place (no new array)
  Bonus: Keep it O(n) time even if it is not sorted
*/

const nums1 = [1, 1, 1, 1];
const expected1 = [1];

const nums2 = [1, 1, 2, 2, 3, 3];
const expected2 = [1, 2, 3];

const nums3 = [1, 1, 2, 3, 3, 4];
const expected3 = [1, 2, 3, 4];

const nums4 = [1, 1];
const expected4 = [1];

/**
 * De-dupes the given sorted array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {Array<number>} The given array deduped.
 */
function dedupeSorted(nums) {}

// ********************************************************************

/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else
  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

const nums1 = [3, 5, 4, 3, 4, 6, 5];
const expected1 = 6;

const nums2 = [3, 5, 5];
const expected2 = 3;

const nums3 = [3, 3, 5];
const expected3 = 5;


const nums4 = [5];
const expected4 = 5;

const nums5 = [];
const expected5 = null;

const nums6 = [3, 3, 5, 4, 3];
const expected6 = 5;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
function firstNonRepeated(nums) {}
