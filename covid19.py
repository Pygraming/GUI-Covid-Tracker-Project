from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

root = Tk()
root.iconphoto(False, tk.PhotoImage(file="images/b.png"))

root.geometry("1300x700")
root.title("Covid-19 Tracker App")
root['background'] = '#c4a474'
canvas = Canvas(width=596, height=296)
canvas.pack()
img = ImageTk.PhotoImage(Image.open("images/logo.png"))
canvas.create_image(0, -55, anchor=NW, image=img)


def showdata():
    from matplotlib import pyplot as plt
    import matplotlib.patches as mpatches
    from covid import Covid
    covid = Covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []

    try:
        root.update()
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")

        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
        for y in cases:
            confirmed.append(y["confirmed"])
            active.append(y["active"])
            deaths.append(y["deaths"])
            recovered.append(y["recovered"])

        confirmed_patch = mpatches.Patch(color='LIGHTGRAY', label='Confirmed')
        recovered_patch = mpatches.Patch(color='LIGHTBLUE', label='Recovered')
        active_patch = mpatches.Patch(color='LIGHTGREEN', label='Active')
        deaths_patch = mpatches.Patch(color='orange', label='Deaths')
        plt.legend(handles=[confirmed_patch, recovered_patch, active_patch, deaths_patch])

        for x in range(len(country_names)):
            plt.bar(country_names[x], confirmed[x], color='LIGHTGRAY')
            if recovered[x] > active[x]:
                plt.bar(country_names[x], recovered[x], color='LIGHTBLUE')
                plt.bar(country_names[x], active[x], color='LIGHTGREEN')
            else:
                plt.bar(country_names[x], active[x], color='LIGHTGREEN')
                plt.bar(country_names[x], recovered, color='LIGHTBLUE')
        plt.bar(country_names[x], deaths[x], color='orange')
        plt.title('Current Covid Cases')
        plt.xlabel('Country Name')
        plt.ylabel('Cases ( in millions )')
        plt.show()
    except Exception as e:
        print("Enter Correct Details")

Label(root, bg = '#c4a474').pack()
Label(root, text="Enter the name of the Country\nto get its Covid-19 Data", font="Consolas 15 bold",
      bg='#e6e6e6').pack()
Label(root, bg = '#c4a474').pack()
Label(root, text="Enter Country Name", font="Consolas 16 bold", bg='#e6e6e6').pack()
data = StringVar()
data.set("")
Label(root, bg = '#c4a474').pack()
entry = Entry(root, textvariable=data, font="calibre 20 normal", width=30).pack()
Label(root, bg = '#c4a474').pack()
Button(root, text="Get Data", font="Consolas 15 bold", height=2, width=10, command=showdata, bd=5).pack()

root.mainloop()
