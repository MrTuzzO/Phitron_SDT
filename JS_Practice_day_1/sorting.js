let nums = [6, 10, 9, 15, 17, 12, 16, 3, 13, 18, 20, 1, 2, 11, 4, 8, 5, 19, 7, 14];

for (let i = 0; i < nums.length; i++){
    for (let j = i + 1; j < nums.length; j++){
        if (nums[i] > nums[j]) {
            let tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }
    }
}
console.log(nums);