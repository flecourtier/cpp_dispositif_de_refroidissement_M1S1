#include "utils.hpp"

/*
BARRE DE CHARGEMENT
*/

void affiche_progression(int pas, int max_pas){
    if(pas==0){
        std::cout << "[>" << std::string(max_pas-pas-1, ' ') << "]   " << pas*100/max_pas << "%\r";
    }
    else if(pas*100/max_pas<10){
        std::cout << "["  << std::string(pas, '=') << ">" << std::string(max_pas-pas-1, ' ') << "]   " << pas*100/max_pas << "%\r";
    }
    else if (pas == max_pas) {
        std::cout << "["  << std::string(pas, '=') << "] " << pas*100/max_pas << "%" << std::endl;
    }
    else{
        std::cout << "["  << std::string(pas, '=') << ">" << std::string(max_pas-pas-1, ' ') << "]  " << pas*100/max_pas << "%\r";
    }
    std::cout.flush();
}

/*
CONSTRUCTION DU MAILLAGE
*/

// Pour écrire les points du maillage 3D dans les fichiers vtk
void def_maillage(const Mesures& mesure,std::ofstream& ofile){
    int M_x=mesure.M_x; int M_y=mesure.M_y; int M_z=mesure.M_z;

    ofile << "# vtk DataFile Version 2.0\nvtk output\nASCII\nDATASET STRUCTURED_GRID\n";
    ofile << "DIMENSIONS " << M_x+1 << " " << M_y+1 << " " << M_z+1 << "\n";
    ofile << "POINTS " << (M_x+1)*(M_y+1)*(M_z+1) << " float\n";

    for(int k=0; k<M_z+1; k++){
        for(int j=0; j<M_y+1; j++){
            for(int i=0; i<M_x+1; i++){
                ofile << i << " " << j << " " << k << "\n";
            }
        }
    }
}

// Pour visualiser le maillage 3D
void visualisation3D_maillage(const Mesures& mesure){
    std::cout << "Création fichier maillage." << std::endl;
    std::ostringstream filename; 
    filename << "../resultats/fichiers_resultats/maillage.vtk";
    std::ofstream ofile(filename.str());
    def_maillage(mesure,ofile);
    ofile.close();
}

/*
FACTO LU
*/

//pour faire la factorisation LU de A
Matrice_tridiag** def_LU(const Matrice_tridiag A){
    int M=A.get_M();
    double* l_a=new double[M-1];
    double* l_b=new double[M]; 
    double* l_c=new double[M-1];
    double* u_a=new double[M-1]; 
    double* u_b=new double[M]; 
    double* u_c=new double[M-1]; 

    //on définit b_i* et c_i*
    l_b[0]=A.get_bi(0); u_c[0]=A.get_ci(0)/l_b[0];
    for(int i=1; i<M-1; i++){
        l_b[i]=A.get_bi(i)-A.get_ai(i-1)*u_c[i-1];
        u_c[i]=A.get_ci(i)/l_b[i];
    }
    l_b[M-1]=A.get_bi(M-1)-A.get_ai(M-2)*u_c[M-2];

    //on définit les autres diagonales manquantes
    for(int i=0; i<M-1; i++){
        l_a[i]=A.get_ai(i);
        l_c[i]=0;
        u_a[i]=0;
        u_b[i]=1;
    }
    u_b[M-1]=1;

    Matrice_tridiag** lu=new Matrice_tridiag*[2];
    lu[0]=new Matrice_tridiag(M,l_a,l_b,l_c); lu[1]=new Matrice_tridiag(M,u_a,u_b,u_c);
    delete [] l_a; delete [] l_b; delete [] l_c;
    delete [] u_a; delete [] u_b; delete [] u_c;
    return lu;   
}

//Résolution de LY=F
void Descente_mat_tridiag(Vecteur& Y,const Matrice_tridiag& L,const Vecteur& F){
    int M=L.get_M();
    Y[0]=F[0]/L.get_bi(0);
    for(int i=1; i<M; i++){
        Y[i]=(F[i]-L.get_ai(i-1)*Y[i-1])/L.get_bi(i);
    }
}

//Résolution de UX=Y
void Remontee_mat_tridiag(Vecteur& X,const Matrice_tridiag& U,const Vecteur& Y){
    int M=U.get_M();
    X[M-1]=Y[M-1];
    for(int i=M-2; i>=0; i--){
        X[i]=Y[i]-U.get_ci(i)*X[i+1];
    }
}

// Définition de la température à partir d'un interpolant linéaire
Vecteur* def_temperature_interpolee(const Mesures& mesure, Vecteur& sol){
    int M_x=mesure.M_x;
    double h_x=mesure.L_x/M_x;
    int M=mesure.M;
    double h=mesure.L_x/M;

    int k; double x_j; double x_i00;
    double a,b;

    Vecteur* T_hat=new Vecteur(M_x+1);
    for(int i=0; i<M_x+1; i++){
        x_i00=i*h_x;
        k=0;
        for(int j=0; j<M+1; j++){
            x_j=j*h;
            if(x_i00>=(x_j-1e-9) and x_i00<=(x_j+h+1e-9)){
                k=j; 
                break;
            }
        }

        //calculer coeff de la droite y=ax+b
        a=(sol[k]-sol[k+1])/(k*h-(k+1)*h);
        b=sol[k]-a*k*h;

        //évaluer T_i_hat
        (*T_hat)[i]=a*x_i00+b;
    }
    return T_hat;
}