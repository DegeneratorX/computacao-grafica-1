#include<iostream>

using std::cin; using std::cout; using std::endl;

#define PI 3.14159265
#define RAIO 5.0
#define FATIAS_VERTICAIS 4
#define FATIAS_HORIZONTAIS 3
#define VERTICES 0
#define INDICES 1

// Funções Blending de Bézier
double b_1(double t){
    return (1.0 - t - t*t + t*t*t);
}

double b_2(double t){
    return (t - 2.0*t*t + t*t*t);
}

double b_3(double t){
    return (t*t - t*t*t);
}

double b_4(double t){
    return (2.0*t*t - t*t*t);
}

void fillVertexArray(){
    int i, j, k;
    // Coordenadas dos pontos P1, P2, P3 e P4 (no caso equivalentes do P0 ao P3)
    double P_1[3] = {1.0, 0.0, 0.0};
    double P_2[3] = {3.5, 0.5, 0.0};
    double P_3[3] = {0.0, 2.5, 0.0};
    double P_4[3] = {2.0, 3.0, 0.0};
    double t,r,z;

    
}

int main(){

}