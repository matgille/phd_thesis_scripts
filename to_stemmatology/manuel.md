J'ai commencé à travailler sur stemmatology. Reprendre la thèse d'Ariane et les scripts qui y sont. Globalement ça devrait marcher. 

On excluera le témoin U après le chapitre 4, donc on fera deux essais: 
- tous les témoins sur 1, 2, 3, 4
- tous sauf U sur le reste du texte.

Ça devrait marcher mais il reste du travail d'exclusion des variantes problématiques. Reprendre le travail sur les variantes significatives pour un petit script qui permette une correction rapide.

Attention avec la première colonne (des numéro du lieu variant) qu'il faut correctement exclure. 

View(collation_table) permet de vérifier si les colonnes et les lignes sont correctes. Prendre comme exemple: https://github.com/ArianePinche/EditionLiSeintConfessor/blob/master/R-database/SaintMartin/scriptR/SMttms.R


Update: voir le script Stemma_Rscript2.R

1) filtrage des lieux variants lexicaux avec a_filtrer_corr.csv et a_filtrer_corr_omissions.csv

2) suppression des variantes à témoin unique qui sont inutiles et cassent tout avec le script remove_unici.py Pour l'instant ça sort 200 lieux variants seulement, essayer de revoir le filtrage. `RegimientoDbs = PCC(RegimientoMatrix, ask = TRUE, omissionsAsReadings=TRUE, verbose=TRUE)` (centrality threshold= 0.01) sort normalement un stemma assez proche de ce que j'imaginais, avec J qui se balade: le problème est que le nombre de lieux variants semble faible (mais je n'arrive pas à l'avoir)

U a été exclu du processus pour l'instant parce que ça plantait trop.
