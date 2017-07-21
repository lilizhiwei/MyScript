var login = {
	userName: "13140023070",
	passWord: "123456",
};
function lz(c){
  var a = c.indexOf("：")>-1?c.split("：")[1]:c;
  a = a.replace(/\,/g,"");
  return Number(a);
}


