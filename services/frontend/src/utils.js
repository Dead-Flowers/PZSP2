
export function generatePassword() {
    var length = 8,
        charset = "Zab1GBW53I1BCVvSy7Y94JHZO7EQyqwcHmuyd87MnnvfWUWULwLwCCkT6WbuNd",
        retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
        retVal += charset.charAt(Math.floor(Math.random() * n));
    }
  return retVal;
}