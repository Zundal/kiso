const alphabet = "baekjoon";
const abc = "abcdefghijklmnopqrstuvwxyz";
temp = 0;

for (x in abc) {
  for (let y = 0; y < alphabet.length; y++) {
    if (abc[x] == alphabet[y]) {
      if (alphabet[y] !== alphabet[y - 1]) {
        temp = y;
      }
    }
  }
  console.log(temp);
  temp = -1;
}
