function reverseString(str) {
  let l = 0;
  let r = str.length - 1;
  while (l < r) {
    str[l] = str[l] + str[r];
    l++;
    r--;
  }

}