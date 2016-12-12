#include <iostream>
#include <string>
using namespace std;

class Nodo {
	public:

	int wordUnder;
	Nodo*  children [256];
	Nodo(){
		this->wordUnder = 0;
		for(int i = 0; i<256; i++){
			this->children[i] = NULL;		
		}
	}
};

class Trie {
	public:

	Nodo* root;

	Trie(){
		this->root = new Nodo();
	}
	
	void agregar_palabra(string palabra){
		Nodo* current = this->root;
		for(int i = 0; i < palabra.size();i++){
			
			if (current->children[(int) palabra[i]] == NULL) {
				current->children[(int) palabra[i]] = new Nodo();
			}
			current->wordUnder += 1;
			current = current->children[(int) palabra[i]];			
		}
	}
	
	int palabras_con_prefijo(string prefijo){
		Nodo* current = this->root;
		for(int i = 0; i < prefijo.size();i++){
			
			if (current->children[(int) prefijo[i]] == NULL) {
				return 0;
			}
			else{
				current = current->children[(int) prefijo[i]];
			}
		}
		return current->wordUnder;
	}
};



int main() {
	
	Trie* trie = new Trie();

	int n;
	cin >> n;
	string prefijos[n];

	for(int i = 0; i < n; i++){
		string s;
		int l;
		cin >> s >> l;
		trie->agregar_palabra(s);
		prefijos[i] = s.substr(0,l);	
	}

	int maximo = -1;

	for(int i = 0; i < n; i++){
		int palabras_debajo = trie->palabras_con_prefijo(prefijos[i]);
		if (palabras_debajo > maximo) {
			maximo = palabras_debajo;		
		}
	}

	cout << maximo << endl;
	
}

