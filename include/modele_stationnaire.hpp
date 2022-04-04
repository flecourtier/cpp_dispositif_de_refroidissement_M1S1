#ifndef MODELE_STATIONNAIRE_HPP
#define MODELE_STATIONNAIRE_HPP

#include "utils.hpp"

class Modele_stationnaire{
    private:
        Mesures* M_mesure;
        Matrice_tridiag* M_A;
        Vecteur* M_F;
        Vecteur* M_sol;

        // Pour construire la matrice A
        void def_matrice_tridiag_stationnaire();

        // Pour construire le vecteur F
        void def_second_membre();

        // Pour calculer la solution analytique
        Vecteur* T_exact();

        // Resolution 1D du modele stationnaire (remplir M_sol)
        void resolution_stat_1D();
    public:
        //constructeur
        Modele_stationnaire(Mesures* m) : M_mesure(m) {
            this->def_matrice_tridiag_stationnaire();
            this->def_second_membre();
            M_sol=new Vecteur(M_mesure->M+1);
            this->resolution_stat_1D();
        }

        //destructeur
        ~Modele_stationnaire(){
            delete M_A;
            delete M_F;
            delete M_sol;
        }

        // accesseur (n'est utilisé que pour montrer la convergence
        // du modèle instationnaire vers le modèle stationnaire)
        Vecteur* get_sol() const {return M_sol;}

        // Visualisation 1D et 3D (écriture fichier csv et vtk)
        void visualisation1D_solution_stationnaire();
        void visualisation3D_solution_stationnaire();     
};



#endif