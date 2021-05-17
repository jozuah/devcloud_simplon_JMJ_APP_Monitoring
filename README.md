

![enter image description here](https://qbd.eu/wp-content/uploads/azure-logo.png)
# Projet : Azure Pricing Monitoring

Dans le cadre de la formation MS CLOUD de l'école du numérique simplon.co, notre équipe de développeur à mis en place une pipeline numérique dont le but est de pouvoir afficher les dépenses liés au compte Azure de Simplon.Co.

A partir d'un document excel fournit par MS Azure sur notre adresse email, le document est stocké dans un container, les données sont extraites et mises dans une base de donnée, les données sont ensuite exposés via notre API, et pour fournir, un site permet d'afficher simplement les données que l'on veut voir.

English version :

As part of the MS CLOUD training of the simplon.co digital school, our team of developers has set up a digital pipeline whose purpose is to display the expenses related to the Simplon.Co Azure account.

From an excel document provided by MS Azure on our email address, the document is stored in a container, the data is extracted and put in a database, the data is then exposed via our API, and finally, a site can simply display the data we want to see.

Translated with www.DeepL.com/Translator (free version)

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

## Logic App 

Fonctionnement : Une fois par semaine, l'application va regarder sur une adresse mail spécifique si un nouveau document du type file.xlx a été mis en pièce jointe d'un mail. Si il y a un nouveau dcoument, il est transféré dans un container de stockage sur Azure Storage.

English version :

How it works: Once a week, the application will look at a specific email address to see if a new document of type file.xlx has been attached to an email. If there is a new document, it is transferred to a storage container on Azure Storage.

![enter image description here](https://github.com/jozuah/devcloud_simplon_JMJ_APP_Monitoring/blob/master/images_readme/logicapp.png)

# Azure Function - trigger stockage blob azure

Fonctionnement : Dès qu'un document est ajouté au container "costsfiles" dans Azure Storage, il est immédiatement analysé et les données sont envoyés sur une base de donnée Azure MySQL

English version :

How it works: As soon as a document is added to the "costsfiles" container in Azure Storage, it is immediately analyzed and the data is sent to an Azure MySQL database

![enter image description here](https://github.com/jozuah/devcloud_simplon_JMJ_APP_Monitoring/blob/master/images_readme/azurefunction.png)

## Back-end 

Fonction : Serveur qui expose les données de l'api sous forme de JSON

Function : Server that exposes api data as JSON

https://jmjappmonitoring-back.azurewebsites.net/

Exemple de requête avec des paramètres :

Example of a query with parameters :

https://jmjappmonitoring-back.azurewebsites.net/api/?SubscriptionName=Nantes&ServiceName=Storage

![enter image description here](https://github.com/jozuah/devcloud_simplon_JMJ_APP_Monitoring/blob/master/images_readme/back_end.png)

## Front-end

Fonction : Partie visible par l'utilisateur, il sélectionne les données qu'il veut voir par l'intermédiaire de menu déroulant.

Function: Part visible by the user, he selects the data he wants to see through a drop-down menu.
Accessibilité : https://jmjappmonitoringstorage.z28.web.core.windows.net/

![enter image description here](https://github.com/jozuah/devcloud_simplon_JMJ_APP_Monitoring/blob/master/images_readme/frontfirst.png)
![enter image description here](https://github.com/jozuah/devcloud_simplon_JMJ_APP_Monitoring/blob/master/images_readme/frontchart.png)
![enter image description here](https://github.com/jozuah/devcloud_simplon_JMJ_APP_Monitoring/blob/master/images_readme/frontdropdown.png)

## Dépot git

Les differentes fonctionnalités ont été divisées en plusieurs branches :

English version :

The different functionalities have been divided into several branches:

branche front : Site html
branche back : Serveur api 
branche azurefunction : Contient le code de la fonction azure

branche master : contient toutes les données du projet

English version :

front branch : html site
back branch : api server 
azurefunction branch : Contains the code of the azure function

master branch : contains all the project data

