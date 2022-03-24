// js code

const find_two_sum = function (nums, target) {
  const nums_dict = {};
  for (let p = 0; p < nums.length; p++) {
    const current_map_val = nums_dict[nums[p]];

    if (current_map_val >= 0) {
      console.log([current_map_val, p]);
      return [current_map_val, p];
    } else {
      const number_to_find = target - nums[p];
      nums_dict[number_to_find] = p;
    }
  }
  return null;
};

nums = [3, 6, 7, 8, 9, 2, 4];
t = 12;

find_two_sum(nums, t);
