var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var [cod1, val1, n1] = lines.shift().split(' ')
var [cod2, val2, n2] = lines.shift().split(' ')

console.log('VALOR A PAGAR: R$ ' + ((val1*n1)+(val2*n2)).toFixed(2))