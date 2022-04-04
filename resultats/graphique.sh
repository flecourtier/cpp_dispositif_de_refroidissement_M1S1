#!/bin/sh

case $1 in
    0)
        echo "Tout : "
        cd creation_graphiques/
        echo "#Maillage 3D"
        pvpython maillage3D.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique 3D maillage créé"
        else
            echo "-> ERREUR : graphique 3D maillage non créé"
        fi
        echo "#Cas stationnaire"
        python solution1D_stat.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique 1D modèle stationnaire créé"
        else
            echo "-> ERREUR : graphique 1D modèle stationnaire non créé"
        fi
        pvpython solution3D_stat.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique 3D modèle stationnaire créé"
        else
            echo "-> ERREUR : graphique 3D modèle stationnaire non créé"
        fi
        echo "#Cas instationnaire"
        python solution1D_instat.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique 1D modèle instationnaire flux constant créé"
            echo "-> graphique 1D modèle instationnaire activ-desactiv créé"
        else
            echo "-> ERREUR : graphique 1D modèle instationnaire non créé"
        fi
        python convergence_modele_instat.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique convergence créé"
        else
            echo "-> ERREUR : graphique convergence non créé"
        fi
        echo " "
        echo "Voulez-vous créer les vidéos du modèle instationnaire ? (0=Non,1=Oui)"
        echo "Attention : cela prendra un peu de temps"
        read creation_video
        if [ $creation_video -eq 1 ]; then
            pvpython solution3D_instat_flux_constant.py
            pvpython solution3D_instat_activ_desactiv.py
            if [ $? -eq 0 ]; then 
                echo "-> video solution 3D modèle instationnaire flux constant créée"
                echo "-> video solution 3D modèle instationnaire activ-desactiv créée"
            else
                echo "-> ERREUR : video 3D modèle instationnaire non créée"
            fi
        else
            echo "-> video 3D modèle instationnaire non créée"
        fi
        break
        ;;
	1)
		echo "Cas stationnaire : "
        cd creation_graphiques/
        python solution1D_stat.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique 1D modèle stationnaire créé"
        else
            echo "-> ERREUR : graphique 1D modèle stationnaire non créé"
        fi
        pvpython solution3D_stat.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique 3D modèle stationnaire créé"
        else
            echo "-> ERREUR : graphique 3D modèle stationnaire non créé"
        fi
        break
		;;
	2)
		echo "Cas instationnaire : "
        cd creation_graphiques/
        python solution1D_instat.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique 1D modèle instationnaire flux constant créé"
            echo "-> graphique 1D modèle instationnaire activ-desactiv créé"
        else
            echo "-> ERREUR : graphique 1D modèle instationnaire non créé"
        fi
        python convergence_modele_instat.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique convergence créé"
        else
            echo "-> ERREUR : graphique convergence non créé"
        fi
        echo " "
        echo "Voulez-vous créer les vidéos du modèle instationnaire ? (0=Non,1=Oui)"
        echo "Attention : cela prendra un peu de temps"
        read creation_video
        if [ $creation_video -eq 1 ]; then
            pvpython solution3D_instat_flux_constant.py
            pvpython solution3D_instat_activ_desactiv.py
            if [ $? -eq 0 ]; then 
                echo "-> video solution 3D modèle instationnaire flux constant créée"
                echo "-> video solution 3D modèle instationnaire activ-desactiv créée"
            else
                echo "-> ERREUR : video 3D modèle instationnaire non créée"
            fi
        else
            echo "-> videos 3D modèle instationnaire non créée"
        fi
        break
		;;
    3)
        echo "Maillage 3D : "
        cd creation_graphiques/
        pvpython maillage3D.py
        if [ $? -eq 0 ]; then 
            echo "-> graphique 3D maillage créé"
        else
            echo "-> ERREUR : graphique 3D maillage non créé"
        fi
        break
		;;
	*)        
		echo "0 = Tout"
        echo "1 = Cas stationnaire"
        echo "2 = Cas instationnaire"
        echo "3 = Maillage 3D"
        break
		;;
esac
