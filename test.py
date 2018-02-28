import math
from numpy import array, zeros, argmin, inf, equal, ndim
from matplotlib import pyplot as plt

PIC_NUM=23
xa=zeros((1,PIC_NUM))
ya=zeros((1,PIC_NUM))
k=0
SCATTER_RADIUS=40
for i in range(0,PIC_NUM-2,1):
    phi=(i+2.5)/(PIC_NUM*1.06)*math.pi*2
    x=SCATTER_RADIUS * (8*math.sin(phi)*  math.sin(phi)*  math.sin(phi))
    y=SCATTER_RADIUS *(6.5* math.cos(phi)-5*math.cos(2*phi)-2*math.cos(3*phi)-math.cos(4*phi))
    xa[0,k]=-math.floor(x)+SCATTER_RADIUS*8
    ya[0,k]=-math.floor(y)+SCATTER_RADIUS*8
    k=k+1

print(xa)

#plt.plot(xa,ya,'-o')
#plt.show()

f = open('test.html', 'w')
f.write("<!DOCTYPE html> \n")
f.write("<html lang=\"en\">\n")
f.write("<head>                                                                                                                        \n")
f.write("	<meta charset=\"UTF-8\">                                                                                                \n")
f.write("	  <meta name=\"viewport\" content=\"width=device-width,initial-scale=1, maximum-scale=1, minimum-scale=1, user-scalable=no\">\n")
f.write("	<style type=\"text/css\">                                                                                                    \n    ") 
f.write("	*{margin:0;padding: 0;}                                                                                                      \n  ")
f.write("    body{background-color: #e3b9b9;}                                                                                          \n    ")
f.write("    h1{margin-top: 20px; text-align: center;}                                                                                 \n    ")
f.write("	#div1{                                                                                                                       \n  ")
f.write("			width: 800px;                                                                                                            \n     	")
f.write("			height: 600px;                                                                                                           \n     	")
f.write("			margin: 20px auto;                                                                                                       \n     	")
f.write("			position: relative;                                                                                                      \n   ")
f.write("		}                                                                                                                          \n     ")
f.write("		#div1 img{                                                                                                                 \n     ")
f.write("			cursor: pointer;                                                                                                         \n   ")
f.write("			background-color: #fff;                                                                                                  \n   ")
f.write("			border: 1px solid #ddd;                                                                                                  \n   ")
f.write("			padding: 10px;                                                                                                           \n   ")
f.write("			box-shadow: 2px 2px 3px rgba(50,50,50,0.4);                                                                              \n   ")
f.write("			position: absolute;                                                                                                      \n   ")
f.write("			z-index: 1;                                                                                                              \n   ")
f.write("			transition: all 0.5s ease-in 0.2s;                                                                                       \n   ")
f.write("			-webkit-transition: all 0.5s ease-in 0.2s;      \n")                                                                       
f.write("			-moz-transition: all 0.5s ease-in 0.2s;                                                                                  \n   ")
f.write("			-o-transition: all 0.5s ease-in 0.2s;                                                                                    \n   ")
f.write("			-ms-transition: all 0.5s ease-in 0.2s;                                                                                   \n   ")
f.write("		}                                                                                                                          \n     ")
f.write("		#div1 img:hover{                                                                                                           \n     ")
f.write("			box-shadow: 10px 10px 15px rgba(50,50,50,0.4);                                                                           \n   ")
f.write("			transform:rotate(0deg) scale(1.5);                                                                                       \n   ")
f.write("			-webkit-transform:rotate(0deg) scale(1.5);                                                                               \n   ")
f.write("			-moz-transform:rotate(0deg) scale(1.5);                                                                                  \n   ")
f.write("			-o-transform:rotate(0deg) scale(1.5);                                                                                    \n   ")
f.write("			-ms-transform:rotate(0deg) scale(1.5);                                                                                   \n   ")
f.write("			z-index: 2;                                                                                                              \n   ")
f.write("		}                                                  \n")   
RotateA=5    
for pici in range(0,PIC_NUM-2,1):                                                               	
    strpic="		#pic"+str(pici)+"{\n"
    f.write(strpic)
    strpic="			left: "+str(xa[0,pici])+"px;                                       \n  "
    f.write(strpic)
    strpic="			top: "+str(ya[0,pici])+"px;                                        \n  "
    f.write(strpic)
    strpic="			-webkit-transform:rotate("+str(pici*RotateA)+"deg);                  \n"
    f.write(strpic)
    strpic="			-moz-transform:rotate("+str(pici*RotateA)+"deg);                     \n"
    f.write(strpic)
    strpic="			-o-transform:rotate("+str(pici*RotateA)+"deg);                       \n"
    f.write(strpic)
    strpic="			-ms-transform:rotate("+str(pici*RotateA)+"deg);                      \n"
    f.write(strpic)
    f.write("		}                                                  \n")
f.write("	</style>\n")
f.write("</head>\n")
f.write("<body>                                                                                 \n")
f.write("	<h1>Helllo World</h1>                                                                       \n  ")
f.write("	<div id=\"div1\">                                                                    \n  ")
for pici in range(0,PIC_NUM-2,1): 
    strpic="		<img src=\"images/"+str((pici%9)+1)+".jpg\" width=\"100px\" height=\"100px\" class=\"pic\" id=\"pic"+str(pici)+"\">       \n"
    f.write(strpic)
f.write("	</div>                                                                               \n")
f.write("</body>\n")
f.write("</html>\n")
f.close()                                                                                     
