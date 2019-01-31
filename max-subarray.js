var maxSubArray = function (nums) {
  let runningTotal = [];
  if (nums.length == 1) {
    return nums[0];
  }

  for (var i = 1; i < nums.length; i++) {

    if (nums[i - 1] > nums[i]) {
      runningTotal.push(nums[i - 1]);
    }

    nums[i] = Math.max(nums[i], (nums[i] + nums[i - 1]));
    runningTotal.push(nums[i])
  }
  return Math.max(...runningTotal);
};

maxSubArray([-1, -2]);
maxSubArray([1]);
maxSubArray([-2, -1, 1, -3, 4, -1, 2, 1, -5, 4]);
