import webbrowser
import os
 
f = open('GFG.html', 'w')
html_template = """
<html>
<head>
    <link rel="icon" type="image/jpg" href="ph3.jpg">
</head>
<body bgColor="#f1916d">
    <div style="text-align: center;">
        <img width="300" src="ph8.jpg">
        <img width="300" src="ph6.jpg">
        <h1><b><u><i>My Personal Page</i></u></b></h1>
                <div style="text-align: Center;">
        <img width="300" src="ph.jpg.jpg">
    </div>
    <div style="text-align: left;">
<p><b>Name:</b> Bassem Al Wazani</p>
<p><b>From:</b> Jordan</p>
<p><b>DOB:</b>11/9/2005</p>
<p><b>University:</b>
    <a href="https://www.philadelphia.edu.jo/ar/">Philadelphia</a>
</p>
<p><b>Majors:</b>
    <a href="https://www.instagram.com/p/Cn_tYLIMke-/?utm_source=ig_web_copy_link&igsh=MzRlODBiNWFlZA=="> majors </a>
    <p><b>Introduction:</b>
        <p> I was born in KSA, studied and obtained my high school from there. I moved back to Jordan lately in 2023 and joined Philadelphia University to study Cyber Security</p>
</div>
</p>
</body>
</html>
"""
f.write(html_template)
f.close()
filename = 'file:///'+os.getcwd()+'/' + 'GFG.html'
webbrowser.open_new_tab(filename)
