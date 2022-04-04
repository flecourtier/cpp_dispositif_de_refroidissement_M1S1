#ifndef MODELE_INSTATIONNAIRE_HPP
#define MODELE_INSTATIONNAIRE_HPP

#include "utils.hpp"

class Modele_instationnaire{
    protected:
        Mesures* M_mesure;
        Matrice_tridiag* M_A;
        Vecteur* M_F;
        Vecteur** M_sol;

        // Pour construire la matrice A
        void def_matrice_tridiag_instationnaire();

        // Pour construire le vecteur F
        void def_second_membre();
    public:
        //constructeur
        Modele_instationnaire(Mesures* m) : M_mesure(m) {
            this-> def_matrice_tridiag_instationnaire();
            this-> def_second_membre();
            M_sol=new Vecteur*[M_mesure->N+1];
            for(int i=0; i<M_mesure->N+1; i++){
                M_sol[i]=new Vecteur(M_mesure->M+1);
            }
        }

        //destructeur (class mère)   
        virtual ~Modele_instationnaire(){
            delete M_A;
            delete M_F;
            for(int i=0; i<M_mesure->N+1; i++){
                delete M_sol[i];
            }
            delete [] M_sol;
        }
};

#endif