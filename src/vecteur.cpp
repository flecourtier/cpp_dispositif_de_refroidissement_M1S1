#include "vecteur.hpp"

//constructeurs
Vecteur::Vecteur(int m) : M(m), M_v(new double[m]){
    for(int i=0; i<m; i++){
        M_v[i]=0;
    }
};

Vecteur::Vecteur(int m, double* v) : M(m), M_v(new double[m]){
    for(int i=0; i<m; i++){
        M_v[i]=v[i];
    }
};

Vecteur::Vecteur(const Vecteur &vec) : M(vec.get_M()), M_v(new double[vec.get_M()]){
    for(int i=0; i<M; i++){
        this->M_v[i]=vec.M_v[i];
    }
}

//surcharges d'opérateurs
Vecteur Vecteur::operator=(Vecteur const &v){ //modif : comparer les tailles
    if (&v != this){
        for (int i = 0; i < this->get_M(); i++)
        {
            (*this)[i]=v[i];
        }
    }
    return *this;
}

Vecteur operator+(Vecteur const &v1, Vecteur const &v2){
    if(v1.get_M()==v2.get_M()){
        Vecteur result(v1.get_M());
        for(int i=0; i<v1.get_M();i++){
            result[i]=v1[i]+v2[i];
        }
        return result;
    }
    else{
        std::cout << "Impossible d'additionner (tailles différentes)" <<std::endl;
        return v1;
    }
}

Vecteur operator*(Vecteur const &v, double alpha) { 
    Vecteur result(v.get_M());
    for(int i=0; i<v.get_M();i++){
        result[i]=v[i]*alpha;
    }
    return result;
}

Vecteur operator*(double alpha, Vecteur const &v){ 
    return v * alpha; 
}

Vecteur operator*(Vecteur const &v1, Vecteur const &v2){ //modif : comparer les tailles
    Vecteur result(v1.get_M());
    for(int i=0; i<v1.get_M();i++){
        result[i]=v1[i]*v2[i];
    }
    return result;
}