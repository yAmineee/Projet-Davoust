package helper;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Set;



public class FrenchDico {

	public static void main(String[] args) {

		// Dictionnaire français contenant K = mot & V = définitions
		HashMap<String, String> dictionnaire = extraireMots("./src/helper/dico.txt");
		
		// Fichier texte contenant uniquement les mots du dictionnaire Fr
		ecritureDesMots(dictionnaire);
		

	}
	
	
	/**
	 * Extrait les mots du dictionnaire passé en paramètre et sauvegarde dans un hashmap
	 * @param chemin_du_fichier : chemin du fichier texte à lire
	 * @return un hashmap avec K= le mot , V= la définition du mot 
	 * */
	private static HashMap<String, String> extraireMots(String chemin_du_fichier) {
		
		HashMap<String, String> dico = new HashMap<String, String>();
		
		try {
			
			//Lecture du fichier texte
			File fichier = new File (chemin_du_fichier);
			FileReader fR = new FileReader (fichier);
			BufferedReader bR = new BufferedReader(fR);
			
			
			String line = "";	// Représetne la valeur d'une ligne du fichier texte.
			String dicoKey = "";	// Représente la key du Hashmap (un mot)
			String dicoValue = "";	// Représente la value du Hashmap (la def du mot)
			String[] temp = null;
			
			while(bR.ready()) {
				
				line = bR.readLine() ;		// Récupérer le contenu de la prochaine ligne
				//temp = line.split(",",2);	// Séparer un mot de sa ou ses définition.s [,[\".\"]]
				temp = line.split("[,[\".\"]]",2);	// Séparer un mot de sa ou ses définition.s [,[\".\"]]
				
				dicoKey = temp[0];
				dicoValue = temp[1];
				
				dico.put(dicoKey, dicoValue);	// Ajout du mot et de sa valeur au Hashmap
				
			}
			
			bR.close(); 	//Fermer le buffer
			
		}catch ( FileNotFoundException f) {
			f.printStackTrace();
		}catch ( IOException e) {
			e.printStackTrace();
		}
		
		return dico;
	}//Fin de extraireMots()

	private static void ecritureDesMots(HashMap<String, String> dico ) {
		
		List<String> listeMots = new ArrayList<String>(dico.keySet());
		Collections.sort(listeMots);
		
		try {
			
			//Ecriture dans un nouveau fichier texte
			FileWriter fW = new FileWriter("./src/helper/ListeMotsFr.txt");
			BufferedWriter bW = new BufferedWriter(fW);
			
			
			
			for(String mot : listeMots) {
				bW.write(mot);
				bW.newLine();
				
			}
			
			bW.close();
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}//Fin de ecritureDesMots()
	
}
