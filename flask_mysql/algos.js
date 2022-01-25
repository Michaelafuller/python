/* 
Parens Valid
Given an str that has parenthesis in it
return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
function parensValid(str) {
    var count = 0
    for(var i = 0; i<str.length; i++){

    }

}










function parensValid(str) {
    var count = 0
    for(var i=0;i<str.length;i++){
        if(str[i]==='('){
            count++
        }
        else if(str[i]===')'){
            count--
        }
        if (count<0){
            return false
        }
    }
    if(count == 0){
        return true
    }
    return false
}


/* 
Braces Valid
Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str3 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected3 = true;

const str4 = "D(i{a}l[ t]o)n{e";
const expected4 = false;

const str5 = "A(1)s[O (n]0{t) 0}k";
const expected5 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
function bracesValid(str) {

    // Your code here
}









/*****************************************************************************/

function bracesValid(str) {
    var symbolArray = []
    var openSymbols = {
        '(':')',
        '[':']',
        '{':'}'
    }
    var closeSymbols = {
        ')':'(',
        ']':'[',
        '}':'{'
    }
    for (var i = 0; i < str.length; i++) {
        if (openSymbols.hasOwnProperty(str[i])) {
            symbolArray.push(str[i])
        } else if (closeSymbols.hasOwnProperty(str[i])) {
            if (symbolArray.length == 0) {
                return false
            }
            if (str[i] != openSymbols[symbolArray.pop()]) {
                return false
            }
        }
    }
    if (symbolArray.length == 0) {
        return true
    }
    return false
}

    console.log(bracesValid(str));




/*
String: Rotate String
Create a standalone function that accepts a string and an integer,
and rotates the characters in the string to the right by that given
integer amount.
*/

var str = "Hello World";

var rotateAmnt1 = 0;
var expected1 = "Hello World";

var rotateAmnt2 = 1;
var expected2 = "dHello Worl";

var rotateAmnt3 = 2;
var expected3 = "ldHello Wor";

var rotateAmnt4 = 4;
var expected4 = "orldHello W";

var rotateAmnt5 = 13;
var expected5 = "ldHello Wor";
/* 
Explanation: this is 2 more than the length so it ends up being the same
as rotating it 2 characters because after rotating every letter it gets back
to the original position.
*/

/**
* Rotates a given string's characters to the right by the given amount,
* wrapping characters to the beginning.
* - Time: O(?).
* - Space: O(?).
* @param {string} str
* @param {number} amnt The amount of characters in the given str to rotate to the
*    right.
* @returns {string} The string rotated by the given amount.
*/
function rotateStr(str, amnt) {
    var newStr = ""
    str.substring(amnt)

}
console.log(rotateStr('Hello World', rotateAmnt2));

// ************************************************************************************

/* 
  Create the function isRotation(str1,str2) that
  returns whether the second string is a rotation of the first.
*/

const strA1 = "ABCD";
const strB1 = "CDAB";
const expected1 = true;
// Explanation: if you start from A in the 2nd string, the letters are in the same order, just rotated

const strA2 = "ABCD";
const strB2 = "CDBA";
const expected2 = false;
// Explanation: all same letters in 2nd string, but out of order

/**
 * Determines whether the second string is a rotated version of the first.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether the second string is a rotated version of the 1st.
 */
function isRotation(s1, s2) {}



/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "        ";
const expected2 = "";

const str3 = "   hello world earth     ";
const expected3 = "hello world earth";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {

}




function trim(str) {
    for (var start = 0; start< str.length; start++) {
        if (str[start] != " ") {
            break
        } else if (start == str.length -1) {
            return ""
        }
    }
    for (var end = str.length-1; end >= 0; end--) {
        if (str[end] != " ") {
            break
        }
    }
    var returnString = ""
    for (var i = start; i <= end; i++) {
        returnString += str[i]
    }
    return returnString
}

// ************************************************************************

/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.
  Is there a quick way to determine if they aren't an anagram before spending more time?
  Given two strings
  return whether or not they are anagrams
*/

const two_strA1 = "yes3";
const two_strB1 = "3eys";
const two_expected1 = true;

const two_strA2 = "yes";
const two_strB2 = "eYs";
const two_expected2 = true;

const two_strA3 = "no";
const two_strB3 = "noo";
const two_expected3 = false;

const two_strA4 = "silent";
const two_strB4 = "listen";
const two_expected4 = true;

const two_strA5 = "not";
const two_strB5 = "noo";
const two_expected5 = false;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {}








function isAnagram(s1, s2) {
    if (s1.length != s2.length) {
        return false
    }
    str1Dict = {}
    str2Dict = {}
    s1 = s1.toLowerCase()
    s2 = s2.toLowerCase()
    for (var i = 0; i < s1.length; i++) {
        if (str1Dict.hasOwnProperty(s1[i])) {
            str1Dict[s1[i]]++
        } else {
            str1Dict[s1[i]] = 1
        }
        if (str2Dict.hasOwnProperty(s2[i])) {
            str2Dict[s2[i]]++
        } else {
            str2Dict[s2[i]] = 1
        }
    }
    for ([key, value] of Object.entries(str1Dict)) {
        if (value != str2Dict[key]) {
            return false
        }
    }
    return true
}
