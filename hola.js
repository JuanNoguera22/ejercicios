/*ejercicio 7
var numeros, suma;
 numeros =[1,2,3,7,0];
for (var i=0 in numeros) {
  for (var a=0 in numeros) {
    suma = numeros[a]+numeros[i];
    if (suma == 10) {
      console.log(numeros[a]+ ' + '+ numeros[i]);
    }
  }
} */

/*ejercicio 6
var myArray, contador, numero;
 
 myArray = [1,5,5,7,6,7,7,1];
 
 for (var i=0 in myArray) {
   for (var a=0 in myArray) {
     if (myArray[a] > myArray[i]) {
       numero = myArray[a];
     }
   }
   contador=0
   for (var b in myArray) {
     if (numero == myArray[b]) {
       contador++;
     }
   }
   
 }
 console.log('el numero mayor es '+ numero +' se repite '+ contador);*/

/*ejercico 5
var myArray = [1,1,2,2,3,3,3,5,5,1];
var numeros = [1,2,3,4,5]
var muestra = "= ";

for (var a in numeros) {
  var muestra = "= "
  for (var b in myArray) {
    if (numeros[a]==myArray[b]) {
      muestra+='*'
    }
  }
  console.log(numeros[a]+muestra);
  
}*/