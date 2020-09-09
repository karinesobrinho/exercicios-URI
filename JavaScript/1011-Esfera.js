var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var r = parseInt(lines.shift())
var e = ((4/3)*(3.14159 * Math.pow(r,3))).toFixed(3)

console.log('VOLUME = '+ e)