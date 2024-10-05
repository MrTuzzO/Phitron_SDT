let year = 1900

if (year % 400 == 0) {
    console.log(`${year} is Leap Year`);
} else if (year % 100 == 0) {
    console.log(`${year} is not Leap Year`);
} else if (year % 4 == 0) {
    console.log(`${year} is Leap Year`);
} else {
    console.log(`${year} is not Leap Year`);
}