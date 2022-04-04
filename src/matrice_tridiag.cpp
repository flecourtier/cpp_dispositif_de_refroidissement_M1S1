#include "matrice_tridiag.hpp"

//constructeurs
Matrice_tridiag::Matrice_tridiag(int m) : M(m), M_a(new double[m-1]), M_b(new double[m]), M_c(new double[m-1]){
    for(int i=0; i<m-1; i++){
        M_a[i]=0;
        M_b[i]=0;
        M_c[i]=0;
    }
    M_b[m-1]=0;
};

Matrice_tridiag::Matrice_tridiag(int m, double* a, double* b, double* c) : M(m), M_a(new double[M-1]), M_b(new double[M]), M_c(new double[M-1]){
    for(int i=0; i<M-1; i++){
        M_a[i]=a[i];
        M_c[i]=c[i];
    }
    for(int i=0; i<M; i++){
        M_b[i]=b[i];
    }
};

Matrice_tridiag::Matrice_tridiag(const Matrice_tridiag &A) : M(A.get_M()), M_a(new double[A.get_M()-1]), M_b(new double[A.get_M()]), M_c(new double[A.get_M()-1]){
    for(int i=0; i<A.get_M()-1; i++){
        this->M_a[i]=A.M_a[i];
        this->M_c[i]=A.M_c[i];
    }
    for(int i=0; i<A.get_M(); i++){
        this->M_b[i]=A.M_b[i];
    }
}