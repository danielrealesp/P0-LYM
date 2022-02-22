# Integrantes

#### Daniel Reales (201822265)
#### Juan Sebastian Pinzon (202013144)


# Aclaraciones Importantes

1. El parser construido entiende un bloque, como se expone en el enunciado, como una serie de instrucciones. Debido a que las instrucciones pueden ser o bien ***comandos*** o ***estructuras de control***, no se admiten bloques conformados por condiciones. Por ejemplo, la siguiente declaracion no es valida por el motivo expuesto (note que el bloque interior es un condicional):
		
		(defun blocked-p ()
			(not (can-move-p :north)))

2. Como se menciona en el enunciado, los bloque estan delimitados por paréntesis. Por lo tanto condicionales tales como:

		(if (blocked-p) (move 1) (skip))

No son validas. La correción sería:

		(if (blocked-p) ((move 1)) ((skip)))

3. Se asumió que los terminales para  ***chips*** y ***balloons*** son ***:chips*** y ***balloons***, respectivamente. Por tanto se reconocen condiciones tales como:

		(can-put-p :chips 3)
		(can-pick-p :balloons 5)

4. Para facilitar la prueba se incluyen programas de ejemplo que incluyen características como recursión, definición de variables y funciones.

