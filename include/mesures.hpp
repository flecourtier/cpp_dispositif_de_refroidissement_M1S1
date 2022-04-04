#ifndef MESURE_HPP
#define MESURE_HPP

#include <iostream>
#include <fstream>
#include <iomanip>
#include <cmath>
#include <sstream>

struct Mesures{
    const int rho=2700, C_p=940, K=164; 
    double L_x,L_y,L_z;
    int M;
    double phi,h_c;
    int T_e;
    bool stationary;
    int T_final;
    int N;
    int M_x,M_y,M_z;

    // constructeur qui lit directement le fichier nom_fichier 
    // donné en paramètre et initialise les attributs ci-dessus
    Mesures(std::string nom_fichier);

    //destructeur
    ~Mesures(){};
};

#endif