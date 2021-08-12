from tkinter import*
import requests

class weather:
    def __init__(self):
        self.root=Tk()
       
        self.root.title("Live Weather Forecast")
        self.root.minsize(400,700)
        self.root.maxsize(400,700)

        self.root.configure(background="#00a65a")
       
        self.label1=Label(self.root,text="Weather Forecast",bg="#00a65a",fg="#fff")
        self.label1.configure(font=("Roman",22,"bold"))
        self.label1.pack(pady=(30,10))

        self.City=Entry(self.root)
        self.City.pack(ipadx=40,ipady=5)
       
        self.click=Button(self.root,text="Enter City",bg="#fff",fg="#000",width=23,height=2,command=lambda:self.__fetch())
        self.click.configure(font=("Constantia",10,"bold"))
        self.click.pack(pady=(10,20))

        self.result=Label(self.root,text="",bg="#00a65a",fg="#fff")
        self.result.configure(font=("Constantia",12,"bold"))
        self.result.pack(pady=(5,10))

       
        self.root.mainloop()



    def __fetch(self):
        city=self.City.get()
        url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=8320daf3dd5b9489474dd07bb048bab3".format(self.City.get().upper())
        try:
            response=requests.get(url)
            data=response.json()
        #print(data["main"])
        #print(type(data["main"]))
            labeltext = ""
            for i in list(data["main"].keys()):
                labeltext += i + ": " + str(data["main"][i])+ "\n"
            #self.label3=Label(self.root,text="{}".format(labeltext),bg="#00a65a",fg="#fff")
            #self.label3.configure(text="{}".format(labeltext))
            #self.label3.pack()
        except:
            labeltext = "WRONG CITY"
       
           
        self.result.configure(text=labeltext)
"""
        //city=""
        //for i in data['main']:
          //  city= city + int(i['temp'])+" | " +i['humidity'] + " | " +i['pressure']

        //self.result.configure(text=city)
"""
       
           
obj=weather()
