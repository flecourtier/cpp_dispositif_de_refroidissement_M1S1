#ifndef UTILS_HPP
#define UTILS_HPP

#include <iostream>
#include <cmath>
#include "mesures.hpp"
#include "vecteur.hpp"
#include "matrice_tridiag.hpp"

//Barre de chargement
void affiche_progression(int pas, int max_pas);

// Pour écrire les points du maillage 3D dans les fichiers vtk
void def_maillage(const Mesures& mesure,std::ofstream& ofile);
// Pour visualiser le maillage 3D
void visualisation3D_maillage(const Mesures& mesure);

// Pour faire la factorisation LU de A
Matrice_tridiag** def_LU(const Matrice_tridiag A);
// Pour résoudre LY=F
void Descente_mat_tridiag(Vecteur& Y,const Matrice_tridiag& L,const Vecteur& F);
// Pour résoudre UX=Y
void Remontee_mat_tridiag(Vecteur& X,const Matrice_tridiag& U,const Vecteur& Y);

// Définition de la température à partir d'un interpolant linéaire
Vecteur* def_temperature_interpolee(const Mesures& mesure, Vecteur& sol);


#endif