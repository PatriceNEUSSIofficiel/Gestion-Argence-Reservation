# Urban_Transport

# Application de Trajet et Géolocalisation avec Django, Python, JavaScript , HTML, CSS et intégration de l'API Google Maps


Ce dépôt est destiné à accueillir le code source de l'application de gestion des trajet et Géolocalisation. 

Ce fichier README.md présente les fonctionnalités requises et l'interface utilisateur de l'application de calcul de trajet.


## Equipes

* Superviseur: Dr AZANZI JIOMEKONG
* Intégrateur (Lead Dev): MFENJOU ANAS CHERIF  [lien vers son portfolio](https://cherif.itengineeringpro.fr/)
 
* Développeurs
  * NEUSSI JIETCHEU PATRICE EUGENE : [lien vers son github](https://github.com/PatriceNEUSSIofficiel)
  * LONTSI LAMBOU RONALDINO : [lien vers son github](https://github.com/LLontsi/)
  * NGUEGHO TIODONG ROBERTO LANDRY : [lien vers son github](https://github.com/nguegho/)
  * DOMCHE WABO LYTHEVINE FRAICHENELLE : [lien vers son github](https://github.com/lythevinedomche/)
  * MFENJOU ANAS CHERIF : [lien vers son github](https://github.com/cherif2004/) 

## PRESENTATION DE L'APPLICATION
L'objectif de ce projet est de développer **une application web** de **trajet** et de **géolocalisation**
pour la ville de **Yaoundé**. L'application permettra aux utilisateurs de trouver le meilleur itinéraire entre deux points (**A** et **B**) en fournissant des informations sur le coût du trajet (jours et nuits), la distance entre les deux points, ainsi que la localisation actuelle de l'utilisateur et son trajet sur la carte. L'application sera développée en utilisant **_Django_**
comme framework backend, **_Python_** pour la logique métier, **_JavaScript_** pour les fonctionnalités interactives côté client, **_HTML_** et **_CSS_** pour la présentation du contenu, et l'API Google Maps pour l'intégration des cartes et de la géolocalisation.


## 1. Fonctionnalités Requises
**a. Authentification Utilisateur** : Les utilisateurs doivent pouvoir créer un compte, se connecter et se déconnecter de l'application.

**b. Calcul du Coût du Trajet** : L'application doit être capable de calculer le coût d'un trajet entre les points A et B, en tenant compte des tarifs spécifiques pour les trajets de jour et de nuit.

**c. Calcul de la Distance** : L'application doit être capable de calculer la distance entre les points A et B en utilisant des données géographiques.

**d. Localisation Actuelle** : L'application doit pouvoir récupérer la localisation actuelle de l'utilisateur en utilisant l'API Google Maps.

**e. Affichage du Trajet sur la Carte** : L'application doit afficher le trajet entre les points A et B sur une carte interactive intégrée à l'aide de l'API Google Maps.

## 2. Interface Utilisateur
**a. Page d'Accueil** : Une page d'accueil accueillante avec des informations sur l'application et la possibilité de se connecter ou de créer un compte.

**b. Formulaire de Recherche** : Une page ou un formulaire permettant aux utilisateurs de spécifier les points de départ et d'arrivée pour trouver le meilleur itinéraire.

**c. Résultats de Recherche** : Une page affichant les résultats de recherche avec les informations sur le coût du trajet, la distance et des options supplémentaires.

**d. Carte Interactive** : Une page affichant une carte interactive avec le trajet entre les points A et B et la localisation actuelle de l'utilisateur.

## 3. Technologies Utilisées
L'application utilise les technologies suivantes :

**- Langage de Programmation**: Python  <br>
**- Framework Frontend** : _React.js_  <br>
**- Framework Backend** : _DJANGO_ <br>
**- Base de Données** : _MYSQL_ <br>
**- API de Cartographie** : _Google Maps API_  


Note: Assurez-vous d'avoir une clé d'API Google Maps valide pour pouvoir utiliser la fonctionnalité de localisation et d'affichage de la carte.

## 4. Contribution
Les contributions à l'amélioration de cette application sont les bienvenues. Si vous souhaitez contribuer, veuillez suivre les directives suivantes :

1. Fork ce dépôt.
2. Créez une branche pour votre fonctionnalité ou votre correction de bogue.
3. Effectuez les modifications nécessaires.
4. Testez soigneusement les modifications.
5. Soumettez une demande d'extraction en expliquant en détail les modifications apportées.

Merci pour votre contribution !

## 5. Licence
Ce projet est sous licence **Apache**. 

# Architecture matérielle

**1. Serveur web :**
-  Un serveur web robuste et évolutif tel que **Nginx** ou **Apache** pour gérer les requêtes HTTP et servir les fichiers statiques.

**2. Serveur d'application :**
-  Un serveur d'application (cluster kubernetes) pour exécuter l'application Django et gérer les processus applicatifs.

**3. Base de données :**
- Une base de données relationnelle telle que   **MySQL** pour stocker les données géographiques, les tarifs de trajet et les informations utilisateur.

**4. Système de fichiers statiques :**
- Utilisez un système de fichiers statiques pour stocker les fichiers CSS, JavaScript, les images et autres ressources statiques de l'application.

**5. Système de cache :**
-  Un système de cache tel que **Redis** ou **Memcached** pour améliorer les performances en mettant en cache les requêtes fréquemment utilisées.

**6. Serveur de localisation :**
-  L'API **Google Maps** pour la géolocalisation et l'affichage des cartes interactives. Vous aurez besoin d'une clé d'API Google Maps valide pour utiliser ce service.



**7. Infrastructure réseau :**
-  Une infrastructure réseau stable avec une connexion Internet fiable pour garantir l'accès à l'application depuis différents appareils et emplacements.

**8. Serveurs de développement et de production :**
-  Les environnements de développement et de production pour assurer un développement et un déploiement efficaces de l'application.



# Architecture logicielle

**Modèle-Vue-Contrôleur (MVC)** :
   -  Le modèle **MVC** pour organiser la structure de votre application.
   - **Modèle** : Comprend les classes et les méthodes pour la logique métier, la gestion des données et les interactions avec la base de données.
   - **Vue** : Gère l'interface utilisateur, la présentation des données et les interactions avec l'utilisateur.
   - **Contrôleur** : Traite les requêtes HTTP, coordonne les actions entre le modèle et la vue, et gère la logique de l'application.

# Architecture DevOps 

1. **Contrôle de version** :
   - Un système de contrôle de version tel que **Git** pour gérer le code source de l'application.
   -  Un référentiel Git pour stocker le code et utilisez des branches pour le développement parallèle, les correctifs de bogues et les fonctionnalités.

2. **Intégration continue (CI)** :
   -  Un service d'intégration continue tel que  **GitLab CI/CD** pour automatiser le processus de construction et de test de l'application.
   - Configurez des pipelines CI pour extraire le code à partir du référentiel, le compiler, exécuter les tests unitaires et générer des artefacts déployables.

3. **Déploiement continu** (CD) :
   - Utilisez l'intégration continue pour déclencher automatiquement le déploiement de nouvelles versions de l'application.
   - Utilisez des outils de déploiement tels que **Ansible** pour automatiser la configuration et le déploiement de l'infrastructure serveur.

5. **Infrastructure en tant que code (IaC)** :
   - Utilisation des outils tels que **Terraform** pour décrire  l'infrastructure en tant que code.
   - Déployement et gestion de  l'infrastructure de manière reproductible en utilisant des scripts et des configurations versionnés.

6. **Conteneurisation** :
   -  la conteneurisation avec **Docker** pour créer des images conteneurisées de votre application.
   - Déployement des conteneurs sur une plateforme d'orchestration telle que **Kubernetes** pour gérer et mettre à l'échelle les applications.

7. **Surveillance et journalisation** :
   - Mise en place des outils de surveillance tels que **Prometheus**, **Grafana** pour collecter et visualiser les métriques de performance, les journaux et les alertes.
   - Surveillez l'état de l'application, les performances du serveur, les erreurs, etc.

8. **Sécurité**:
   - Mettez en œuvre des pratiques de sécurité, telles que l'utilisation de certificats SSL/TLS pour les communications sécurisées, la gestion des secrets et des variables d'environnement sensibles, et la mise à jour régulière des dépendances logicielles pour corriger les vulnérabilités connues.

9. **Plan de reprise d'activité (PRA)** :
   - Mettez en place des mesures de sauvegarde régulières des données de l'application et des configurations de l'infrastructure.
   - Définissez des procédures de restauration pour minimiser les temps d'arrêt en cas de défaillance du système.

## Stack

Ce projet est développé avec le framework Django 4.2.2 , utilise react  comme moteur de template et tourne sur une base de données MySql

## Installation

Commencez par cloner le projet sur votre PC

```bash
git clone https://github.com/PatriceNEUSSIofficiel/Urban_Transport
```

1) cd to development directory
2) mkvirtualenv transport
3) mkdir transport
4) clone repository to new directory
5) pip install -r requirements.txt
6) Update settings.py with your email API information


GOOGLE_API_KEY = "XXX"


7) python manage.py makemigrations
8) python manage.py migrate
9) python manage.py runserver
10) https://localhost:8000 - Bob's your uncle!! 



Rendez-vous sur la branche correspondant à votre module (exemple: `git checkout -b cherif`)
**Vous ne ferez des commits et push que sur votre branche**

## Cycle de développement

Avant de commencer à travailler, chacun doit se rassurer au préalable d'avoir récupérer les travaux de ses collaborateurs afin que toute l'équipe ai la même base de code. De ce fait, le workflow quotidien doit être le suivant

```bash
git checkout {{branch}} // branch est votre branche
git pull origin main
git merge main {{branch}}
// commit 1
// commit 2
git push origin {{branch}}
```

Une fois le push fait, le développeur devra faire une **pull request** sur GitHub afin qu'on puisse fusionner ses travaux.
Chaque soir (18h), le Lead Dev fusionnera toutes les differentes branches ayant soumis des *pull request* à partir des outils. Si tout est ok, les travaux seront mis sur la branche principale (main) pour déploiement

## Guide de développement

LES REGLES SUIVANTES DOIVENT SCRUPULEUSEMENT ETRE RESPECTEES

1. Chaque responsable de module doit créer une branche correspondant à son module pour effectuer son travail.
Par exemple, _MFENJOU ANAS CHERIF_ qui s'occupe des **interface utilisateurs** doit avoir une branche **cherif** dans laquelle il fera ses modifications en rapport avec son module  `git checkout -b cherif`
2. Aucun push ne doit être fait sur la branche principale. Les différents développeurs devront faire des push sur leurs branches et faire une **pull request** sur la branche **dev**  
3. Les commits sur un nombre important de fichiers sont proscits. Ils doivent être ponctuels et spécifique à une activité précise. Par ailleurs les commits doivent être fait avec la syntaxe suivante **{{badge}}: description**. La description du badge doivent être précise et en rapport avec l'action effectuée. {{badge}} est un terme générique qui peut avoir les valeurs suivantes:

* **feat** : Utilisé lorsqu'une nouvelle fonctionnalité a été ajoutée
* **fix** : Utilisé lorsqu'un bug a été corrigé
* **patch** : Utilisé lorsqu'on a apporté une optimisation d'une fonction sans ajout de fonctionnalité ou correction de bug et sans que sa n'impacte sur le reste du code (lors du remplacement d'un if/else par une condition ternaire par exemple)
* **chore** : Utilisé lorsque la structure globale d'un grand ensemble a été fortement modifiée
* **cs-fix** : Utilisé lorsqu'on fait une correction du style de code (par exemple quand on change **ma_variable** par **maVariable**)
* **docs**: Utilisé quand on fait une modification sur le guide d'utilisation (documentation). Un wiki sera créer sur ce dépôt de chaque responsable documentera chacune des fonctionnalités de son module.
Vous pouvez vous referez à la page des commits (<https://github.com/PatriceNEUSSIofficiel/Urban_Transport/commits/>) pour avoir un aperçu
# Gestion-Argence-Reservation-en-ligne
