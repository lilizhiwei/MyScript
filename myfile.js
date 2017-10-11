var login = {
	userName: "13140023070",
	passWord: "123456",
	url: "https://www.yyddd.com/pc/login.html",
	url1: "https://www.yyddd.com/mobile",
	url2: "https://www.yyddd.com/cash/#page/login"
};
function lz(c){
  var a = c.indexOf("：")>-1?c.split("：")[1]:c;
  a = a.replace(/\,/g,"");
  return Number(a);
}


