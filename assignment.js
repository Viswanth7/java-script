//1.Function Declaration vs Function Expression
console.log(a());
console.log(b());
function a() {
  return "Function Declaration";
}
var b = function() {
  return "Function Expression";
};
