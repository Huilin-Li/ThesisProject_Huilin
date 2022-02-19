#install.packages('IOHanalyzer')
#install.packages('Rcpp')
library(Rcpp)
library(IOHanalyzer)
library(tibble)
library(writexl)
library(plyr)


three_folders <- c("data_to_prove_no_impact_in_sync_or_async_evaluation",
                 "data_to_prove_yes_impact_in_sync_or_async_global_best_one",
                 "fixed_data_to_prove_UNIOA_is_same_as_SEP")

AUCs_names <- c("auc_28", "auc_10", "auc_14")
for (i in seq(3)){
 name <- three_folders[i]
 auc_name <- AUCs_names[i]
 path <- paste("D:/Temp_Huilin/unzips/", name, "/", sep="")
 AUCs <- read.csv(text="Alg, funcID, Dim, Budget, AUC")
 for (f in list.files(path)){
   dsl <- DataSetList(paste(path, f, sep=""))
   for (fid in seq(24)) {
     for (D in c(5,20)) {
       x <- generate_data.AUC(subset(dsl, funcId == fid && DIM == D), targets = get_ECDF_targets(dsl, "bbob"))
       x <- add_column(x, funcID = fid, .after = 'ID')
       x <- add_column(x, Dim = D, .after = 'funcID')
       names(x)<-c("Alg", "funcID", "Dim", "Budget", "AUC")
       AUCs <- rbind(AUCs, x)
     }
   }
 }
 outPath <- paste("D:/Temp_Huilin/", auc_name, ".xlsx", sep="")
 write_xlsx(AUCs, outPath)
}









##################################################### no need 

three_folders <- c("data_to_prove_no_impact_in_sync_or_async_evaluation",
                   "data_to_prove_yes_impact_in_sync_or_async_global_best_one",
                   "fixed_data_to_prove_UNIOA_is_same_as_SEP")

for (name in three_folders){
  inDir = paste("D:/Temp_Huilin/zips/", name, "/", sep="")
  outDir = paste("D:/Temp_Huilin/unzips/", name, sep="")
  for (zip_f in list.files(inDir)){
    zipF <- paste(inDir, zip_f, sep="")
    unzip(zipF,exdir=outDir)
  }
}




AUCs <- read.csv(text="Alg, funcID, Dim, Budget, AUC")
for (f in list.files("D:/Temp_Huilin/test/")){
  dsl <- DataSetList(paste("D:/Temp_Huilin/test/", f, sep=""))
  for (fid in seq(24)) {
    for (D in c(5, 20)) {
      x <- generate_data.AUC(subset(dsl, funcId == fid && DIM == D), targets = get_ECDF_targets(dsl, "bbob"))
      x <- add_column(x, funcID = fid, .after = 'ID')
      x <- add_column(x, Dim = D, .after = 'funcID')
      names(x)<-c("Alg", "funcID", "Dim", "Budget", "AUC")
      AUCs <- rbind(AUCs, x)
    }
  }
}
write_xlsx(AUCs, "D:/Temp_Huilin/auc4.xlsx")














