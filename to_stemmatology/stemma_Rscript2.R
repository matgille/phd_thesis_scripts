# Adapted from Ariane Pinche's work https://github.com/ArianePinche/EditionLiSeintConfessor/blob/master/R-database/SaintMartin/scriptR/SMttms.R


#Load libraries

setwd("/home/mgl/Bureau/These/Edition/scripts/to_stemmatology")
library(stemmatology)
# Load data then convert them as matrix
Regimiento = read.csv("data/stemma_filtre.csv", sep=",", row.names=1)
RegimientoMatrix <- as.matrix(Regimiento)
View(RegimientoMatrix)
myConflicts = PCC.conflicts(RegimientoMatrix)
# Draw a stemma
RegimientoDbs = PCC(RegimientoMatrix, ask = TRUE, omissionsAsReadings = TRUE, verbose=TRUE)
stemma = PCC.Stemma(RegimientoMatrix, ask = FALSE, threshold = 0.05, omissionsAsReadings = FALSE)
View(stemma)

#RegimientoDbs = PCC(RegimientoMatrix[100:400, ], ask = FALSE, threshold = 0.05)
#RegimientoDbs = PCC(RegimientoMatrix, ask = TRUE)
#omissionsAsReadings = TRUE,
#alternateReadings = TRUE, verbose = TRUE)
saintMartinDbs = PCC(RegimientoMatrix[100:400, ], ask = FALSE, threshold = 0.05)
#saintMartinDbs = PCC(RegimientoMatrix[400:800, ], ask = TRUE, threshold = 0.035)
#saintMartinDbs = PCC(RegimientoMatrix[800:1200, ], ask = TRUE, threshold = 0.015)
#saintMartinDbs = PCC(RegimientoMatrix[1200:1600, ], ask = TRUE, threshold = 0.015)
saintMartinDbs = PCC(RegimientoMatrix[1600:2000, ], ask = FALSE,threshold = 0.04)
saintMartinDbs = PCC(RegimientoMatrix[2000:2400, ], ask = FALSE,threshold = 0.04)
#saintMartinDbs = PCC(RegimientoMatrix[2400:2800, ], ask = TRUE,threshold = 0.03)
#saintMartinDbs = PCC(RegimientoMatrix[2800:3200, ], ask = TRUE,threshold = 0.01)
#saintMartinDbs = PCC(RegimientoMatrix[3200:3700, ], ask = TRUE,threshold = 0.025)
#saintMartinDbs = PCC(RegimientoMatrix[100:800, ], ask = TRUE,threshold = 0.019)
#saintMartinDbs = PCC(RegimientoMatrix[1600:2400, ], ask = TRUE,threshold = 0.015)

#saintMartinDbs = PCC(RegimientoMatrix[1000:2000, ], ask = TRUE)
#saintMartinDbs = PCC(RegimientoMatrix, ask = TRUE)
#View(saintMartinDbs)
stemma = PCC.Stemma(RegimientoDbs, ask = FALSE)
View(stemma)

