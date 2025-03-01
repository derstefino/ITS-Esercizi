'''S1-5. Si scriva un programma che converta la temperatura da Fahrenheit a Celsius utilizzando la formula

gradiCelsius=5∗(gradiFahrenheit−32)/9

Si inizializzi una temperatura espressa in gradi Fahrenheit con un numero intero.

La temperatura deve essere convertita e visualizzata in gradi Celsius con un numero in virgola mobile con una precisione di un decimo di grado.

Un possibile esempio di output potrebbe essere il seguente:

72 gradi Fahrenheit corrispondono a 22.2 gradi Celsius.'''

temp_Fahr:int = 70

gradiCelsius:float = 5 * ((temp_Fahr - 32) / 9)

print(f"{temp_Fahr} gradi Fahrenheit corrispondono a {gradiCelsius:.1f} gradi Celsius")