class Persona{

    static contadorPersonas = 0;

    constructor(nombre, apellido, edad,){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
        
    }

    get idPersona(){
        return this._idPersona;
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

    get edad(){
        return this._edad;
    
    }

    set edad(edad){
        this._edad = edad;
    }


    toString(){
        return `
        Id: ${this._idPersona}
        Nombre: ${this._nombre}
        Apellido: ${this._apellido}
        Edad: ${this._edad}`
    }

}

class Empleado extends Persona{
    
    static contadorEmpleados = 0

    constructor(nombre, apellido, edad, salario){
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadorEmpleados;
        this._salario = salario;
    }

    get idEmpleado(){
        return this._idEmpleado;
    }

    get salario(){
            return this._salario;
        }
    
    set salario(salario){
        this._salario = salario;
        }

    toString(){
        return `
        ${super.toString} 
        Id Empleado: ${this._idEmpleado} 
        Salario: ${this._salario}`
    }
}

class Cliente extends Persona{

    static contadorCliente = 0;
    constructor(nombre, apellido, edad, fechaRegistro){
            super(nombre, apellido, edad);
            this._idCliente = ++Cliente.contadorCliente;
            this._fechaRegistro = fechaRegistro
        }

    get idCliente(){
        return this._idCliente;
        }

    get fechaRegistro(){
        return this._fechaRegistro;
    }

    set fechaRegistro(fecha){
        this._fechaRegistro = fecha;
    }


    toString() {
        return `
        ${super.toString()} 
        ${this._idCliente} 
        ${this._fechaRegistro}
        `
    }
}

let persona1 = new Persona('Facundo', 'Cano', '22');

console.log(persona1.toString());

let empleado1 = new Empleado('Leonel', 'Shelion', '24', '2137641');

console, console.log(empleado1.toString());