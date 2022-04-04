#include "mi_activ_desactiv.hpp"

// On définit la solution en fonction du temps
void Modele_instationnaire_activ_desactiv::def_solution_activ_desactiv(){
    int M=M_mesure->M;
    double dt=(double)(M_mesure->T_final)/M_mesure->N;
    double eps=pow(10,-3);

    //on initialise T_0
    Vecteur* T_n=new Vecteur(M+1);
    for(int i=0; i<M+1; i++){
        (*T_n)[i]=M_mesure->T_e;
        (*M_sol)[0][i]=M_mesure->T_e;
    }
    
    //On détermine la facto LU de A
    Matrice_tridiag** LU=def_LU(*M_A);

    //on crée le vecteur qu'on va multiplier à T_n
    Vecteur* alpha=new Vecteur(M+1);
    for(int i=1; i<M; i++){
        (*alpha)[i]=M_mesure->rho*M_mesure->C_p/dt;
    }

    //on résout le modèle instationnaire
    double t=0.; 
    Vecteur* Y=new Vecteur(M+1);
    for(int n=1; n<M_mesure->N+1; n++){
        Descente_mat_tridiag(*Y,*LU[0],(*alpha)*(*T_n)+(*M_F));
        Remontee_mat_tridiag(*T_n,*LU[1],*Y);
        //activation-desactivation
        t=t+dt;
        if(std::abs(t-30)<eps){
            if((*M_F)[0]==M_mesure->phi){ (*M_F)[0]=0;}
            else{ (*M_F)[0]=M_mesure->phi; }
            t=0.;
        }
        for(int i=0; i<M+1; i++){
            (*M_sol[n])[i]=(*T_n)[i];
        }
    }
    delete T_n; delete alpha; delete Y;
    delete LU[0]; delete LU[1]; delete [] LU;
}

/*
RESOLUTION 1D MODELE INSTATIONNAIRE ACTIV DESACTIV
*/

// On crée un tableau avec les valeurs que l'on souhaite récupérée
// Ici on veut récupérer la température en 3 points de l'ailette
Vecteur** Modele_instationnaire_activ_desactiv::donnees_a_analyser_instationnaire_activ_desactiv(){
    int M=M_mesure->M;
    int N=M_mesure->N;

    //on crée un tableau pour enregistrer les valeurs de T_n voulues
    Vecteur** tab=new Vecteur*[3];
    for(int i=0; i<3; i++){
        tab[i]=new Vecteur(N+1);
    }

    //on enregsitre les résultats
    for(int n=0; n<M_mesure->N+1; n++){
        (*(tab[0]))[n]=(*(M_sol[n]))[0];
        (*(tab[1]))[n]=(*(M_sol[n]))[M/2];
        (*(tab[2]))[n]=(*(M_sol[n]))[M];
    }

    return tab;
}

// Visualisation 1D (écriture fichier csv)
void Modele_instationnaire_activ_desactiv::visualisation1D_solution_instationnaire_activ_desactiv(){
    std::cout << "Création fichier solution 1D modèle instationnaire activ/desactiv." << std::endl;
    int N=M_mesure->N;
    double dt=(double)(M_mesure->T_final)/N;
    Vecteur** tab = donnees_a_analyser_instationnaire_activ_desactiv();
    std::ostringstream filename; 
    filename << "../resultats/fichiers_resultats/solution1D_instat_activ_desactiv.csv";
    std::ofstream ofile(filename.str());
    ofile << "time, x_0, x_{M/2}, x_{M}\n";
    for(int n=0; n<N+1; n++){
        ofile << n*dt << ", " << (*(tab[0]))[n] << ", " << (*(tab[1]))[n] 
            << ", " << (*(tab[2]))[n] << "\n";
    }
    ofile.close();
    for(int i=0; i<3; i++){
        delete tab[i];
    }
    delete [] tab;
}

/*
RESOLUTION 3D MODELE INSTATIONNAIRE FLUX CONSTANT
*/

void Modele_instationnaire_activ_desactiv::visualisation3D_solution_instationnaire_activ_desactiv(){
    std::cout << "Création fichier solution 3D modèle instationnaire activ/desactiv : " << std::endl;
    int M_x=M_mesure->M_x; int M_y=M_mesure->M_y; int M_z=M_mesure->M_z;
    int N=M_mesure->N;
    for(int n=0; n<N+1; n++){
        if(n % ((N+1)/20) == 0){
            affiche_progression(n / ((N+1)/20), 20);
        }
        std::ostringstream filename;
        filename << "../resultats/fichiers_resultats/solution3D_instat_activ_desactiv/solution3D_activ_desactiv." << n <<".vtk";
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