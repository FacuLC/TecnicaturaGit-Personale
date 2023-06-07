// let persona3 = new Persona('Carla', 'Ponse'); No se puede porque aun no esta definida la calse Persona  

class Persona{// Clase Padre
    constructor(nombre, apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get apellido(){
        return this._apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }
}

// Usamos(extends) para unir la Clase Padre(Persona) con la Clase Hija(Empleado)
class Empleado extends Persona{
    constructor(nombre, apellido, departamento){
        super(nombre, apellido);// Se utiliza (super) para llamar a los atributos de la clase Padre
        this._departamento = departamento;
    }
    
    get departamento(){
        return this._departamento;
    }
    
    set departamento(departamento){
        return this._departamento = departamento
    }
}
// Caso Nombre persona1
let persona1 = new Persona('Martin', 'Perez');
console.log(persona1.nombre);
persona1.nombre = 'Facundo';
console.log(persona1.nombre)

// Caso Apellido persona1
console.log(persona1.apellido);
persona1.apellido = 'Cano';
console.log(persona1.apellido);
console.log(persona1);

//----------------------------------------------------------------

// Caso Nombre persona2
let persona2 = new Persona('Lucas', 'Rojas');
console.log(persona2.nombre);
persona2.nombre ='Leonel';
console.log(persona2.nombre);

// Caso Apellido persona2
console.log(persona2.apellido);
persona2.apellido = 'Romero'
console.log(persona2.apellido);
console.log(persona2);

// Caso Clase Hija
let empleado1 = new Empleado('Leo','Ferro', 'Sistemas');
console.log(empleado1);
console.log(empleado1.nombre);