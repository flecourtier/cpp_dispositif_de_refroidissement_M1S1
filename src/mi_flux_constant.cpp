#include "mi_flux_constant.hpp"

// On définit la solution en fonction du temps
void Modele_instationnaire_flux_const::def_solution_flux_constant(){
    int M=M_mesure->M;
    int N=M_mesure->N;
    double dt=(double)(M_mesure->T_final)/M_mesure->N;

    //on initialise T_0
    Vecteur* T_n=new Vecteur(M+1);
    for(int i=0; i<M+1; i++){
        (*T_n)[i]=M_mesure->T_e;
        (*M_sol)[0][i]=M_mesure->T_e;
    }

    //on détermine la facto LU de A
    Matrice_tridiag** LU=def_LU(*M_A);

    //on crée le vecteur qu'on va multiplier à T_n
    Vecteur* alpha=new Vecteur(M+1);
    for(int i=1; i<M; i++){
        (*alpha)[i]=M_mesure->rho*M_mesure->C_p/dt;
    }

    //on résout le modèle instationnaire
    Vecteur* Y=new Vecteur(M+1);
    for(int n=1; n<N+1; n++){
        Descente_mat_tridiag(*Y,*LU[0],(*alpha)*(*T_n)+(*M_F));
        Remontee_mat_tridiag(*T_n,*LU[1],*Y);
        for(int i=0; i<M+1; i++){
            (*M_sol[n])[i]=(*T_n)[i];
        }
    }
    delete T_n; delete alpha; delete Y;
    delete LU[0]; delete LU[1]; delete [] LU;
}

/*
RESOLUTION 1D MODELE INSTATIONNAIRE FLUX CONSTANT
*/

// On crée un tableau avec les valeurs que l'on souhaite récupérer
// Ici on veut récupérer la température en 6 temps différents
Vecteur** Modele_instationnaire_flux_const::donnees_a_analyser_instationnaire_flux_constant(){    
    int N=M_mesure->N;
    double eps=pow(10,-3);
    double dt=(double)(M_mesure->T_final)/M_mesure->N;
    double t_n;

    //on crée un tableau pour enregistrer les valeurs de T_n voulues
    // on n'alloue pas chaque case du tableau de manière dynamique car 
    // tab sera composé des pointeurs de M_sol qu'on souhaite analyser
    Vecteur** tab=new Vecteur*[6];

    //on enregsitre les résultats
    for(int n=1; n<N+1; n++){
        t_n=n*dt;
        if(std::abs(t_n-15)<eps){ 
            tab[0]=M_sol[n];
        }
        if(std::abs(t_n-30)<eps){ 
            tab[1]=M_sol[n];
        }
        if(std::abs(t_n-60)<eps){ 
            tab[2]=M_sol[n];
        }
        if(std::abs(t_n-90)<eps){ 
            tab[3]=M_sol[n];
        }
        if(std::abs(t_n-150)<eps){
            tab[4]=M_sol[n];
        }
        if(std::abs(t_n-210)<eps){
            tab[5]=M_sol[n]; 
        }
    }

    return tab;
}

// Visualisation 1D (écriture fichier csv)
void Modele_instationnaire_flux_const::visualisation1D_solution_instationnaire_flux_constant(){
    std::cout << "Création fichier solution 1D modèle instationnaire flux constant." << std::endl;
    Vecteur** tab = donnees_a_analyser_instationnaire_flux_constant();
    int M=M_mesure->M;
    double h=M_mesure->L_x/M;
    
    std::ostringstream filename; 
    filename << "../resultats/fichiers_resultats/solution1D_instat_flux_constant.csv";
    std::ofstream ofile(filename.str());
    ofile << "x, t=15s, t=30s, t=60s, t=90s, t=150s, t=210s\n";
    for(int i=0; i<M+1; i++){
        ofile << i*h << ", " << (*(tab[0]))[i] << ", " << (*(tab[1]))[i] 
            << ", " << (*(tab[2]))[i] << ", " << (*(tab[3]))[i]
            << ", " << (*(tab[4]))[i] << ", " << (*(tab[5]))[i] << "\n";
    }
    ofile.close();
    delete [] tab;
}

/*
RESOLUTION 3D MODELE INSTATIONNAIRE FLUX CONSTANT
*/

void Modele_instationnaire_flux_const::visualisation3D_solution_instationnaire_flux_constant(){
    std::cout << "Création fichier solution 3D modèle instationnaire flux constant :" << std::endl;
    int M_x=M_mesure->M_x; int M_y=M_mesure->M_y; int M_z=M_mesure->M_z;
    int N=M_mesure->N;
    for(int n=0; n<N+1; n++){
        if(n % ((N+1)/20) == 0){
            affiche_progression(n / ((N+1)/20), 20);
        }
        std::ostringstream filename;
        filename << "../resultats/fichiers_resultats/solution3D_instat_flux_constant/solution3D_flux_constant." << n <<".vtk";
        std::ofstream ofile(filename.str());
        def_maillage(*M_mesure,ofile);
        ofile << "POINT_DATA " << (M_x+1)*(M_y+1)*(M_z+1) << "\n";
        ofile << "FIELD FieldData 1\n";
        ofile << "sol1 1 " << (M_x+1)*(M_y+1)*(M_z+1) << " float\n";
        Vecteur* T_hat=def_temperature_interpolee(*M_mesure,*(M_sol[n]));
        for(int k=0; k<M_z+1; k++){
            for(int j=0; j<M_y+1; j++){
                for(int i=0; i<M_x+1; i++){
                    ofile << (*T_hat)[i] << "\n";
                }
            }
        }
        ofile.close();
        delete T_hat;
    }
}

/*
CONVERGENCE MODELE INSTATIONNAIRE VERS MODELE STATIONNAIRE
*/

void Modele_instationnaire_flux_const::visualisation_convergence_modele(Vecteur* sol_stat){
    int N=M_mesure->N;
    int M=M_mesure->M;
    double dt=(double)(M_mesure->T_final)/M_mesure->N;
    std::cout << "Création fichier convergence modèle instationnaire flux constant vers modèle stationnaire." << std::endl;
    std::ostringstream filename; 
    filename << "../resultats/fichiers_resultats/convergence_instat_vers_stat.csv";
    std::ofstream ofile(filename.str());
    ofile << "t, erreur\n";    
    double erreur=0.;
    for(int n=0; n<N+1; n++){
        for(int i=0; i<M+1; i++){
            if(std::abs((*M_sol[n])[i]-(*sol_stat)[i]) > erreur){
                erreur=std::abs((*M_sol[n])[i]-(*sol_stat)[i]);
            }
        }
        ofile << n*dt << ", " << erreur << "\n";
        erreur=0.;
    }
    ofile.close();
}