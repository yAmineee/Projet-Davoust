import random

mots = ['ABCES', 'ABIME', 'ABORD', 'ACCES', 'ACHAT', 'ACTIF', 'ADAGE', 'ADIEU', 'AFFUT', 'AGATE', 'AGAVE', 'AGENT',
        'AGILE', 'AGORA', 'AHURI', 'AIDER', 'AIGLE', 'AINEE', 'AINSI', 'AIOLI', 'AJONC', 'AJOUT', 'ALBUM', 'ALGUE',
        'ALIAS', 'ALIBI', 'ALIEN', 'ALLER', 'ALORS', 'AMANT', 'AMBRE', 'AMIBE', 'AMONT', 'AMOUR', 'ANCRE', 'ANGLE',
        'ANNEE', 'ANTAN', 'AORTE', 'APNEE', 'APPAT', 'APPEL', 'APPUI', 'APRES', 'ARABE', 'ARBRE', 'ARMEE', 'ARRET',
        'ASSEZ', 'ATLAS', 'ATOLL', 'ATOME', 'AUCUN', 'AUSSI', 'AUTRE', 'AVANT', 'AVION', 'AVOIR', 'AVRIL', 'BABIL',
        'BACHE', 'BACON', 'BADGE', 'BADIN', 'BALAI', 'BALSA', 'BANAL', 'BANDE', 'BANNI', 'BARBE', 'BARIL', 'BARON',
        'BASSE', 'BELGE', 'BELLE', 'BIBLE', 'BIJOU', 'BILAN', 'BILLE', 'BISON', 'BISOU', 'BLANC', 'BLEME', 'BLOND',
        'BOUEE', 'BOULE', 'BOURG', 'BRAVO', 'BRUIT', 'BRUTE', 'BULLE', 'CADRE', 'CALME', 'CANAL', 'CARTE', 'CAUSE',
        'CELLE', 'CELUI', 'CETTE', 'CHALE', 'CHAMP', 'CHANT', 'CHOIX', 'CHOSE', 'CHUTE', 'CIVIL', 'CLERC', 'CLONE',
        'CLOWN', 'COCON', 'COEUR', 'COLLE', 'COMME', 'COMTE', 'CONNU', 'CONTE', 'CORNE', 'CORPS', 'COTON', 'COUDE',
        'COUPE', 'COURS', 'COURT', 'CRABE', 'CRAIE', 'CRANE', 'CREER', 'CRIER', 'CRIME', 'CRISE', 'CROIX', 'CRUEL',
        'CULTE', 'CYCLE', 'CYGNE', 'DANSE', 'DEBUT', 'DECES', 'DEGEL', 'DEPOT', 'DESIR', 'DEVIN', 'DIGNE', 'DOIGT',
        'DONNE', 'DOUTE', 'DOUZE', 'DROIT', 'DUREE', 'ECHEC', 'ECOLE', 'ECRIT', 'EDILE', 'EDITE', 'EFFET', 'ELEVE',
        'ELLES', 'ENFIN', 'ENTRE', 'ESSAI', 'ETAGE', 'ETANG', 'ETAPE', 'ETUDE', 'FAIRE', 'FAÇON', 'FEMME', 'FENTE',
        'FERME', 'FILLE', 'FINAL', 'FONDS', 'FORCE', 'FORET', 'FORME', 'FOULE', 'FRERE', 'FRONT', 'FUTUR', 'GAFFE',
        'GALOP', 'GAMIN', 'GARCE', 'GARDE', 'GARNI', 'GATER', 'GAULE', 'GAVER', 'GENRE', 'GLACE', 'GOBER', 'GOMME',
        'GOULU', 'GRACE', 'GRADE', 'GRAIN', 'GRAND', 'GRAVE', 'GUEPE', 'GUEUX', 'GUIDE', 'HABIT', 'HAMAC', 'HARDI',
        'HATIF', 'HERBE', 'HERON', 'HEROS', 'HEURE', 'HIVER', 'HOMME', 'HONTE', 'HOTEL', 'HOULE', 'HUILE', 'HUTTE',
        'IDEAL', 'IDOLE', 'IMAGE', 'IMPUR', 'ISSUE', 'JADIS', 'JALON', 'JAMBE', 'JASER', 'JAUNE', 'JETER', 'JETON',
        'JEUNE', 'JOINT', 'JOUER', 'JOUET', 'JOUTE', 'JUGER', 'JURER', 'JURON', 'JUSTE', 'KAYAK', 'KOALA', 'KURDE',
        'LACET', 'LAMPE', 'LANCE', 'LAPIN', 'LAQUE', 'LARGE', 'LASER', 'LATIN', 'LEGAL', 'LEGER', 'LEVEE', 'LEVER',
        'LEVRE', 'LIBRE', 'LIEGE', 'LIGNE', 'LIGUE', 'LISTE', 'LITRE', 'LIVRE', 'LOCAL', 'LOGIS', 'LOQUE', 'LOUER',
        'LOUPE', 'LOURD', 'LOYAL', 'LOYER', 'LUEUR', 'LUNDI', 'LUTIN', 'LUTTE', 'LYCEE', 'MACHE', 'MAIRE', 'MANIE',
        'MAREE', 'MASSE', 'MATCH', 'MATIN', 'MEDIA', 'MELON', 'MERLE', 'MESSE', 'METAL', 'METEO', 'METRE', 'METRO',
        'MICHE', 'MIEUX', 'MIXTE', 'MOCHE', 'MOINS', 'MONDE', 'MORNE', 'MOYEN', 'MUSEE', 'MUTIN', 'NAINE', 'NANTI',
        'NATIF', 'NAVAL', 'NEIGE', 'NEUVE', 'NEVEU', 'NOEUD', 'NOIRE', 'NOTRE', 'NOYER', 'NUAGE', 'NUIRE', 'NUQUE',
        'NYLON', 'OBJET', 'OCEAN', 'OFFRE', 'ONCLE', 'ONGLE', 'OPERA', 'ORDRE', 'OUEST', 'OUTRE', 'OVULE', 'PARCE',
        'PARMI', 'PARTI', 'PASSE', 'PECHE', 'PEINE', 'PERDU', 'PERLE', 'PERTE', 'PETIT', 'PHASE', 'PIANO', 'PIECE',
        'PISTE', 'PLACE', 'PLEIN', 'PLUME', 'POETE', 'POIDS', 'POINT', 'PORTE', 'POSTE', 'POULE', 'PREVU', 'PRISE',
        'PRIVE', 'PROMU', 'QUAND', 'QUANT', 'RABOT', 'RADAR', 'RADIO', 'RAFLE', 'RALER', 'RAMER', 'RAMPE', 'RANCE',
        'RAPER', 'RATER', 'RATIO', 'RAYER', 'RECEL', 'RECIF', 'RECIT', 'RECUL', 'REGAL', 'REGNE', 'REINE', 'RENDU',
        'RENTE', 'RESTE', 'REVER', 'REVUE', 'RICHE', 'RIDER', 'RISEE', 'RIVAL', 'ROMAN', 'ROTER', 'ROUGE', 'ROUTE',
        'ROYAL', 'RUADE', 'RUBAN', 'RUBIS', 'RUGBY', 'RUGIR', 'RUSSE', 'SAINT', 'SALLE', 'SALON', 'SANTE', 'SCENE',
        'SCORE', 'SELON', 'SERBE', 'SERIE', 'SEULE', 'SIEGE', 'SIGNE', 'SOEUR', 'SOLDE', 'SOMME', 'SONGE', 'SORTE',
        'SOURD', 'SPORT', 'STADE', 'STAGE', 'STYLE', 'SUBIR', 'SUCER', 'SUCRE', 'SUITE', 'SUIVI', 'SUJET', 'SUPER',
        'TABAC', 'TABLE', 'TACHE', 'TALUS', 'TAMIS', 'TANTE', 'TAPIR', 'TAPIS', 'TARTE', 'TASSE', 'TAUPE', 'TAXER',
        'TEMPS', 'TENDU', 'TENIR', 'TENTE', 'TERME', 'TERRE', 'TETER', 'TETON', 'TEXTE', 'THEME', 'THESE', 'TIEDE',
        'TIERS', 'TIRER', 'TISSU', 'TITAN', 'TITRE', 'TOILE', 'TOMBE', 'TONTE', 'TORDU', 'TOTAL', 'TRAIN', 'TROIS',
        'TRONE', 'TUILE', 'TUYAU', 'UNION', 'UNITE', 'USAGE', 'USINE', 'UTILE', 'VACHE', 'VAGIN', 'VALET', 'VANNE',
        'VASTE', 'VEINE', 'VENDU', 'VENIR', 'VENTE', 'VIDEO', 'VIEUX', 'VIGNE', 'VILLE', 'VINGT', 'VIRIL', 'VIRUS',
        'VISER', 'VIVRE', 'VOILE', 'VOIRE', 'VOMIR', 'VOTRE', 'VOUTE', 'VOYOU', 'WAGON', 'ZEBRE']
secret = random.choice(mots)  # le mot à deviner!

bienvenue = """
Bienvenue à WORDLE en français!
Vous avez six essais pour trouver un mot de cinq lettres.
Vous devez entrer à chaque tentative un mot complet de cinq lettres en français.
Après chaque tentative vous saurez quelles lettres étaient correctes, 
et lesquelles étaient dans le mot mais mal placées:
---------------------------------------------
_ indique une lettre qui n'est pas dans le mot
= indique une lettre mal placée
# indique une lettre placée correctement.
---------------------------------------------
Exemple:
CARTE
#_==_	=> ceci indique que le C est correct, et que le R et le T sont mal placés. Le mot ne contient pas de A ou de E.

"""
print(bienvenue)

for l in secret:
    print('_', end="")

gagne = False
for repeat in range(5):
    print()  # nouvelle ligne
    mi = input().upper()  # mettre en majuscule
    if (len(mi) != 5):  # TODO: accepter seulement des mots valides (des mots du dictionnaire)
        print("vous devez entrer des mots de 5 lettres")
        continue
    if (mi == secret):
        print("bravo vous avez gagné!")
        gagne = True
        break
    else:
        # print(" ", end='')
        for i in range(5):
            if (mi[i] == secret[i]):
                print("#", end='')
            elif (mi[
                      i] in secret):  # TODO: si une lettre est répétée, tenir compte du nombre de lettres dans le mot secret pour ne pas marquer par exemple une fois la lettre mal placée et une fois bien placée.
                print("=", end='')
            else:
                print("_", end='')
if (not gagne):
    print("Perdu! Le mot était", secret)
