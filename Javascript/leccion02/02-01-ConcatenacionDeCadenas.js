var nombre = 'Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+' '+apellido; //Primera concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Rosalia'+' '+'Lotierzo'; //Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a der siguiendo la cadena lee el numero como str
console.log(juntos);
juntos = nombre + 78 + 17; //Cuando no usamos los parentesis los concatena
console.log(juntos);
juntos = nombre + (78 + 17); //Cuando usamos los parentesis y dentro hay numeros los suma
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido; //Tercera concatenacion usando el operador simplificado
console.log(nombre);
