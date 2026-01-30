sm = int(input('Salario Mensal(ienes)'))

sa = sm * 12

# -----------------------------
# 1) Dedução do salário (tabela)
# -----------------------------
# SD = quanto será "isentado" no começo

if sa <= 1_900_000:
    sd = 650_000
elif sa <= 3_600_000:
    sd = int(sa*0.30+80_000)
elif sa <= 6_600_000:
    sd = int(sa*0.20+440_000)
elif sa <= 8_500_000:
    sd = int(sa*0.10+1_100_000)
else:
    sd = 1_950_000 # maximo

salario_deducionado = sa - sd

# -----------------------------
# 2) Previdência (simplificadsa
# prev= previdencia
# -----------------------------

Prev = int(sa*0.0915)
previdencia_deducionada = salario_deducionado - Prev

# -----------------------------
# 3) Saúde (simplificado)
# -----------------------------

Saude = int(sa*0.045)
saude_deducionada = previdencia_deducionada - Saude

# -----------------------------
# 4) Dedução básica (simplificado)
# -----------------------------
# Pra valores normais, é 480.000
# (essa tabela só muda depois de renda MUITO alta)

if sa<= 24_000_000:
    db = 480_000
elif sa <= 24_500_000:
    db = 320_000
elif sa <= 25_000_000:
    db = 160_000
else:
    db = 0

    # RT = RENDA TRIBUTAVEL

rt = saude_deducionada - db
if rt <= 0:
    rt = 0

# -----------------------------
# 5) Imposto anual pela tabela
# -----------------------------

if rt < 1_000:
    imposto=0
elif rt<=1_949_000:
    imposto = int(rt*0.05-0)
elif rt<= 3_299_000:
    imposto = int(rt*0.10-97_500)
elif rt<= 6_949_000:
    imposto = int(rt*0.20-427_500)
elif rt<= 8_999_000:
    imposto = int(rt*0.23-636_000)
elif rt<= 17_999_000:
    imposto = int(rt*0.33-1_536_000)
elif rt<= 39_999_000:
    imposto = int(rt*0.40-2_796_000)
else:
    imposto = int(rt*0.45-4_796_000)

if imposto < 0:
    imposto = 0
    # -----------------------------
    # Resultado (mostra tudo)
    # -----------------------------
print('\n ---- Resultado ----')
print('salario anual:', sa)
print('dedução fixa governamental:', sd)
print('salario após dedução:', salario_deducionado)

print('previdencia (valor):', Prev)
print('salario após previdencia:', previdencia_deducionada)

print('saude (valor):', Saude)
print('salario após saude:', saude_deducionada)

print('dedução basica:', db)
print('renda tributavel:', rt)
print('imposto anual:', imposto)