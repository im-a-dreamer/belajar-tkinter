import tkinter as tk 

window = tk.Tk()
label = tk.Label(text="Hello, tkinter", 
                 fg="white", 
                 bg="black",
                 width=20,
                 height=10)
label.pack()
window.mainloop()

# text untuk menampilkan teks
# fg untuk menampilkan foreground (warna teks)
# bg untuk menampilkan background (warna latar belakang)
# width untuk lebar
# height untuk tinggi
# setiap metode Label() harus diakhiri dengan metode pack()

