#include "modele_stationnaire.hpp"

// Pour construire la matrice A
void Modele_stationnaire::def_matrice_tridiag_stationnaire(){
    int M=M_mesure->M;
    double h=M_mesure->L_x/M;
    double p=2*(M_mesure->L_y+M_mesure->L_z);
    double S=M_mesure->L_y*M_mesure->L_z;

    double* a=new double[M];
    double* b=new double[M+1];
    double* c=new double[M];
    
    for(int i=0; i<M-1; i++){
        a[i]=-M_mesure->K/pow(h,2);
    }
    a[M-1]=-M_mesure->K/h;

    for(int i=1; i<M; i++){
        b[i]=2*M_mesure->K/pow(h,2)+M_mesure->h_c*p/S;
    }
    b[0]=M_mesure->K/h; b[M]=M_mesure->K/h;

    for(int i=1; i<M; i++){
        c[i]=-M_mesure->K/pow(h,2);
    }
    c[0]=-M_mesure->K/h;

    M_A=new Matrice_tridiag(M+1,a,b,c);
    delete [] a; delete [] b; delete [] c;
}

// Pour construire le vecteur F
void Modele_stationnaire::def_second_membre(){
    int M=M_mesure->M;
    double p=2*(M_mesure->L_y+M_mesure->L_z);
    double S=M_mesure->L_y*M_mesure->L_z;

    double* v=new double[M+1];

    for(int i=1; i<M; i++){
        v[i]=M_mesure->h_c*p*M_mesure->T_e/S;
    }
    v[0]=M_mesure->phi; v[M]=0;

    M_F=new Vecteur(M+1,v);
    delete [] v;
}

// Pour calculer la solution analytique
Vecteur* Modele_stationnaire::T_exact(){
    int M=M_mesure->M;
    double h=M_mesure->L_x/M;
    double p=2*(M_mesure->L_y+M_mesure->L_z);
    double S=M_mesure->L_y*M_mesure->L_z;
    double a=M_mesure->h_c*p/(M_mesure->K*S);
    Vecteur* T=new Vecteur(M+1);
    for(int i=0; i<M+1; i++){
        (*T)[i]=M_mesure->T_e+M_mesure->phi/M_mesure->K*cosh(sqrt(a)*M_mesure->L_x)/(sqrt(a)*sinh(sqrt(a)*M_mesure->L_x))*
            cosh(sqrt(a)*(M_mesure->L_x-i*h))/cosh(sqrt(a)*M_mesure->L_x);
    }
    return T;
}

// Resolution 1D du modèle stationnaire
void Modele_stationnaire::resolution_stat_1D(){
    int M=M_mesure->M;
    Matrice_tridiag** LU=def_LU(*M_A);

    Vecteur* Y=new Vecteur(M+1); 
    Descente_mat_tridiag(*Y,*LU[0],*M_F);   
    Remontee_mat_tridiag(*M_sol,*LU[1],*Y);
    delete Y;
    delete LU[0]; delete LU[1]; delete [] LU;
}

// Visualisation 1D (écriture fichier csv)
void Modele_stationnaire::visualisation1D_solution_stationnaire(){
    std::cout << "Création fichier solution 1D modèle stationnaire." << std::endl;
    int M=M_mesure->M;
    double h=M_mesure->L_x/M;
    Vecteur* T=T_exact();
    std::ostringstream filename; 
    filename << "../resultats/fichiers_resultats/solution1D_stat_Lx" << M_mesure->L_x*1000 << ".csv";
    std::ofstream ofile(filename.str());
    ofile << "x, sol, sol_exacte\n";
    for(int i=0; i<M+1; i++){
        ofile << i*h << ", " << (*M_sol)[i] << ", " << (*T)[i] << "\n";
    }
    ofile.close();
    delete T;
}

// Visualisation 3D (ecriture fichier vtk)
void Modele_stationnaire::visualisation3D_solution_stationnaire(){
    std::cout << "Création fichier solution 3D modèle stationnaire." << std::endl;
    int M_x=M_mesure->M_x; int M_y=M_mesure->M_y; int M_z=M_mesure->M_z;
    std::ostringstream filename; 
    filename << "../resultats/fichiers_resultats/solution3D_stat.vtk";
    std::ofstream ofile(filename.str());
    def_maillage(*M_mesure,ofile);
    ofile << "POINT_DATA " << (M_x+1)*(M_y+1)*(M_z+1) << "\n";
    ofile << "FIELD FieldData 1\n";
    ofile << "sol1 1 " << (M_x+1)*(M_y+1)*(M_z+1) << " float\n";
    Vecteur* T_hat=def_temperature_interpolee(*M_mesure,*M_sol);
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