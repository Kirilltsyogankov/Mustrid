import tkinter as tk

def joonista_bahama_lipp():
    tahvel.delete("all")  # Kustutab eelneva joonistuse
    # Joonistab kolm võrdse suurusega triipu
    triibu_korgus = 33
    tahvel.create_rectangle(50, 50, 250, 50 + triibu_korgus, fill="#3F888F", outline="")
    tahvel.create_rectangle(50, 50 + triibu_korgus, 250, 50 + 2 * triibu_korgus, fill="#FFD500", outline="")
    tahvel.create_rectangle(50, 50 + 2 * triibu_korgus, 250, 50 + 3 * triibu_korgus, fill="#3F888F", outline="")
    # Joonistab musta kolmnurga
    tahvel.create_polygon(50, 50, 150, 100, 50, 150, fill="#000000", outline="")
    # Tekst
    tahvel.create_text(150, 180, text="Bahama lipud", font=("Helvetica", 12, "bold"))

def joonista_eesti_lipp():
    tahvel.delete("all")  # Kustutab eelneva joonistuse
    triibu_korgus = 50
    tahvel.create_rectangle(50, 50, 250, 50 + triibu_korgus, fill="#0072CE", outline="")
    tahvel.create_rectangle(50, 50 + triibu_korgus, 250, 100 + triibu_korgus, fill="#000000", outline="")
    tahvel.create_rectangle(50, 100 + triibu_korgus, 250, 150 + triibu_korgus, fill="#FFFFFF", outline="")
    tahvel.create_text(150, 180 + triibu_korgus, text="Eesti riigi lipud", font=("Helvetica", 12, "bold"))

def joonista_venemaa_lipp():
    tahvel.delete("all")  # Kustutab eelneva joonistuse
    triibu_korgus = 50
    tahvel.create_rectangle(50, 50, 250, 50 + triibu_korgus, fill="#FFFFFF", outline="")
    tahvel.create_rectangle(50, 50 + triibu_korgus, 250, 50 + 2 * triibu_korgus, fill="#0033A0", outline="")
    tahvel.create_rectangle(50, 50 + 2 * triibu_korgus, 250, 50 + 3 * triibu_korgus, fill="#D52B1E", outline="")
    tahvel.create_text(150, 180 + triibu_korgus, text="Venemaa riigi lipud", font=("Helvetica", 12, "bold"))

def joonista_muster(tahvel, ruudud, ringid, x1, y1, x2, y2, sügavus):
    if sügavus == 0:
        return
    else:
        tahvel.create_rectangle(x1, y1, x2, y2, outline="black")
        if ruudud > 1:
            ruudu_laius = (x2 - x1) / ruudud
            ruudu_korgus = (y2 - y1) / ruudud
            for i in range(1, ruudud):
                tahvel.create_line(x1 + i * ruudu_laius, y1, x1 + i * ruudu_laius, y2, fill="black")
                tahvel.create_line(x1, y1 + i * ruudu_korgus, x2, y1 + i * ruudu_korgus, fill="black")
        if ringid > 0:
            raadius = min(x2 - x1, y2 - y1) / 4
            kesk_x = (x1 + x2) / 2
            kesk_y = (y1 + y2) / 2
            tahvel.create_oval(kesk_x - raadius, kesk_y - raadius, kesk_x + raadius, kesk_y + raadius, outline="black")
        joonista_muster(tahvel, ruudud, ringid, x1, y1, (x1 + x2) / 2, (y1 + y2) / 2, sügavus - 1)
        joonista_muster(tahvel, ruudud, ringid, (x1 + x2) / 2, y1, x2, (y1 + y2) / 2, sügavus - 1)
        joonista_muster(tahvel, ruudud, ringid, x1, (y1 + y2) / 2, (x1 + x2) / 2, y2, sügavus - 1)
        joonista_muster(tahvel, ruudud, ringid, (x1 + x2) / 2, (y1 + y2) / 2, x2, y2, sügavus - 1)

def joonista_maatriks():
    tahvel.delete("all")
    ruudud = int(ruutude_sisestus.get())
    ringid = int(ringide_sisestus.get())
    joonista_muster(tahvel, ruudud, ringid, 10, 10, 390, 390, 3)

def joonista_lauamäng():
    tahvel_lauamäng.delete("all")
    ruudu_suurus = 50
    for i in range(8):
        for j in range(8):
            x1 = j * ruudu_suurus
            y1 = i * ruudu_suurus
            x2 = x1 + ruudu_suurus
            y2 = y1 + ruudu_suurus
            if (i + j) % 2 == 0:
                tahvel_lauamäng.create_rectangle(x1, y1, x2, y2, fill="white", outline="")
            else:
                tahvel_lauamäng.create_rectangle(x1, y1, x2, y2, fill="black", outline="")

class Valgusfoor:
    def __init__(self, root):
        self.root = root
        self.root.title("Valgusfoor")

        # Loob Canvas'i valgusfoori jaoks
        self.tahvel = tk.Canvas(root, width=100, height=250, bg="white")
        self.tahvel.pack()

        # Loob valgusfoori lambid
        self.punane_tuli = self.tahvel.create_oval(40, 30, 80, 70, fill="gray")
        self.kollane_tuli = self.tahvel.create_oval(40, 90, 80, 130, fill="gray")
        self.roheline_tuli = self.tahvel.create_oval(40, 150, 80, 190, fill="gray")

        # Loob nupud
        self.nupp = tk.Button(root, text="Lülita sisse", command=self.lülita_tuled)
        self.nupp.pack()

        # Algseis
        self.tuled_sees = False

    def lülita_tuled(self):
        # Vahetab valgusfoori tuled sisse või välja
        if self.tuled_sees:
            self.tahvel.itemconfig(self.punane_tuli, fill="gray")
            self.tahvel.itemconfig(self.kollane_tuli, fill="gray")
            self.tahvel.itemconfig(self.roheline_tuli, fill="gray")
            self.nupp.config(text="Lülita sisse")
            self.tuled_sees = False
        else:
            self.tahvel.itemconfig(self.punane_tuli, fill="red")
            self.tahvel.itemconfig(self.kollane_tuli, fill="yellow")
            self.tahvel.itemconfig(self.roheline_tuli, fill="green")
            self.nupp.config(text="Lülita välja")
            self.tuled_sees = True

# Loob graafikaaken
aken = tk.Tk()
aken.title("Lipud, muster, šahhmatilaud ja valgusfoor")

# Loob ülemise raami
ülemine_raam = tk.Frame(aken)
ülemine_raam.pack()

# Loob tahvli (canvas) lipumustri jaoks
tahvel = tk.Canvas(ülemine_raam, width=300, height=250, bg="white")
tahvel.grid(row=0, column=0, padx=10, pady=10)

# Lisab nupud ülemisele raamile
bahama_nupp = tk.Button(ülemine_raam, text="Bahama lipud", command=joonista_bahama_lipp)
bahama_nupp.grid(row=0, column=1, padx=5)
eesti_nupp = tk.Button(ülemine_raam, text="Eesti riigi lipud", command=joonista_eesti_lipp)
eesti_nupp.grid(row=0, column=2, padx=5)
venemaa_nupp = tk.Button(ülemine_raam, text="Venemaa riigi lipud", command=joonista_venemaa_lipp)
venemaa_nupp.grid(row=0, column=3, padx=5)

# Loob alumise raami
alumine_raam = tk.Frame(aken)
alumine_raam.pack()

# Loob sisestuskastid
ruudu_silt = tk.Label(alumine_raam, text="Ruudud:")
ruudu_silt.grid(row=0, column=0, padx=5, pady=5)
ruutude_sisestus = tk.Entry(alumine_raam)
ruutude_sisestus.grid(row=0, column=1, padx=5, pady=5)

ringide_silt = tk.Label(alumine_raam, text="Ringid:")
ringide_silt.grid(row=0, column=2, padx=5, pady=5)
ringide_sisestus = tk.Entry(alumine_raam)
ringide_sisestus.grid(row=0, column=3, padx=5, pady=5)

# Lisab joonistamisnupu alumisele raamile
joonista_nupp = tk.Button(alumine_raam, text="Joonista muster", command=joonista_maatriks)
joonista_nupp.grid(row=0, column=4, padx=5, pady=5)

# Loob tahvli (canvas) šahhmatilaua jaoks
tahvel_lauamäng = tk.Canvas(aken, width=400, height=400, bg="white")
tahvel_lauamäng.pack()

# Joonistab šahhmatilaua
joonista_lauamäng()

# Loob valgusfoori
valgusfoor = Valgusfoor(aken)

# Käivitab programmilooppi
aken.mainloop()
