// JavaScript Document

function mostrarFecha(){
	var fecha=new Date();
	var horas=fecha.getHours();
	var minutos=fecha.getMinutes();
	var segundos=fecha.getSeconds();
	
	//si el parametrto fecha a sacado a sacado lo correcto
	//console.log; permite testear la variable fecha
	//console.log('fecha: ', fecha);
	
	var fechaMostrar=horas+':'+minutos+':'+segundos;
	var barra=document.getElementById('barra');
	
	//console.log('barra: ', barra);
	
	barra.innerHTML=fechaMostrar;
	setTimeout("mostrarFecha()", 1000);
	}
	
	function dialogos(){
		var nombre=prompt('Ingrese su nombre: ');
		if(nombre){
			var confirmacion=confirm('esta seguro de registrar sun nombre: ');
			if(confirmacion){
				alert(nombre+ ', sus datos se registraron  correctamente!!!');
				}
			}
		}
		
		function desplegarValor(valor){
			document.miFormulario.visor.value+=valor;
			}
			
		function calcular(){
			var resultado=eval(document.miFormulario.visor.value);
			document.miFormulario.visor.value=resultado;
		}
				
				
		function cambiarVegetal(vegetal){
				var direccion="imagenes/"+vegetal+".jpg";
				document.getElementById('miGrafico').src=direccion;
		}