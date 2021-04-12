

![enter image description here](https://qbd.eu/wp-content/uploads/azure-logo.png)
# Projet : Azure Pricing Monitoring

Dans le cadre de la formation MS CLOUD de l'école du numérique simplon.co, notre équipe de développeur à mis en place une pipeline numérique dont le but est de pouvoir afficher les dépenses liés au compte Azure de Simplon.Co.

A partir d'un document excel fournit par MS Azure sur notre adresse email, le document est stocké dans un container, les données sont extraites et mises dans une base de donnée, les données sont ensuite exposés via notre API, et pour fournir, un site permet d'afficher simplement les données que l'on veut voir.

## Equipe de developpement
Jordan T. : https://github.com/Jordan-Fakers
Mouny K. : https://github.com/keomouny
Joshua G. : https://github.com/jozuah

## Technologies utilisées

**Html/CSS**

**JavaScript**

**Python**

**Microsoft Azure** 

## Déploiement


| Technologie | Utilisation | Langage |
|---|:---:|:---:|
| Azure Logic      | Email -> Azure Storage | No-Code |
| Azure Functions | Azure Storage -> base de donnée      |    Python |
| Azure MySQL     | Stockage de donnée      |  SQL |
|  Azure Web App  |    Back-end  | Python |
|  Azure Storage  |    Front-end / Stockage de fichiers  | Html/CSS/ Javascript |

# Logic App 

Fonctionnement : Une fois par semaine, l'application va regarder sur une adresse mail spécifique si un nouveau document du type file.xlx a été mis en pièce jointe d'un mail. Si il y a un nouveau dcoument, il est transféré dans un container de stockage sur Azure Storage.

# Azure Function - trigger stockage blob azure

Fonctionnement : Dès qu'un document est ajouté au container "costsfiles" dans Azure Storage, il est immédiatement analysé et les données sont envoyés sur une base de donnée Azure MySQL

# Back-end 

Fonction : Serveur qui expose les données de l'api sous forme de JSON
https://jmjappmonitoring-back.azurewebsites.net/

Exemple de requête avec des paramètres :
https://jmjappmonitoring-back.azurewebsites.net/api/?SubscriptionName=Nantes&ServiceName=Storage

# Front-end

Fonction : Partie visible par l'utilisateur, il sélectionne les données qu'il veut voir par l'intermédiaire de menu déroulant.
Accessibilité : https://jmjappmonitoringstorage.z28.web.core.windows.net/


# Dépot git

Les differentes fonctionnalités ont été divisées en plusieurs branches :

branche front : Site html
branche back : Serveur api 
branche azurefunction : Contient le code de la fonction azure

branche master : contient toutes les données du projet

