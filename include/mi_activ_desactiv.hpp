#ifndef MI_ACTIV_DESACTIV_HPP
#define MI_ACTIV_DESACTIV_HPP

#include "modele_instationnaire.hpp"

class Modele_instationnaire_activ_desactiv : public Modele_instationnaire {
    private:
        // Pour obtenir la solution en fonction du temps (remplir M_sol)
        void def_solution_activ_desactiv();
        
        // On crée un tableau avec les valeurs que l'on souhaite récupérer
        // Ici on veut récupérer la température en 3 points de l'ailette
        Vecteur** donnees_a_analyser_instationnaire_activ_desactiv();
    public:
        //constructeur
        Modele_instationnaire_activ_desactiv(Mesures* m) : Modele_instationnaire(m) {
            this->def_solution_activ_desactiv();
        }

        //destructeur
        ~Modele_instationnaire_activ_desactiv(){};

        // Visualisation 1D (écriture fichier csv)
        void visualisation1D_solution_instationnaire_activ_desactiv();
        // Visualisation 3D (écriture dans plusieurs fichiers vtk)
        void visualisation3D_solution_instationnaire_activ_desactiv();  
};


#endif