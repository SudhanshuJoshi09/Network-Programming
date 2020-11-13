HTTP/1.1 200 OK
Date: Fri, 13 Nov 2020 08:14:19 GMT
Server: Apache
Upgrade: h2,h2c
Connection: Upgrade, close
Last-Modified: Thu, 28 Nov 2019 10:07:41 GMT
Accept-Ranges: bytes
Content-Length: 4166
Vary: Accept-Encoding,User-Agent
Content-Type: text/html

<?xml version="1.0" encoding="iso-8859-1"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv=Content-Type content="text/html; charset=iso-8859-1">
<meta http-equiv="refresh" content="300; URL=/index.htm">
<title>Dr Ram P Rustagi's Website </title>
<style type="text/css">
body {
background-color:#efc;
color: brown;
font-size: 14px;
}
h1, h2, h3, h4, h5, h6{
margin:5px;
}
h1 {text-decoration: underline;
}
.floatright {float: right; height:100px; width: 125px;}
.clear {clear:both;}
p {
color: black;
}
</style>
</head>

<body>
<p><img class="floatright" src="/images/RPR-PP-Photo.jpg" alt="Photo of RP Rustagi">
<h1>Dr Ram P Rustagi</h1>
<hr size=2 width="100%" align=center>

<h2 class="clear"><a name=top></a>Contents</h2>
<ul type=disc>
<li tab-stops:list .5in'><a href="#contactinfo"><b>Contact Information</b></a></li>
<li tab-stops:list .5in'><a href="#bio"><b>Biographical Information</b></a></li>
<li tab-stops:list .5in'><a href="#interests"><b> Interests</b></a></li>
</ul>

<hr size=1 width="100%" align=center>
<hr size=2 width="100%" align=center>

<h2><a name=contactinfo></a>Contact Information</h2>
<p><b>Electronic mail address</b> <br>
<a href="mailto:ram@rprustagi.com">ram@rprustagi.com</a>
</p>
<p><b>Web Address</b> <br>
<a href="//www.rprustagi.com">www.rprustagi.com</a> </p>

<p><b>Phone</b> <br>
<!-- Work: +91-80-26721983 x715<br> -->
Home: +91-80-4208-7127
</p>

<p><strong>Postal Address</strong><b><br>
</b>I-205, Mantri Tranquil Apts<br>
Gubbalala, Subramanyapura Post<br>
Bengaluru - 560 061<br>
India</p>
<hr size=2 width="100%" align=center>

<h2><a name=bio></a>Biographical Information</h2>

<ul type=disc>
<li tab-stops:list .5in'>
Ph.D,  Dept. of Comp. Sc. & Engg, <a href="http://www.cse.iitd.ernet.in">I I T Delhi</a></li>
<li tab-stops:list .5in'>
M.Tech, <a href="http://www.iisc.ac.in">I I Sc, Bangalore</a></li>
</ul>

<p><strong>Current Engagement :
<b> Key Resource Person, KS Group of Institutions, and  <a href="hhttp://www.ksit.ac.in/cse_dept.html"> Professor, CSE Dept, KSIT Bangalore</a>
<br />
Profile and experience information: <a href="/pub/professional-summary.pdf">Professional Summary</a><br />
</p>

<hr size=2 width="100%" align=center>
<h2><a name=interests></a>Interests</h2>

<ul type=disc>
 <li tab-stops:list .5in'>Network and Security</li>
 <li tab-stops:list .5in'>Application Performance - Design, Optimization and Scaling</li>
 <li tab-stops:list .5in'>Machine Learning, Analytics, Data Mining</li>
 <li tab-stops:list .5in'>Algorithms Design</li>
</ul>

<hr size=2 width="100%" align=center>
<h2><a name=Publications> </a>Publications</h2>
<ul> Magazine Articles
  <li><a href="/ELNT/Experiential-Learning.html"> Articles in ACCS Magazine - Advanced Communications and Computing</a>
  </li>
  <li>Research Publications</a>
  </li>
</ul>

<h2>Workshops, Tutorials, Invited Talks </h2>
<h3><a href="workshops">Workshops</a></h3>
  <ul>
    <li>In collaboration with <a href="workshops/ieee">IEEE Computer Society, India</a></li>
    <li>In collaboration with <a href="workshops/bites">BITES, Karnataka</a></li>
    <li>Others <a href="workshops/others">Individual Institutions and Misc</a></li>
  </ul>
<h3><a href="talks">Invited Talks</a></h3>
  <ul>
    <li>2019-11-26: PES University, Bangalore <a href="talks/2019-11-26-PESU_MCA_Applications-of-Networking.pdf">Applications of Computer Networks</a></li>
    <li>2019-10-11: ACM Compute 2019, Goa <a href="talks/2019-10-11-EL-Teaching-CN.pdf">Experiential Learning Approach to teaching Computer Networks</a></li>
    <li>2018-04-20: DSCE, Bangalore <a href="talks/2018-04-20-DSCE.pdf">Networking: Past, Present and Future</a></li>
    <li>2018-12-10: MS Ramaiah Institute of Technology, Bangalore <a href="/talks/2018-12-10-MSRIT-MITM.pdf">Man In The Middle attack</a></li>
    <li>2019-08-23: DSCE, Bangalore:  <a href="/talks/2019-08-23-SDN-ML-Overview.pdf">Software Defined Networking with Machine Learning</a></li
</ul>
<h5>Copyright Ram P. Rustagi</h5>

<h5>Last revised: Nov 28, 2019 </h5>

</body>
</html>
