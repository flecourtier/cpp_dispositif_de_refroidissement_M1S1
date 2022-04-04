#include "mesures.hpp"

Mesures::Mesures(std::string nom_fichier){
    std::ifstream ifile(nom_fichier);
    if ( ifile ){
        char c;
        ifile >> c >> c >> L_x; L_x=L_x/1000.;
        ifile >> c >> c >> L_y; L_y=L_y/1000.;
        ifile >> c >> c >> L_z; L_z=L_z/1000.;
        ifile >> c >> M;
        ifile >> c >> c >> c >> phi; phi=phi*1000000;
        ifile >> c >> c >> h_c; h_c=h_c*1000000;
        ifile >> c >> c >> T_e;
        ifile >> c >> c >> c >> c >> c >> c >> c >> c >> c >> c >> stationary;
        ifile >> c >> c >> c >> c >> c >> c >> T_final;
        ifile >> c >> N;
        ifile >> c >> c >> M_x;
        ifile >> c >> c >> M_y;
        ifile >> c >> c >> M_z;
    }
}