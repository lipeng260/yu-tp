import codecs

import xlrd

x1 = xlrd.open_workbook('tp.xlsx')
sheet1 = x1.sheet_by_index(0)
# 行，列 面积{3}
s3 =sheet1.cell_value(1, 1)
# 行，列 {0}
s0 = sheet1.cell_value(1, 4)
# 行，列 {1}
s1 = sheet1.cell_value(1, 5)
# 行，列 {2}
s2 = sheet1.cell_value(1, 3)

f = open('tp.html', 'ab')
encoder = codecs.getencoder('utf_16_le')

for i in range(1, 818):
    body = """<div class=WordSection1 style='layout-grid:21.15pt'>

<table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0 width=346
 style='border-collapse:collapse;mso-table-layout-alt:fixed;border:none;
 mso-border-alt:solid windowtext .5pt;mso-yfti-tbllook:1184;mso-padding-alt:
 0cm 5.4pt 0cm 5.4pt;mso-border-insideh:.5pt solid windowtext;mso-border-insidev:
 .5pt solid windowtext'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:13.7pt'>
  <td width=41 style='width:40.95pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.7pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:9.0pt;font-family:"Times New Roman";background:red;
  mso-highlight:red;mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=73 style='width:72.75pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.7pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:9.0pt;font-family:"Times New Roman";background:red;
  mso-highlight:red;mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=104 style='width:104.35pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.7pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:9.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=128 style='width:127.5pt;border:none;border-bottom:solid windowtext 1.0pt;
  mso-border-bottom-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:13.7pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:9.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;mso-yfti-lastrow:yes;height:19.7pt'>
  <td width=41 style='width:40.95pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:19.7pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:9.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'>{0}</span><span
  style='font-size:9.0pt;font-family:宋体;mso-font-kerning:0pt'>期</span><span
  lang=EN-US style='font-size:9.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'><o:p></o:p></span></p>
  </td>
  <td width=73 style='width:72.75pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:19.7pt'>
  <p class=MsoNormal align=center style='text-align:center'><span lang=EN-US
  style='font-size:9.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'>{1}</span><span
  style='font-size:9.0pt;font-family:宋体;mso-font-kerning:0pt'>号 </span><span
  lang=EN-US style='font-size:9.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>{2}</span><span style='font-size:9.0pt;font-family:宋体;mso-font-kerning:
  0pt'>室</span><span lang=EN-US style='font-size:9.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=104 style='width:104.35pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:19.7pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:9.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>建筑面积：</span><span lang=EN-US style='font-size:9.0pt;
  font-family:"Times New Roman";mso-font-kerning:0pt'> {3} </span><span
  style='font-size:9.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>㎡</span><span lang=EN-US style='font-size:9.0pt;
  font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=128 style='width:127.5pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:19.7pt'>
  <p class=MsoNormal align=center style='text-align:center'><span
  style='font-size:9.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>表决票序列号</span><span lang=EN-US style='font-size:9.0pt;
  font-family:"Times New Roman";mso-font-kerning:0pt'>20190803{4}<o:p></o:p></span></p>
  </td>
 </tr>
</table>

<p class=MsoNormal style='mso-line-height-alt:0pt'><b><span lang=EN-US
style='font-size:14.0pt;font-family:"Times New Roman"'><span
style='mso-spacerun:yes'> </span></span></b><span lang=EN-US><span
style='mso-spacerun:yes'>    </span></span><b><span lang=EN-US
style='font-size:14.0pt;font-family:"Times New Roman"'><o:p></o:p></span></b></p>

<p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
0pt'><b><span style='font-size:14.0pt;font-family:宋体'>上海市浦东新区香梅花园</span></b><b><span
lang=EN-US style='font-size:14.0pt;font-family:"Times New Roman"'>3-5</span></b><b><span
style='font-size:14.0pt;font-family:宋体'>期小区</span></b><span lang=EN-US><span
style='mso-spacerun:yes'>    </span></span><b><span lang=EN-US
style='font-size:14.0pt;font-family:"Times New Roman"'><o:p></o:p></span></b></p>

<p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
0pt'><b><span lang=EN-US style='font-size:14.0pt;font-family:"Times New Roman"'>2019</span></b><b><span
style='font-size:14.0pt;font-family:宋体'>年第一次业主大会表决票</span></b><span lang=EN-US><span
style='mso-spacerun:yes'>    </span></span><b><span lang=EN-US
style='font-size:14.0pt;font-family:"Times New Roman"'><o:p></o:p></span></b></p>

<p class=MsoNormal align=center style='text-align:center;text-indent:56.0pt;
mso-char-indent-count:4.0;mso-line-height-alt:0pt'><b><span lang=EN-US
style='font-size:14.0pt;font-family:"Times New Roman"'><span
style='mso-spacerun:yes'> </span></span></b><span lang=EN-US><span
style='mso-spacerun:yes'>    </span></span><b><span lang=EN-US
style='font-size:14.0pt;font-family:"Times New Roman"'><o:p></o:p></span></b></p>

<p class=MsoNormal align=left style='text-align:left;mso-line-height-alt:0pt'><span
style='font-size:11.0pt;font-family:宋体'>尊敬的业主：</span><span lang=EN-US><span
style='mso-spacerun:yes'>    </span></span><span lang=EN-US style='font-size:
11.0pt;font-family:"Times New Roman"'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;text-indent:22.0pt;
mso-line-height-alt:0pt'><span style='font-size:11.0pt;font-family:宋体'>根据相关法律、法规和文件的相关规定以及本小区《管理规约》及《议事规则》的约定，本小区采用书面征求意见的方式召开</span><span
lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman"'>2019</span><span
style='font-size:11.0pt;font-family:宋体'>年第一次业主大会，就物业服务企业和服务标准、服务内容进行表决。</span><span
lang=EN-US><span style='mso-spacerun:yes'>    </span></span><span lang=EN-US
style='font-size:11.0pt;font-family:"Times New Roman"'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;text-indent:22.0pt;
mso-line-height-alt:0pt'><span style='font-size:11.0pt;font-family:宋体'>待表决事项的具体内容及计票规则请见所附《关于召开</span><span
lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman"'>2019</span><span
style='font-size:11.0pt;font-family:宋体'>年第一次业主大会的公告》。</span><span lang=EN-US><span
style='mso-spacerun:yes'>   </span><span style='mso-spacerun:yes'> </span></span><span
lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman"'><o:p></o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;text-indent:22.0pt;
mso-line-height-alt:0pt'><span lang=EN-US style='font-size:11.0pt;font-family:
"Times New Roman"'><span style='mso-spacerun:yes'> </span></span><span
lang=EN-US><span style='mso-spacerun:yes'>    </span></span><span lang=EN-US
style='font-size:11.0pt;font-family:"Times New Roman"'><o:p></o:p></span></p>

<div align=center>

<table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0 width=364
 style='border-collapse:collapse;mso-table-layout-alt:fixed;border:none;
 mso-border-alt:solid windowtext .5pt;mso-yfti-tbllook:1184;mso-padding-alt:
 0cm 5.4pt 0cm 5.4pt;mso-border-insideh:.5pt solid windowtext;mso-border-insidev:
 .5pt solid windowtext'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:21.15pt'>
  <td width=172 style='width:172.3pt;border:solid windowtext 1.0pt;mso-border-alt:
  solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:21.15pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>表决事项</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border:solid windowtext 1.0pt;border-left:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:21.15pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>同意</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=64 style='width:63.75pt;border:solid windowtext 1.0pt;border-left:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:21.15pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>反对</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border:solid windowtext 1.0pt;border-left:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:solid windowtext .5pt;
  mso-border-right-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;
  height:21.15pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>弃权</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:25.65pt'>
  <td width=172 style='width:172.3pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=left style='text-align:left;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>一、修改本小区《管理规约》</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.75pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;height:25.65pt'>
  <td width=172 style='width:172.3pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=left style='text-align:left;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>二、恢复小区三期车库出入口的双向通行</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.75pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:3;height:25.65pt'>
  <td width=172 style='width:172.3pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=left style='text-align:left;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>三、门禁对讲系统及地弹簧的更换维修</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.75pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:4;height:25.65pt'>
  <td width=172 style='width:172.3pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=left style='text-align:left;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>四、电梯及一楼公告栏广告</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.75pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:5;height:25.65pt'>
  <td width=172 style='width:172.3pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=left style='text-align:left;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>五、网球场广告</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.75pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:6;mso-yfti-lastrow:yes;height:25.65pt'>
  <td width=172 style='width:172.3pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=left style='text-align:left;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>六、公共部位的车位翻新及地面下沉维修</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.75pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
  <td width=64 style='width:63.8pt;border-top:none;border-left:none;border-bottom:
  solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;mso-border-top-alt:
  solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;mso-border-bottom-alt:
  solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;padding:
  0cm 5.4pt 0cm 5.4pt;height:25.65pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
</table>

</div>

<p class=MsoNormal align=left style='text-align:left'><span lang=EN-US
style='font-family:"Times New Roman"'><span style='mso-spacerun:yes'> </span></span><span
lang=EN-US><span style='mso-spacerun:yes'>    </span></span><span lang=EN-US
style='font-family:"Times New Roman"'><o:p></o:p></span></p>

<div align=center>

<table class=MsoNormalTable border=1 cellspacing=0 cellpadding=0 width=415
 style='border-collapse:collapse;mso-table-layout-alt:fixed;border:none;
 mso-border-alt:solid windowtext .5pt;mso-yfti-tbllook:1184;mso-padding-alt:
 0cm 5.4pt 0cm 5.4pt;mso-border-insideh:.5pt solid windowtext;mso-border-insidev:
 .5pt solid windowtext'>
 <tr style='mso-yfti-irow:0;mso-yfti-firstrow:yes;height:43.1pt'>
  <td width=415 colspan=4 style='width:414.65pt;border:solid windowtext 1.0pt;
  mso-border-alt:solid windowtext .5pt;padding:0cm 5.4pt 0cm 5.4pt;height:43.1pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span style='font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>请您填写相关信息并签名</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span style='font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>（签名业主需为房产证权利人一栏有名字的成年人）</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:1;height:31.4pt'>
  <td width=71 style='width:71.0pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:31.4pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>室号</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=154 style='width:154.15pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:31.4pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><u><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'>&nbsp;{0}&nbsp;</span></u><span style='font-size:11.0pt;
  font-family:宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:
  "Times New Roman";mso-bidi-font-family:"Times New Roman";mso-font-kerning:
  0pt'>期</span><u><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'>&nbsp;{1} </span></u><span style='font-size:11.0pt;
  font-family:宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:
  "Times New Roman";mso-bidi-font-family:"Times New Roman";mso-font-kerning:
  0pt'>号</span><u><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'> {2} </span></u><span style='font-size:11.0pt;
  font-family:宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:
  "Times New Roman";mso-bidi-font-family:"Times New Roman";mso-font-kerning:
  0pt'>室</span><span lang=EN-US><span style='mso-spacerun:yes'>  </span>&nbsp; </span><u><span
  lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'><o:p></o:p></span></u></p>
  </td>
  <td width=71 style='width:70.85pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:31.4pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>业主</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span style='font-size:11.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>签名</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:11.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
  <td width=119 style='width:118.65pt;border-top:none;border-left:none;
  border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:31.4pt'>
  <p class=MsoNormal align=center style='text-align:center;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:11.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  </td>
 </tr>
 <tr style='mso-yfti-irow:2;mso-yfti-lastrow:yes;height:4.5pt'>
  <td width=71 style='width:71.0pt;border:solid windowtext 1.0pt;border-top:
  none;mso-border-top-alt:solid windowtext .5pt;mso-border-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:4.5pt'>
  <p class=MsoNormal align=center style='margin-top:0cm;margin-right:5.65pt;
  margin-bottom:0cm;margin-left:5.65pt;margin-bottom:.0001pt;text-align:center;
  mso-line-height-alt:0pt'><span style='font-size:10.0pt;font-family:宋体;
  mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:"Times New Roman";
  mso-bidi-font-family:"Times New Roman";mso-font-kerning:0pt'>注</span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'><span style='mso-spacerun:yes'>   </span></span><span style='font-size:
  10.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:
  "Times New Roman";mso-bidi-font-family:"Times New Roman";mso-font-kerning:
  0pt'>意</span><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><o:p></o:p></span></p>
  <p class=MsoNormal align=center style='margin-top:0cm;margin-right:5.65pt;
  margin-bottom:0cm;margin-left:5.65pt;margin-bottom:.0001pt;text-align:center;
  mso-line-height-alt:0pt'><span lang=EN-US style='font-size:10.0pt;font-family:
  "Times New Roman";mso-font-kerning:0pt'><span style='mso-spacerun:yes'>  
  </span></span><span style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:
  "Times New Roman";mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:
  "Times New Roman";mso-font-kerning:0pt'>事</span><span lang=EN-US
  style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><span
  style='mso-spacerun:yes'>   </span></span><span style='font-size:10.0pt;
  font-family:宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:
  "Times New Roman";mso-bidi-font-family:"Times New Roman";mso-font-kerning:
  0pt'>项</span><span lang=EN-US><span style='mso-spacerun:yes'>  </span>&nbsp; </span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'><o:p></o:p></span></p>
  </td>
  <td width=344 colspan=3 valign=top style='width:343.65pt;border-top:none;
  border-left:none;border-bottom:solid windowtext 1.0pt;border-right:solid windowtext 1.0pt;
  mso-border-top-alt:solid windowtext .5pt;mso-border-top-alt:solid windowtext .5pt;
  mso-border-bottom-alt:solid windowtext .5pt;mso-border-right-alt:solid windowtext .5pt;
  padding:0cm 5.4pt 0cm 5.4pt;height:4.5pt'>
  <p class=MsoNormal style='mso-line-height-alt:0pt'><span lang=EN-US
  style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  <p class=MsoNormal style='mso-line-height-alt:0pt'><span lang=EN-US
  style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>
  <p class=MsoNormal style='line-height:16.0pt;mso-line-height-rule:exactly'><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>1.</span><span style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:
  "Times New Roman";mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:
  "Times New Roman";mso-font-kerning:0pt'>请在上方表格中“同意”、“反对”或“弃权”下方空格处打</span><span
  style='font-size:10.0pt;font-family:宋体;mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>“√”</span><span style='font-size:10.0pt;font-family:
  宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:"Times New Roman";
  mso-bidi-font-family:"Times New Roman";mso-font-kerning:0pt'>。表格中只能打一个“√”，多选或涂改将使所在表格成为无效表决。</span><span
  lang=EN-US><span style='mso-spacerun:yes'>  </span>&nbsp; </span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'><o:p></o:p></span></p>
  <p class=MsoNormal style='line-height:16.0pt;mso-line-height-rule:exactly'><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>2.</span><span style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:
  "Times New Roman";mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:
  "Times New Roman";mso-font-kerning:0pt'>请用水笔或圆珠笔填写，用铅笔填写将使所在表格成为无效表决。</span><span
  lang=EN-US><span style='mso-spacerun:yes'>  </span>&nbsp; </span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'><o:p></o:p></span></p>
  <p class=MsoNormal style='line-height:16.0pt;mso-line-height-rule:exactly'><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>3.</span><span style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:
  "Times New Roman";mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:
  "Times New Roman";mso-font-kerning:0pt'>请在投票前仔细阅读所附《关于召开</span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>2019</span><span style='font-size:10.0pt;font-family:宋体;mso-font-kerning:
  0pt'>年第</span><span style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:
  "Times New Roman";mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:
  "Times New Roman";mso-font-kerning:0pt'>一次业主大会的公告》。</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  <p class=MsoNormal style='line-height:16.0pt;mso-line-height-rule:exactly'><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>4.</span><span style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:
  "Times New Roman";mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:
  "Times New Roman";mso-font-kerning:0pt'>请您在填好后将此表决票交还给您所在楼的业主召集人（楼组长）。您也可以在</span><u><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'> 2019&nbsp;</span></u><span style='font-size:10.0pt;font-family:宋体;
  mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:"Times New Roman";
  mso-bidi-font-family:"Times New Roman";mso-font-kerning:0pt'>年</span><u><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>&nbsp;8&nbsp;</span></u><span style='font-size:10.0pt;font-family:宋体;
  mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:"Times New Roman";
  mso-bidi-font-family:"Times New Roman";mso-font-kerning:0pt'>月</span><u><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>&nbsp;18&nbsp;</span></u><span style='font-size:10.0pt;font-family:宋体;
  mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:"Times New Roman";
  mso-bidi-font-family:"Times New Roman";mso-font-kerning:0pt'>日</span><u><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>&nbsp;12:00&nbsp;</span></u><span style='font-size:10.0pt;font-family:
  宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:"Times New Roman";
  mso-bidi-font-family:"Times New Roman";mso-font-kerning:0pt'>前，将此表决票自行投入设在小区的固定票箱内（分别位于</span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>3</span><span style='font-size:10.0pt;font-family:宋体;mso-font-kerning:
  0pt'>、</span><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'>4</span><span style='font-size:10.0pt;font-family:宋体;
  mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:"Times New Roman";
  mso-bidi-font-family:"Times New Roman";mso-font-kerning:0pt'>期大门和</span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>5</span><span style='font-size:10.0pt;font-family:宋体;mso-font-kerning:
  0pt'>期大门</span><span style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:
  "Times New Roman";mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:
  "Times New Roman";mso-font-kerning:0pt'>处）。</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  <p class=MsoNormal style='line-height:16.0pt;mso-line-height-rule:exactly'><span
  lang=EN-US><o:p>&nbsp;</o:p></span></p>
  <p class=MsoNormal style='line-height:16.0pt;mso-line-height-rule:exactly'><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'><o:p>&nbsp;</o:p></span></p>
  <p class=MsoNormal style='text-indent:185.0pt;mso-char-indent-count:18.5;
  mso-line-height-alt:0pt'><span style='font-size:10.0pt;font-family:宋体;
  mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:"Times New Roman";
  mso-bidi-font-family:"Times New Roman";mso-font-kerning:0pt'>上</span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'><span style='mso-spacerun:yes'>     </span></span><span
  style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>海</span><span lang=EN-US style='font-size:10.0pt;
  font-family:"Times New Roman";mso-font-kerning:0pt'><span
  style='mso-spacerun:yes'>     </span></span><span style='font-size:10.0pt;
  font-family:宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:
  "Times New Roman";mso-bidi-font-family:"Times New Roman";mso-font-kerning:
  0pt'>市</span><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><span style='mso-spacerun:yes'>     </span></span><span
  style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>浦</span><span lang=EN-US style='font-size:10.0pt;
  font-family:"Times New Roman";mso-font-kerning:0pt'><span
  style='mso-spacerun:yes'>     </span></span><span style='font-size:10.0pt;
  font-family:宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:
  "Times New Roman";mso-bidi-font-family:"Times New Roman";mso-font-kerning:
  0pt'>东</span><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><span style='mso-spacerun:yes'>    </span></span><span
  style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>新</span><span lang=EN-US style='font-size:10.0pt;
  font-family:"Times New Roman";mso-font-kerning:0pt'><span
  style='mso-spacerun:yes'>    </span></span><span style='font-size:10.0pt;
  font-family:宋体;mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:
  "Times New Roman";mso-bidi-font-family:"Times New Roman";mso-font-kerning:
  0pt'>区</span><span lang=EN-US><span style='mso-spacerun:yes'>  </span>&nbsp; </span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'><o:p></o:p></span></p>
  <p class=MsoNormal style='text-indent:185.0pt;mso-char-indent-count:18.5;
  mso-line-height-alt:0pt'><span style='font-size:10.0pt;font-family:宋体;
  mso-ascii-font-family:"Times New Roman";mso-hansi-font-family:"Times New Roman";
  mso-bidi-font-family:"Times New Roman";mso-font-kerning:0pt'>香梅花园</span><span
  lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:
  0pt'>3-5</span><span style='font-size:10.0pt;font-family:宋体;mso-font-kerning:
  0pt'>期小区业主委员会</span><span lang=EN-US><span style='mso-spacerun:yes'> 
  </span>&nbsp; </span><span lang=EN-US style='font-size:10.0pt;font-family:
  "Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  <p class=MsoNormal align=right style='text-align:right;mso-line-height-alt:
  0pt'><span lang=EN-US style='font-size:10.0pt;font-family:"Times New Roman";
  mso-font-kerning:0pt'><span style='mso-spacerun:yes'>   </span>2019</span><span
  style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>年</span><span lang=EN-US style='font-size:10.0pt;
  font-family:"Times New Roman";mso-font-kerning:0pt'>8</span><span
  style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>月</span><span lang=EN-US style='font-size:10.0pt;
  font-family:"Times New Roman";mso-font-kerning:0pt'>1</span><span
  style='font-size:10.0pt;font-family:宋体;mso-ascii-font-family:"Times New Roman";
  mso-hansi-font-family:"Times New Roman";mso-bidi-font-family:"Times New Roman";
  mso-font-kerning:0pt'>日</span><span lang=EN-US><span
  style='mso-spacerun:yes'>  </span>&nbsp; </span><span lang=EN-US
  style='font-size:10.0pt;font-family:"Times New Roman";mso-font-kerning:0pt'><o:p></o:p></span></p>
  </td>
 </tr>
</table>

</div>

<p class=MsoNormal align=left style='text-align:left;mso-pagination:widow-orphan'><span
lang=EN-US style='font-family:"Times New Roman"'><o:p>&nbsp;</o:p></span></p>

<p class=MsoNormal align=left style='text-align:left;mso-pagination:widow-orphan'><span
lang=EN-US style='font-family:"Times New Roman";mso-fareast-font-family:"Times New Roman";
mso-font-kerning:0pt'><o:p>&nbsp;</o:p></span></p>

</div>"""
    s3 = sheet1.cell_value(i, 1)
    # 行，列 {0}
    s0 = sheet1.cell_value(i, 4)
    # 行，列 {1}
    s1 = sheet1.cell_value(i, 5)
    # 行，列 {2}
    s2 = sheet1.cell_value(i, 3)
    f.write(encoder(body.format(int(s0), int(s1), int(s2), s3, '0' * (3-len(str(i))) + str(i)))[0])

end = """
</body>
</html>
"""
f.write(encoder(end)[0])
f.close()
