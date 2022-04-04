#include "modele_stationnaire.hpp"
#include "mi_flux_constant.hpp"
#include "mi_activ_desactiv.hpp"

int main(int argc, char *argv[]){  

    //on définit le fichier de configuration
    std::string nom_fichier="../simu.cfg";
    if(argc>1){
        nom_fichier=argv[1];
    }

    //on initialise une mesure à partir du fichier de configuration
    Mesures* mesure=new Mesures(nom_fichier);

    //crétion du fichier "maillage.vtk"
    visualisation3D_maillage(*mesure);

    // on instancie un Modele_stationnaire peu importe si stationnary = 0 ou 1
    // car dans le cas où le modèle est instationnaire on veut montrer 
    // la convergence vers le modèle stationnaire
    Modele_stationnaire* Ms=new Modele_stationnaire(mesure);

    //si le modèle est stationnaire
    if(mesure->stationary==1){
        Ms->visualisation1D_solution_stationnaire();
        Ms->visualisation3D_solution_stationnaire();
        delete Ms;
    }
    //si il est instationnaire
    else if(mesure->stationary==0){
        Modele_instationnaire_flux_const* Mifc=new Modele_instationnaire_flux_const(mesure);
        Mifc->visualisation1D_solution_instationnaire_flux_constant();
        Mifc->visualisation3D_solution_instationnaire_flux_constant();
        Mifc->visualisation_convergence_modele(Ms->get_sol());
        delete Ms;
        delete Mifc;

        Modele_instationnaire_activ_desactiv* Miadc=new Modele_instationnaire_activ_desactiv(mesure);
        Miadc->visualisation1D_solution_instationnaire_activ_desactiv();
        Miadc->visualisation3D_solution_instationnaire_activ_desactiv();
        delete Miadc;
    }

    delete mesure;

    return 0;
}