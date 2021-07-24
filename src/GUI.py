import tkinter as tk
from tkinter.constants import W
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (MenuPage,FirstPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("MenuPage")
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="brown")
        self.controller = controller
        self.controller.title("")
        self.controller.state('zoomed')
        headingLabel1 = tk.Label(self, text="Soilytics", font=(
            'Times New Roman', 45), fg='white', bg='brown')
        headingLabel1.pack(pady=25)
        space = tk.Label(self, height=4, bg='brown')
        space.pack()
        main_menu = tk.Label(self, text='Main Menu', font=(
            'Times New Roman', 25), fg='white', bg='brown')
        main_menu.pack()
        selection = tk.Label(self, text='Please make a selection', font=(
            'Times New Roman', 25), fg='white', bg='brown', anchor='w')
        selection.pack(fill='x')
        button_frame = tk.Frame(self, bg='brown')
        button_frame.pack(fill="both", expand=True)
        def FirstP():
            controller.show_frame("FirstPage")
        show_database=tk.Button(button_frame,text="Show First Page",command=FirstP,height=5,width=50)
        show_database.grid(row=0,column=0,pady=5)
class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='brown')
        self.controller = controller
        headingLabel1 = tk.Label(self, text="Soilytics", font=(
            'Times New Roman', 45), fg='white', bg='brown')
        headingLabel1.pack(pady=25)
        def MenuPage():
            controller.show_frame("MenuPage")
        button=tk.Button(self,text="<-----",command=MenuPage,height=2,width=20)
        button.pack(pady=25,anchor=W)
        button_frame = tk.Frame(self, bg='brown')
        button_frame.pack(fill="both", expand=True)
        city_label=tk.Label(button_frame,text="Enter City",height=5,width=10,bg="brown")
        city_label.grid(row=1,column=0,pady=5,padx=20)
        country_label=tk.Label(button_frame,text="Enter Country",height=5,width=20,bg="brown")
        country_label.grid(row=2,column=0,pady=5,padx=20)
        city=tk.Entry(button_frame,font=('Times New Roman',20))
        city.grid(row=1,column=1,pady=5,padx=20)
        country=tk.Entry(button_frame,font=('Times New Roman',20))
        country.grid(row=2,column=1,pady=5,padx=20)
        def search():
            from geopy.geocoders import Nominatim
            geolocator = Nominatim(user_agent="geoapiExercises")
            city1 = str(city.get())
            country1=str(country.get())
            loc = geolocator.geocode(city1+',' + country1)
            L = ['Latitude', 'Longitude']
            b = ""
            latitude = str(loc.latitude)
            longitude = str(loc.longitude)
            b = L[0]+":-"+latitude+"\n"
            b = b+L[1]+":-"+longitude
            display = tk.Text(button_frame, height=10, width=30)
            display.grid(row=6, column=2)
            display.insert(tk.END, b)
        user_button=tk.Button(button_frame,text="Click Me",command=search,height=2,width=10)
        user_button.grid(row=4,column=1,pady=5,padx=20)
app = App()
app.mainloop()
