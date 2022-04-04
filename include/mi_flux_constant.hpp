#ifndef MI_FLUX_CONSTANT_HPP
#define MI_FLUX_CONSTANT_HPP

#include "modele_instationnaire.hpp"

class Modele_instationnaire_flux_const : public Modele_instationnaire {
    private:
        // Pour obtenir la solution en fonction du temps (remplir M_sol)
        void def_solution_flux_constant();

        // On crée un tableau avec les valeurs que l'on souhaite récupérer
        // Ici on veut récupérer la température en 6 temps différents
        Vecteur** donnees_a_analyser_instationnaire_flux_constant();  
    public:
        //constructeur
        Modele_instationnaire_flux_const(Mesures* m) : Modele_instationnaire(m) {
            this->def_solution_flux_constant();
        }

        //destructeur
        ~Modele_instationnaire_flux_const(){};

        // Visualisation 1D (écriture fichier csv)
        void visualisation1D_solution_instationnaire_flux_constant();
        // Visualisation 3D (écriture dans plusieurs fichiers vtk)
        void visualisation3D_solution_instationnaire_flux_constant();  

        // Visualisation de la convergence du modèle instat vers le modèle stat
        void visualisation_convergence_modele(Vecteur* sol_stat);
};

#endif