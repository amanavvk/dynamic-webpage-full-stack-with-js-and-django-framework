from matplotlib import colors
import matplotlib.pyplot as plt
import base64
from io import BytesIO


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    

    graph=base64.b64encode(image_png)
    graph=graph.decode("utf-8")
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,10))
    plt.title("sales of items")
    #plt.plot(x,y)
    plt.pie(y,labels=x,autopct='%1.1f%%',shadow=True,startangle=140)
    #fig,ax=plt.subplot(figsize=(10,7))
    #plt.pie(y,labels=x,shadow=True,colors=colors,startangle=90,wedgeprops={'linewidth' : 1,'edgecolor':'green'},textprops=dict(color='magenta'))
    #plt.setp(autotexts,size=8,weight='bold')
    #plt.bar(x,y,color='maroon',width=0.4)
    plt.xticks(rotation=45)
    plt.xlabel('items')
    plt.ylabel('price')
    plt.tight_layout()
    graph=get_graph()
    return graph