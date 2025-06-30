function removeDuplicates(nums) {
  let = i = 0;
  let j = 0;
  if (nums.length === 0) {
    return 0;
  }
  while (j < nums.length) {
    if (nums[i] !== nums[j]) {
      i++;
      nums[i] = nums[j];
    }
  }
  return i + 1;
}

const nums = [1, 1, 2, 2, 3, 4];
const newLength = removeDuplicates(nums);
console.log(newLength);
console.log(nums.slice(0, newLength)); 