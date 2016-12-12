#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

long long int max(long long int a,long long int b){
	if (a >= b){
		return a;
	}else{
		return b;
	}
}
int main(int argc, const char* argv[] ){
	ifstream prueba(argv[1]);
	vector<int> arr;
	int n;
	int current;
	vector<long long int> solution;
	long long int maximo = 0;
	
	prueba >> n;
	if (n != 0){
		while (prueba >> current){
			arr.push_back(current);
		}
	}
	
	for(int i=0; i<arr.size(); i++){
		solution.push_back(0);
	}					
	
	for(int i=0; i<arr.size(); i++){
		if (i == 0) {
			solution[0] = arr[0];		
		}else{
	  		solution[i] = max(arr[i],solution[i-1]+arr[i]);		//la solucion se arma en base a la solucion anterior
		}	
		maximo = max(maximo,solution[i]);			//actualizo el maximo
	}
	cout << maximo << endl;
}
