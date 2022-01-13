// '''
// create a function that given a string, returns the string's acronym
// (first letter of each word capitalized)
// do it with the .split first if you need to, then try to do it without
// '''
const str1 = "there's no free lunch - gotta pay yer way."
const expected1 = 'TNFL-GPYW'

const str2 = "Live from New York, it's Saturday Night!"
const expected2 = 'LFNYISN'


function acronymCreator(str){
    var newArr= [str.split(" ")]
    var expected = ""
    for(var j = 0; j <= newArr.length[0]; j++){
            expected += newArr[0][j].charAt(0)
        }
    console.log(newArr[0][j].charAt(0))
    return expected
}

console.log(acronymCreator(str1))

// turns give str into an acronym
// - time: 0(?)
// - space: 0(?)
// @param {string} str a string to be turned into an acronym
// @returns {string} the given str converted into an acronym

// pseudo code

/*
- create a function that takes in a string and returns a string
- create a var to hold onto the return item (string)
- convert given string into a list - (use .split(" "))
- create a loop to loop through all the items in the new list
    - grab the first letter of each item in the list
    - make uppercase 
    - add it to return item variable
- return the return item (string)
*/



/* 
  Given an arr and a separator string, output a string of every item in the array separated by the separator.
  
  No trailing separator at the end
  Default the separator to a comma with a space after it if no separator is provided
*/


// const arr1 = [1, 2, 3];
// const separator1 = ", ";
// const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

// const arr3 = [1, 2, 3];
// const separator3 = " - ";
// const expected3 = "1 - 2 - 3";

// const arr4 = [1];
// const separator4 = ", ";
// const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";


// pseudo code
//  create function that interprets array as string
// includes seperator between iteration

function seperatorCreator(arr, separator){
    var newStr = "";
    if(arr.length < 1){
        return newStr
    }
    for(var i = 0; i < arr.length-1; i++){
        newStr += (arr[i] + separator)
    }
    newStr += arr[arr.length-1]
    return newStr;
}

console.log(seperatorCreator(arr5, separator5))


/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.

    - create a function that takes in a string and returns a string
    - create a return string
    - create a count variable that starts at 1
    - EDGE CASE: if string has no length
    - loop through the given string
        - compare the current string index to the index - 1 
        - if true: increase count
            - if character not already in return string then add to return string
        - if false: 
            - add the total count for the variable to return string
            - reset the count variable back to 1
    - return the return variable string...

  */

    const str1 = "aaaabbcddd";
    const expected1 = "a4b2c1d3";
    
    const str2 = "";
    const expected2 = "";
    
    const str3 = "a";
    const expected3 = "a";
    
    const str4 = "bbcc";
    const expected4 = "bbcc";


function encode(str){
    var newStr = ""
    var count = 1
    if (newStr.length == str.length) {
        return str
    }
    for(var i = 0; i<str.length; i++){
        if (str[i] == str[i+1]){
            count ++
        }
    }
}
    /**
     * Encodes the given string such that duplicate characters appear once followed
     * by a number representing how many times the char occurs only if the
     * character occurs more than two time.
     * - Time: O(?).
     * - Space: O(?).
     * @param {string} str The string to encode.
     * @returns {string} The given string encoded.
     */
    function encodeStr(str) {}



//   **************************************************************************************

/* 
  String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
function decodeStr(str) {}