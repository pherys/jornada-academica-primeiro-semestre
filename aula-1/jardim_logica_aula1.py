# Este é um script Python baseado no pseudocódigo
# "INÍCIO (Cuidar da Planta)"

# --- Simulação da Verificação ---
# No pseudocódigo, o "Passo 2: Verificar se a terra está seca" é uma verificação.
#
#
# Tente mudar o valor de True para False e veja o que acontece!
terra_esta_seca = True

# --- Início da Lógica ---
print("--- INÍCIO (Cuidar da Planta) ---")
print("1: Ir até o vaso...")
print(f"2: Verificando a terra... (Resultado: está seca? {terra_esta_seca})")

# Esta é a tradução direta do "SE / SENÃO"
# Em Python, usamos "if" (SE), "else" (SENÃO)

if terra_esta_seca == True:
    #  SE (a terra está seca) ENTÃO
    print("  -> A terra está seca!")
    print("  4: Pegar o regador")
    print("  5: Colocar água na planta")
    print("  6: Falar 'Bom dia, planta!'")
else:
    # SENÃO (se a terra NÃO está seca)
    print("  -> A terra está úmida.")
    print("  8: Apenas verificar as folhas")
    print("  9: Falar 'Você já está bem!'")


print("11: Colocar o vaso no sol")
print("12: Guardar ferramentas")
print("--- FIM ---")
