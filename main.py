import tkinter as tk
from tkinter import ttk, messagebox
from database import Database
from album import Album

root = tk.Tk()
root.title("Album Database")
root.geometry("600x400")
root.configure(background="#F4F4F4")

db = Database('infoAlbum.db')

# Styling
style = ttk.Style()
style.configure("TButton", background="#FF6B6B", foreground="#4949c6")
style.configure("TLabel", background="#F4F4F4", foreground="#4949c6")
style.configure("TEntry", background="#FFFFFF", fieldbackground="#4949c6")
style.configure("TText", background="#FFFFFF", foreground="#4949c6")

# Input Form Interface
def switch_to_input_form():
    display_frame.pack_forget()
    input_frame.pack()

def ajouter_album():
    titre = titre_entry.get()
    nomAuteur = nomAuteur_entry.get()
    annee = annee_entry.get()
    prenomAuteur = prenomAuteur_entry.get()
    nbreChansons = nbreChansons_entry.get()
    
    if titre and nomAuteur and annee and prenomAuteur and nbreChansons:
        try:
            annee = int(annee)  # Make sure annee is a valid integer
        except ValueError:
            messagebox.showerror("Invalid annee", "Please enter a valid integer for annee.")
            return
        db.ajouter_album(titre, nomAuteur, annee, prenomAuteur, nbreChansons)
        result_label.configure(text="Les informations ont été sauvegardées avec succès dans la base de données 'albums.db'.")
        clear_input_fields()
        switch_to_display_form()  # Refresh the display table
    else:
        result_label.configure(text="Veuillez remplir tous les champs.", foreground="red")

# In the Database class:
def clear_input_fields():
    titre_entry.delete(0, tk.END)
    nomAuteur_entry.delete(0, tk.END)
    annee_entry.delete(0, tk.END)
    prenomAuteur_entry.delete(0, tk.END)
    nbreChansons_entry.delete(0, tk.END)

# Display Form Interface
def switch_to_display_form():
    input_frame.pack_forget()
    display_frame.pack()
    afficher_albums()

def afficher_albums():
    albums = db.recuperer_albums()

    for row in table.get_children():
        table.delete(row)

    for album in albums:
        table.insert("", "end", values=(album.id, album.titre, album.nomAuteur, album.annee, album.prenomAuteur, album.nbreChansons))

    result_label.configure(text="Les informations ont été récupérées avec succès depuis la base de données 'albums.db'.")

# Input Form
input_frame = tk.Frame(root, bg="#F4F4F4")
input_label = ttk.Label(input_frame, text="Nouvelle Album", font=("Helvetica", 16), background="#F4F4F4")

input_label.pack(pady=5)
result_label = ttk.Label(input_frame, text="", background="#F4F4F4")
result_label.pack()

titre_label = ttk.Label(input_frame, text="Titre:", background="#F4F4F4")
titre_label.pack()
titre_entry = ttk.Entry(input_frame)
titre_entry.pack()

nomAuteur_label = ttk.Label(input_frame, text="NomAuteur:", background="#F4F4F4")
nomAuteur_label.pack()
nomAuteur_entry = ttk.Entry(input_frame)
nomAuteur_entry.pack()

annee_label = ttk.Label(input_frame, text="Annee:", background="#F4F4F4")
annee_label.pack()
annee_entry = ttk.Entry(input_frame)
annee_entry.pack()

prenomAuteur_label = ttk.Label(input_frame, text="PrenomAuteur:", background="#F4F4F4")
prenomAuteur_label.pack()
prenomAuteur_entry = ttk.Entry(input_frame)
prenomAuteur_entry.pack()

nbreChansons_label = ttk.Label(input_frame, text="NbreChansons:", background="#F4F4F4")
nbreChansons_label.pack()
nbreChansons_entry = ttk.Entry(input_frame)
nbreChansons_entry.pack()

ajouter_button = ttk.Button(input_frame, text="Ajouter", command=ajouter_album)
ajouter_button.pack(pady=10)

switch_to_display_button = ttk.Button(input_frame, text="Afficher", command=switch_to_display_form)
switch_to_display_button.pack()

# Display Form
display_frame = tk.Frame(root, bg="#F4F4F4")

display_label = ttk.Label(display_frame, text="Albums enregistrées", font=("Helvetica", 16), background="#F4F4F4")
display_label.pack(pady=10)

table_frame = ttk.Frame(display_frame)
table = ttk.Treeview(table_frame, columns=("ID", "Titre", "NomAuteur", "Annee", "PrenomAuteur", "NbreChansons"), show="headings")
table.heading("ID", text="ID")
table.heading("Titre", text="Titre")
table.heading("NomAuteur", text="NomAuteur")
table.heading("Annee", text="Annee")
table.heading("PrenomAuteur", text="PrenomAuteur")
table.heading("NbreChansons", text="NbreChansons")

table.column("ID", width=20)
table.column("Titre", width=150)
table.column("NomAuteur", width=150)
table.column("Annee", width=80)
table.column("PrenomAuteur", width=150)
table.column("NbreChansons", width=150)

table.tag_configure("oddrow", background="#E8E8E8")
table.tag_configure("evenrow", background="#FFFFFF")

table.pack(padx=10, pady=10)
table_frame.pack(padx=10, pady=5)

switch_to_input_button = ttk.Button(display_frame, text="Retour", command=switch_to_input_form)
switch_to_input_button.pack(pady=10)

# Other Functions
def on_quit():
    db.fermer_connexion()
    root.destroy()

# Quit Button
quit_button = ttk.Button(root, text="Quitter", command=on_quit)
quit_button.pack(pady=10)

# Start the program
switch_to_input_form()
root.mainloop()

print("Fin du programme.")
