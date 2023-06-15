class Persona{

    contadorPersonas = 0;

    constructor(nombre, apellido, edad){
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
        
    }

    get _idPersona(){
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
        Id: ${this._id_persona}
        Nombre: ${this._nombre}
        Apellido: ${this._apellido}
        Edad: ${this._edad}`
    }

}

class Empleado extends Persona{
    constructor(nombre, apellido, edad, salario){
        super(nombre, apellido, edad);
        this._salario = salario;
    }

    get id_empleado(){
        return this._id_empleado;
    }

    get salario(){
            return this._salario;
        }
    
    set salario(salario){
        this._salario = salario;
        }

    toString(){
        return super.toString + ' Salario: '+ this._salario
    }
}

class Gerente extends Persona{
    constructor(nombre, apellido, edad, salario){
        super(nombre, apellido, edad);
        this._id_
        this._salario = salario;
    }
}

