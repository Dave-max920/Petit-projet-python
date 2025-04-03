def folder_creator(name):
        return name
#creation de la fonction qui permet de creer un fichier
def file_creator(name, type_file, ):
        #demander l'avis de l'utilisateur s'il souhaite creer un nouveau fichier 
        print("1.oui")
        print("2. Non")
        choix_user=int(input("inserer un fichier?"))
        #condition pour prendre en compte l'avis de l'utilisateur
        if choix_user==1:
            file_informations=[name, type_file]
            #une fois la creation du fichier ccompli, la fonction enverra les details du fichier
            return file_informations
        

#demander a l'utilisateur ses information
user_name=input("Quel est votre nom ?")
user_bithyear=int(input("Quel est votre annee de naissance?"))
user_gender=input("Votre sexe?")
user_pasword=input("Mettez votre mot de passe")

#l'utilisateur devra creer un dossier
nom=input("Nom du dossier")
print("1.oui"),
print("2. Non"),
choix_user=input("voulez vous y creer un dossier")

#boucle permettant de deamder l'utilisateur s'il souhaite creer un autre dossier
while choix_user == 1:
        nom=input("Nom du dossier")
        print("1.oui"),
        print("2. Non"),
        choix_user=input("voulez vous y creer un dossier")
        continue

#pour la creation du fichier
fichier=input("nom du fichier")
type=input("type du fichier")
file_creator(fichier, type)
