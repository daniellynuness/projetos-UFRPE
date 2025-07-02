def fahr_to_celsius(temp_f):
  """Converte uma temperatura de Fahrenheit para Celsius."""
  return (temp_f - 32) * (5 / 9)

try:
  temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit a ser convertida: "))

  temp_celsius = int(fahr_to_celsius(temp_fahrenheit))

  print("\n--- Resultado ---")
  print(f"A temperatura de {temp_fahrenheit}°F equivale a {temp_celsius:.2f}°C.")

except ValueError:
  print("\nErro: Por favor, insira um valor numérico válido.")