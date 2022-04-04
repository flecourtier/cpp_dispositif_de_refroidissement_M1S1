#include "modele_instationnaire.hpp"

// Pour construire la matrice A
void Modele_instationnaire::def_matrice_tridiag_instationnaire(){
    int M=M_mesure->M;
    double h=M_mesure->L_x/M;
    double p=2*(M_mesure->L_y+M_mesure->L_z);
    double S=M_mesure->L_y*M_mesure->L_z;
    double dt=(double)(M_mesure->T_final)/M_mesure->N;

    double* a=new double[M];
    double* b=new double[M+1];
    double* c=new double[M];
    
    for(int i=0; i<M-1; i++){
        a[i]=-M_mesure->K/pow(h,2);
    }
    a[M-1]=-M_mesure->K/h;
    for(int i=1; i<M; i++){
        b[i]=M_mesure->rho*M_mesure->C_p/dt+2*M_mesure->K/pow(h,2)+M_mesure->h_c*p/S;
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
void Modele_instationnaire::def_second_membre(){
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