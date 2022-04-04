#ifndef VECTEUR_HPP
#define VECTEUR_HPP

#include <iostream>
#include <cmath>

class Vecteur{
    private:
        int M;
        double *M_v;
    public:
        //constructeurs
        Vecteur(int m);
        Vecteur(int m, double* v);
        Vecteur(const Vecteur &vec);

        //destructeur
        ~Vecteur(){delete [] M_v;}

        Vecteur operator=(Vecteur const &v);

        int get_M() const {return M;}
        double* get_v() const {return M_v;}
        
        double & operator[](int k) { return M_v[k]; }
        double const& operator[](int k) const { return M_v[k]; }
};

Vecteur operator+(Vecteur const &v1, Vecteur const &v2);

Vecteur operator*(Vecteur const &v, double alpha);

Vecteur operator*(double alpha, Vecteur const &v);

Vecteur operator*(Vecteur const &v1, Vecteur const &v2);

#endif