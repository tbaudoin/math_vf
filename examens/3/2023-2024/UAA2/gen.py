# Importer le module os
import os
import posixpath

# Définir le répertoire où se trouvent les fichiers tikz
tikz_dir = 'tikz'
# Parcourir tous les fichiers du répertoire
for file in os.listdir(tikz_dir):
    # Vérifier si le fichier a l'extension .tikz
    if file.endswith(".tikz"):
        # Obtenir le nom du fichier sans l'extension
        file_name = file[:-5]
        if not os.path.exists(posixpath.join(tikz_dir,file_name+'.pdf')):
            # Créer un fichier tex temporaire avec l'environnement tikzpicture
            tex_file = file_name + ".tex"
            with open('gen_template.tex', 'r') as f:
                content = f.read()

            with open(posixpath.join(tikz_dir, tex_file), "w") as f:
                f.write(content.replace('PATHTOFILE', file))         
            # Exécuter lualatex pour générer le fichier pdf
            os.system("lualatex -output-directory " + tikz_dir + " " + posixpath.join(tikz_dir, tex_file))
            # Supprimer le fichier tex temporaire et les autres fichiers auxiliaires
            os.remove(posixpath.join(tikz_dir, tex_file))
            os.remove(posixpath.join(tikz_dir, file_name + ".log"))
            os.remove(posixpath.join(tikz_dir, file_name + ".aux"))
            # Afficher un message pour indiquer la progression
            print("Créé " + file_name + ".pdf à partir de " + file)
