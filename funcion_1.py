def analizar_riesgo(vulnerabilidades):
    if vulnerabilidades == 0:
        return "SEGURO 🟢"
    elif vulnerabilidades < 5:
        return "RIESGO MEDIO 🟡"
    else:
        return "RIESGO CRÍTICO 🔴"

