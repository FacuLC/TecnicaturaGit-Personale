
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
        ${this._idEmpleado} 
        Salario: ${this._salario}
        `
    }
}

