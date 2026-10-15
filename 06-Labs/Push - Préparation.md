---
tags: [lab, htb, push, preparation]
statut: a-faire
---
# Push - Préparation

## Ce que l'on sait (recoupé par recherche le 15 octobre 2026)
- **Type :** lab rapide HackTheBox, petit scénario Active Directory sur Windows. Il fait partie du lot « time-efficient Pro Labs » avec Sidecar, Control et Intercept ([journal HTB](https://roadmap.hackthebox.com/changelog/new-time-efficient-pro-labs-available-on-htb-labs)).
- **Taille :** 2 machines et 2 drapeaux par machine selon HTB (un contrôleur de domaine et un serveur membre selon un autre article HTB). À confirmer sur la page du lab.
- **Thèmes annoncés par HTB :** ClickOnce, SCCM, ADCS (certificats), authentification par clé et Kerberos, abus de privilèges, mouvement latéral.
- **Niveau :** avancé pour l'Active Directory (le lab voisin Sidecar est décrit comme non adapté aux débutants). Pas de note de difficulté officielle trouvée pour Push.
- **Accès :** confirmé par toi (abonnement actif jusqu'au 8 octobre 2027).
- **Règle HTB :** pas de partage de solutions, donc notes et rapport privés.

## Place dans ton plan
- Premier lab de la liste, octobre 2026, avant Sidecar. Budget du plan : 15 à 25 h (avis ; avec seulement 2 machines, ce peut être moins).
- Au rythme prévu (5 à 5 h 30 de lab par semaine en semaine d'entreprise), cela représente 3 à 5 semaines.
- **Plafond :** si tu dépasses 25 h, tu arrêtes, tu écris ce qui bloque et tu passes à Sidecar. Rien ne t'oblige à tout finir.
- **Critère de réussite du plan :** Push terminé et rapport privé de 3 à 5 pages.

## Avant de commencer
- [ ] Environnement : machine virtuelle dédiée, connexion VPN HackTheBox testée, instantané de la machine virtuelle pris.
- [ ] Dossier de travail et notes privés (nom avec « privé », ignoré par git).
- [ ] Un gestionnaire de mots de passe pour tout ce que tu trouves : jamais d'identifiant en clair dans le vault.
- [ ] Copie du [[06-Labs/Modèle - Journal de lab|modèle de journal]].
- [ ] Lecture de la description officielle du lab, sans chercher de solution.
- [ ] Licence Burp Suite Professional active, exigée pour l'examen BSCP (à vérifier dès octobre, ce n'est pas lié à Push).

## Concepts à réviser (sans technique d'attaque)
Pour chaque thème, réponds par écrit avant de commencer. Source : documentation Microsoft Learn (recherche par le nom du thème) et [MITRE ATT&CK T1127.002 pour ClickOnce](https://attack.mitre.org/techniques/T1127/002).

- **ADCS (services de certificats) :** qu'est-ce qu'une autorité de certification, un modèle de certificat, une inscription ? Qui peut demander quel certificat ? À quelle identité est-il lié ? Où est ancrée la confiance dans le domaine ?
- **SCCM (Configuration Manager) :** quels rôles et quels comptes de service existent ? Comment un logiciel est-il déployé sur un poste ? Quelles machines parlent à quelles machines ?
- **ClickOnce :** comment une application est-elle déployée depuis une adresse ou un partage ? Que contient un manifeste ? Quelle signature est vérifiée et avec quels droits l'application s'exécute-t-elle ?
- **Kerberos et authentification par clé ou certificat :** rappelle le déroulement d'un ticket (TGT, ticket de service). Comment un compte peut-il s'authentifier avec une clé ou un certificat plutôt qu'un mot de passe ?
- **Raccourcis et partages Windows :** comment Windows traite-t-il un fichier raccourci dans un dossier partagé ? Qui l'ouvre, et avec quel compte ?

## Méthode pendant le lab
- **Journal horodaté :** une ligne par action (objectif, résultat, trace probable côté défense). Voir le modèle.
- **Tableau des hôtes et des comptes** à jour, sans secret en clair.
- **Schéma du chemin d'attaque :** une version par étape franchie.
- **Règle de blocage :** 45 minutes sans progrès, tu écris la question précise et tu changes d'angle ; 90 minutes, tu reprends un autre jour ; ensuite seulement, un indice officiel HackTheBox. Tu ne cherches pas de solution publique (elle gâche l'apprentissage, et les partager est interdit).
- **Journal de détection :** pour chaque étape, note ce que la défense aurait pu voir et ce que tu ferais autrement. C'est ce qui te distingue en entretien.

## À la fin
- [ ] Rapport privé de 3 à 5 pages ([[06-Labs/Modèle - Rapport de lab|modèle]]).
- [ ] Fiche de leçons : 5 lignes maximum, ce que tu referais autrement.
- [ ] Mise à jour de la ligne du plan : heures réelles passées (elles servent à recaler la suite).

Retour : [[06-Labs/Labs - Index|Labs - Index]]
