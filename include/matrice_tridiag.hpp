#ifndef MATRICE_TRIDIAG_HPP
#define MATRICE_TRIDIAG_HPP

#include <iostream>
#include <cmath>
#include "vecteur.hpp"

class Matrice_tridiag{
    private:
        int M;
        double *M_a;
        double *M_b;
        double *M_c;
    public:
        //constructeurs
        Matrice_tridiag(int m);
        Matrice_tridiag(int m, double* a, double* b, double* c);
        Matrice_tridiag(const Matrice_tridiag &A);

        //destructeur
        ~Matrice_tridiag(){
            delete [] M_a;
            delete [] M_b;
            delete [] M_c;
        }

        int get_M() const {return M;}
        double get_ai(int i) const {return M_a[i];}
        double get_bi(int i) const {return M_b[i];}
        double get_ci(int i) const {return M_c[i];}
};

#endif