HTTP/1.1 200 OK
Date: Thu, 12 Nov 2020 10:48:13 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2020-11-12-10; expires=Sat, 12-Dec-2020 10:48:13 GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=204=K7Wc_-bL0yL8Vam2fRqCjhuEX9zBc1cEUzxtuV1nmvZhcjO5O6LkqSxFZ1jgl5R93z-Xgwqb2ybNz2-MQMLl_LJjdBXl3BVETffyGwix8PZGGa35MfMcrpUE0uG_mWNFNp08vMpBiOgms5_5hfr2d1BeoG92ZNbVVgz_mFJ1bGI; expires=Fri, 14-May-2021 10:48:13 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Connection: close
Transfer-Encoding: chunked

3bb7
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="X5O/+F/LnbgKYvLnlRCTHQ==">(function(){window.google={kEI:'7RKtX6_iCNaT4-EPuMmxwAI',kEXPI:'0,18168,183994,1151585,5662,731,223,5105,206,3204,10,1226,364,1499,612,205,383,246,5,1354,648,3452,50,264,3,65,594,175,216,263,21,545,323,113,451,1013,711,1864,7,328,363,950,1115347,1197791,100,391,7,328978,13677,4855,32692,16114,28684,9188,8384,4859,1361,9291,3022,3895,850,11033,1808,4020,978,7931,5297,2054,920,873,4192,6430,1141,7512,5875,4517,2778,918,2277,8,2796,1593,1279,2212,530,149,1103,840,517,1522,4258,312,1132,4,3,2063,606,2023,1777,143,377,1947,2229,93,328,1284,16,1988,939,2247,1812,1787,3229,2843,7,4773,826,469,6286,4455,641,7877,4928,108,3407,908,2,941,2614,2397,10745,3,346,230,970,44,1,820,7,4618,148,5990,6299,1686,4,1252,276,2304,217,1019,271,874,405,42,1818,445,1948,74,462,41,1,932,281,52,75,4,135,762,761,640,463,460,1555,4067,1035,1316,3,3280,1426,69,305,1015,1095,200,1514,603,2,692,1753,690,1968,491,3412,1,338,519,912,564,689,429,162,1173,2551,138,3095,990,52,622,2408,256,820,1,1392,850,80,575,800,638,1624,475,2,567,388,620,1793,2,1,1,1607,992,755,614,55,744,572,40,2268,958,170,98,508,2,881,319,230,174,413,11,731,665,337,1357,451,1255,161,70,1083,182,907,154,1999,100,249,52,60,272,147,513,50,29,975,515,334,59,777,341,22,277,196,556,2,735,113,221,46,42,1,431,1047,569,21,740,129,456,1472,542,1,947,2,200,587,269,227,86,932,338,164,164,142,621,357,546,1963,123,5735747,1874,1833,149,2,8798058,549,333,444,1,2,80,1,900,896,1,9,2,2551,1,748,141,59,736,563,1,4265,1,1,2,1017,9,305,3299,248,595,1,776,62,509,103,24,56,41,11,29,54,2,128,5,39,16,49,1,39,22,6,23958288,2716138,17691',kBL:'v90u'};google.sn='webhp';google.kHL='en-IN';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var c;a&&(!a.getAttribute||!(c=a.getAttribute("eid")));)a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&&(!a.getAttribute||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function(){delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(b);a.src=b;google.li=f+1}};google.logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&ei=")||(e="&ei="+google.getEI(d),-1==c.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));d="";!b&&google.cshid&&-1==c.search("&cshid=")&&"slh"!=a&&(d="&cshid="+google.cshid);b=b||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+c+e+f+"&zx="+google.time()+d;/^http:/i.test(b)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:b,glmm:1}),b="");return b};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-submitfalse");a="1"==c||"q"==c&&!a.elements.q.value?!0:!1}else a=!1;a&&(b.preventDefault(),b.stopPropagation())},!0);document.documentElement.addEventListener("click",function(b){var a;a:{for(a=b.target;a&&a!=document.documentElement;a=a.parentElement)if("A"==a.tagName){a="1"==a.getAttribute("data-nohref");break a}a=!1}a&&b.preventDefault()},!0);}).call(this);
var a=window.location,b=a.href.indexOf("#");if(0<=b){var c=a.href.substring(b+1);/(^|&)q=/.test(c)&&-1==c.indexOf("#")&&a.replace("/search?"+c.replace(/(^|&)fp=[^&]*/g,"")+"&cad=h")};</script><style>#gbar,#guser{font-size:13px;padding-top:1px !important;}#gbar{height:22px}#guser{padding-bottom:7px !important;text-align:right}.gbh,.gbd{border-top:1px solid #c9d7f1;font-size:1px}.gbh{height:0;position:absolute;top:24px;width:100%}@media all{.gb1{height:22px;margin-right:.5em;vertical-align:top}#gbar{float:left}}a.gb1,a.gb4{text-decoration:underline !important}a.gb1,a.gb4{color:#00c !important}.gbi .gb4{color:#dd8e27 !important}.gbf .gb4{color:#900 !important}
</style><style>body,td,a,p,.h{font-family:arial,sans-serif}body{margin:0;overflow-y:scroll}#gog{padding:3px 8px 0}td{line-height:.8em}.gac_m td{line-height:17px}form{margin-bottom:20px}.h{color:#1558d6}.q{color:#4b11a8}em{font-weight:bold;font-style:normal}.lst{height:25px;width:496px}.gsfi,.lst{font:18px arial,sans-serif}.gsfs{font:17px arial,sans-serif}.ds{display:inline-box;display:inline-block;margin:3px 0 4px;margin-left:4px}input{font-family:inherit}body{background:#fff;color:#000}a{color:#4b11a8;text-decoration:none}a:hover,a:active{text-decoration:underline}.fl a{color:#1558d6}a:visited{color:#4b11a8}.sblc{padding-top:5px}.sblc a{display:block;margin:2px 0;margin-left:13px;font-size:11px}.lsbb{background:#f8f9fa;border:solid 1px;border-color:#dadce0 #70757a #70757a #dadce0;height:30px}.lsbb{display:block}#WqQANb a{display:inline-block;margin:0 12px}.lsb{background:url(/images/nav_logo229.png) 0 -261px repeat-x;border:none;color:#000;cursor:pointer;height:30px;margin:0;outline:0;font:15px arial,sans-serif;vertical-align:top}.lsb:active{background:#dadce0}.lst:focus{outline:none}</style><script nonce="X5O/+F/LnbgKYvLnlRCTHQ=="></script></head><body bgcolor="#fff"><script nonce="X5O/+F/LnbgKYvLnlRCTHQ==">(function(){var src='/images/nav_logo229.png';var iesg=false;document.body.onload = function(){window.n && window.n();if (document.images){new Image().src=src;}
if (!iesg){document.f&&document.f.q.focus();document.gbqf&&document.gbqf.q.focus();}
}
})();</script><div id="mngb"><div id=gbar><nobr><b class=gb1>Search</b> <a class=gb1 href="http://www.google.co.in/imghp?hl=en&tab=wi">Images</a> <a class=gb1 href="http://maps.google.co.in/maps?hl=en&tab=wl">Maps</a> <a class=gb1 href="https://play.google.com/?hl=en&tab=w8">Play</a> <a class=gb1 href="http://www.youtube.com/?gl=IN&tab=w1">YouTube</a> <a class=gb1 href="https://news.google.com/?tab=wn">News</a> <a class=gb1 href="https://mail.google.com/mail/?tab=wm">Gmail</a> <a class=gb1 href="https://drive.google.com/?tab=wo">Drive</a> <a class=gb1 style="text-decoration:none" href="https://www.google.co.in/intl/en/about/products?tab=wh"><u>More</u> &raquo;</a></nobr></div><div id=guser width=100%><nobr><span id=gbn class=gbi></span><span id=gbf class=gbf></span><span id=gbe></span><a href="http://www.google.co.in/history/optout?hl=en" class=gb4>Web History</a> | <a  href="/preferences?hl=en" class=gb4>Settings</a> | <a target=_top id=gb_70 href="https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=http://www.google.com/&ec=GAZAAQ" class=gb4>Sign in</a></nobr></div><div class=gbh style=left:0></div><div class=gbh style=right:0></div></div><center><br clear="all" id="lgpd"><div id="lga"><img alt="Google" height="92" src="/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png" style="padding:28px 0 14px" width="272" id="hplogo"><br><br></div><form action="/search" name="f"><table cellpadding="0" cellspacing="0"><tr valign="top"><td width="25%">&nbsp;</td><td align="center" nowrap=""><input name="ie" value="ISO-8859-1" type="hidden"><input value="en-IN" name="hl" type="hidden"><input name="source" type="hidden" value="hp"><input name="biw" type="hidden"><input name="bih" type="hidden"><div class="ds" style="height:32px;margin:4px 0"><input class="lst" style="margin:0;padding:5px 8px 0 6px;vertical-align:top;color:#000" autocomplete="off" value="" title="Google Search" maxlength="2048" name="q" size="57"></div><br style="line-height:0"><span class="ds"><span class="lsbb"><input class="lsb" value="Google Search" name="btnG" type="submit"></span></span><span class="ds"><span class="lsbb"><input class="lsb" id="tsuid1" value="I'm Feeling Lucky" name="btnI" type="submit"><script nonce="X5O/+F/LnbgKYvLnlRCTHQ==">(function(){var id='tsuid1';document.getElementById(id).onclick = function(){if (this.form.q.value){this.checked = 1;if (this.form.iflsig)this.form.iflsig.disabled = false;}
else top.location='/doodles/';};})();</script><input value="AINFCbYAAAAAX60g_f0Zsov9cGYs3aAmxbE2_2EoUwbF" name="iflsig" type="hidden"></span></span></td><td class="fl sblc" align="left" nowrap="" width="25%"><a href="/advanced_search?hl=en-IN&amp;authuser=0">Advanced search</a></td></tr></table><input id="gbv" name="gbv" type="hidden" value="1"><script nonce="X5O/+F/LnbgKYvLnlRCTHQ==">(function(){var a,b="1";if(document&&document.getElementById)if("undefined"!=typeof XMLHttpRequest)b="2";else if("undefined"!=typeof ActiveXObject){var c,d,e=["MSXML2.XMLHTTP.6.0","MSXML2.XMLHTTP.3.0","MSXML2.XMLHTTP","Microsoft.XMLHTTP"];for(c=0;d=e[c++];)try{new ActiveXObject(d),b="2"}catch(h){}}a=b;if("2"==a&&-1==location.search.indexOf("&gbv=2")){var f=google.gbvu,g=document.getElementById("gbv");g&&(g.value=a);f&&window.setTimeout(function(){location.href=f},0)};}).call(this);</script></form><div id="gac_scont"></div><div style="font-size:83%;min-height:3.5em"><br><div id="prm"><style>.szppmdbYutt__middle-slot-promo{font-size:small;margin-bottom:32px}.szppmdbYutt__middle-slot-promo a.ZIeIlb{display:inline-block;text-decoration:none}.szppmdbYutt__middle-slot-promo img{border:none;margin-right:5px;vertical-align:middle}</style><div class="szppmdbYutt__middle-slot-promo" data-ved="0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQnIcBCAQ"><a class="NKcBbd" href="https://www.google.com/url?q=https://artsandculture.google.com/project/life-in-miniature%3Futm_source%3Dgoogle%26utm_medium%3Dhppromo%26utm_campaign%3DIndianMiniatures&amp;source=hpp&amp;id=19021425&amp;ct=3&amp;usg=AFQjCNHdkiz_MxN1nNxQxkUZK03cfVxBQQ&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ8IcBCAU" rel="nofollow">Discover Indian Miniatures</a><span>: Tiny paintings sharing big stories</span></div></div><div id="gws-output-pages-elements-homepage_additional_languages__als"><style>#gws-output-pages-elements-homepage_additional_languages__als{font-size:small;margin-bottom:24px}#SIvCob{display:inline-block;line-height:28px;}#SIvCob a{padding:0 3px;}.H6sW5{display:inline-block;margin:0 2px;white-space:nowrap}.z4hgWe{display:inline-block;margin:0 2px}</style><div id="SIvCob">Google offered in:  <a href="http://www.google.com/setprefs?sig=0_X-Ey_GoObKML8D6D1LPplv7Fdck%3D&amp;hl=hi&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ2ZgBCAc">&#2361;&#2367;&#2344;&#2381;&#2342;&#2368;</a>    <a href="http://www.google.com/setprefs?sig=0_X-Ey_GoObKML8D6D1LPplv7Fdck%3D&amp;hl=bn&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ2ZgBCAg">&#2476;&#2494;&#2434;&#2482;&#2494;</a>    <a href="http://www.google.com/setprefs?sig=0_X-Ey_GoObKML8D6D1LPplv7Fdck%3D&amp;hl=te&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ2ZgBCAk">&#3108;&#3142;&#3122;&#3137;&#3095;&#3137;</a>    <a href="http://www.google.com/setprefs?sig=0_X-Ey_GoObKML8D6D1LPplv7Fdck%3D&amp;hl=mr&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ2ZgBCAo">&#2350;&#2352;&#2366;&#2336;&#2368;</a>    <a href="http://www.google.com/setprefs?sig=0_X-Ey_GoObKML8D6D1LPplv7Fdck%3D&amp;hl=ta&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ2ZgBCAs">&#2980;&#2990;&#3007;&#2996;&#3021;</a>    <a href="http://www.google.com/setprefs?sig=0_X-Ey_GoObKML8D6D1LPplv7Fdck%3D&amp;hl=gu&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ2ZgBCAw">&#2711;&#2753;&#2716;&#2736;&#2750;&#2724;&#2752;</a>    <a href="http://www.google.com/setprefs?sig=0_X-Ey_GoObKML8D6D1LPplv7Fdck%3D&amp;hl=kn&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ2ZgBCA0">&#3221;&#3240;&#3277;&#3240;&#3233;</a>    <a href="http://www.google.com/setprefs?sig=0_X-Ey_GoObKML8D6D1LPplv7Fdck%3D&amp;hl=ml&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ2ZgBCA4">&#3374;&#3378;&#3375;&#3390;&#3379;&#3330;</a>    <a href="http://www.google.com/setprefs?sig=0_X-Ey_GoObKML8D6D1LPplv7Fdck%3D&amp;hl=pa&amp;source=homepage&amp;sa=X&amp;ved=0ahUKEwjvjKyw6vzsAhXWyTgGHbhkDCgQ2ZgBCA8">&#2602;&#2672;&#2588;&#2622;&#2604;&#2624;</a>  </div></div></div><span id="footer"><div style="font-size:10pt"><div style="margin:19px auto;text-align:center" id="WqQANb"><a href="/intl/en/ads/">Advertising Programs</a><a href="http://www.google.co.in/services/">Business Solutions</a><a href="/intl/en/about.html">About Google</a><a href="http://www.google.com/setprefdomain?prefdom=IN&amp;prev=http://www.google.co.in/&amp;sig=K_G_hR0RDg3vW-zE6VIluty0hwmgc%3D">Google.co.in</a></div></div><p style="font-size:8pt;color:#70757a">&copy; 2020 - <a href="/intl/en/policies/privacy/">Privacy</a> - <a href="/intl/en/policies/terms/">Terms</a></p></span></center><script nonce="X5O/+F/LnbgKYvLnlRCTHQ==">(function(){window.google.cdo={height:0,width:0};(function(){var a=window.innerWidth,b=window.innerHeight;if(!a||!b){var c=window.document,d="CSS1Compat"==c.compatMode?c.documentElement:c.body;a=d.clientWidth;b=d.clientHeight}a&&b&&(a!=google.cdo.width||b!=google.cdo.height)&&google.log("","","/client_204?&atyp=i&biw="+a+"&bih="+b+"&ei="+google.kEI);}).call(this);})();(function(){var u='/xjs/_/js/k\x3dxjs.hp.en.bEPbWVVbP10.O/m\x3dsb_he,d/am\x3dADxBHA/d\x3d1/rs\x3dACT90oGG9dShNiE27O0XJnnrcMHpcKFUVA';
var c=this||self,e=/^[\w+/_-]+[=]{0,2}$/,f=null,g=function(a){return(a=a.querySelector&&a.querySelector("script[nonce]"))&&(a=a.nonce||a.getAttribute("nonce"))&&e.test(a)?a:""},h=function(a){return a};var l;var n=function(a,b){this.a=b===m?a:""},m={};setTimeout(function(){var a=document;var b="SCRIPT";"application/xhtml+xml"===a.contentType&&(b=b.toLowerCase());b=a.createElement(b);a=u;if(void 0===l){var d=null;var k=c.trustedTypes;if(k&&k.createPolicy){try{d=k.createPolicy("goog#html",{createHTML:h,createScript:h,createScriptURL:h})}catch(p){c.console&&c.console.error(p.message)}l=d}else l=d}a=(d=l)?d.createScriptURL(a):a;a=new n(a,m);b.src=a instanceof n&&a.constructor===n?a.a:"type_error:TrustedResourceUrl";(a=b.ownerDocument&&b.ownerDocument.defaultView)&&
a!=c?a=g(a.document):(null===f&&(f=g(c.document)),a=f);a&&b.setAttribute("nonce",a);google.timers&&google.timers.load&&google.tick&&google.tick("load","xjsls");document.body.appendChild(b)},0);})();(function(){window.google.xjsu='/xjs/_/js/k\x3dxjs.hp.en.bEPbWVVbP10.O/m\x3dsb_he,d/am\x3dADxBHA/d\x3d1/rs\x3dACT90oGG9dShNiE27O0XJnnrcMHpcKFUVA';})();function _DumpException(e){throw e;}
function _F_installCss(c){}
(function(){google.jl={dw:false,em:[],emw:false,lls:'default',pdt:0,snet:true,uwp:true};})();(function(){var pmc='{\x22d\x22:{},\x22sb_he\x22:{\x22agen\x22:true,\x22cgen\x22:true,\x22client\x22:\x22heirloom-hp\x22,\x22dh\x22:true,\x22dhqt\x22:true,\x22ds\x22:\x22\x22,\x22ffql\x22:\x22en\x22,\x22fl\x22:true,\x22host\x22:\x22google.com\x22,\x22isbh\x22:28,\x22jsonp\x22:true,\x22msgs\x22:{\x22cibl\x22:\x22Clear Search\x22,\x22dym\x22:\x22D
2bf
id you mean:\x22,\x22lcky\x22:\x22I\\u0026#39;m Feeling Lucky\x22,\x22lml\x22:\x22Learn more\x22,\x22oskt\x22:\x22Input tools\x22,\x22psrc\x22:\x22This search was removed from your \\u003Ca href\x3d\\\x22/history\\\x22\\u003EWeb History\\u003C/a\\u003E\x22,\x22psrl\x22:\x22Remove\x22,\x22sbit\x22:\x22Search by image\x22,\x22srch\x22:\x22Google Search\x22},\x22nrft\x22:false,\x22ovr\x22:{},\x22pq\x22:\x22\x22,\x22refpd\x22:true,\x22rfs\x22:[],\x22sbas\x22:\x220 3px 8px 0 rgba(0,0,0,0.2),0 0 0 1px rgba(0,0,0,0.08)\x22,\x22sbpl\x22:16,\x22sbpr\x22:16,\x22scd\x22:10,\x22stok\x22:\x225i0He4aqqYGnYmf1KZIPCT4it1E\x22,\x22uhde\x22:false}}';google.pmc=JSON.parse(pmc);})();</script>        </body></html>
0

