import matplotlib.pyplot as plt
import base64
from io import BytesIO
from matplotlib import style
from matplotlib.widgets import Cursor,Button
import numpy as np
from textwrap import wrap

def graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph_ =base64.b64encode(image_png)
    graph_=graph_.decode('utf-8')
    buffer.close()
    return graph_

def plot(c,b):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,10))
    plt.title("sports compititions distribution with participants")
    plt.plot(c,b,'o',linewidth=5)
    #plt.pie(b,labels=ab,autopct='%1.1f%%',shadow=True,startangle=140)
    #plt.pie(ab,labels=b,autopct='%1.1f%%',shadow=True,startangle=140)
    #fig,ax=plt.subplot(figsize=(10,7))
    #plt.pie(y,labels=x,shadow=True,colors=colors,startangle=90,wedgeprops={'linewidth' : 1,'edgecolor':'green'},textprops=dict(color='magenta'))
    #plt.setp(autotexts,size=8,weight='bold')
    #plt.bar(ab,b,color='maroon',width=0.4)
    plt.xticks(rotation=45)
    #plt.plot(ab, label='first set')

    plt.xlabel('sports')
    plt.ylabel('style')
    style.use('ggplot')
    #fig,ax=plt.subplots()
    #cursor=Cursor(ax,horizOn=True,vertOn=True,color='green')
    plt.tight_layout()

    #ab= np.arange(1,8)
    
    #plt.text(7,3,"1:swimming")
    #plt.text(7,2.5,"1:swimming")
    #plt.text(7,2,"1:swimming")
    #plt.text(7,1.5,"1:swimming")
    #plt.text(7,1,"1:swimming")
    


    
    #ax=plt.subplots()
    #plt.xticks(['swimming','cricket','basketball','volleybol',' baseball','rummy','carrom','chesss','badminton','golf','tannis'])
    #plt.set_x(['swimming','cricket','basketball','volleybol',' baseball','rummy','carrom','chesss','badminton'])

# Set number of ticks for x-axis
    
# Set ticks labels for x-axis
    

    graph_=graph()
    return graph_







          
