import sys

UIT_2026 = 5500.0

# FUNCIONES

def sueldo_bruto_grati(sueldo,mes_ingreso):
    sueldo_bruto = sueldo * ((12 - mes_ingreso) + 1)
    # Le agregamos lo que corresponde a las gratificaciones de Julio y Diciembre
    if mes_ingreso > 6:
        sueldo_bruto_anual = sueldo_bruto + sueldo
    else:
        sueldo_bruto_anual = sueldo_bruto + 2*sueldo
    return sueldo_bruto_anual


def tasa_impuesto(s_neto):
    imp_anual = 0.0
    if s_neto <= 5*UIT_2026:
        imp_anual = s_neto*0.08
        return imp_anual
    elif 5*UIT_2026 < s_neto <= 20*UIT_2026:
        imp_anual = 5 * UIT_2026 * 0.08
        imp_anual = imp_anual + ((s_neto -(5*UIT_2026)) * 0.14)
        return imp_anual
    elif 20*UIT_2026 < s_neto <= 35*UIT_2026:
        imp_anual = 5*UIT_2026 * 0.08
        imp_anual = imp_anual + (20*UIT_2026-5*UIT_2026)*0.14
        imp_anual = imp_anual + ((s_neto-(20*UIT_2026))*0.17)
        return imp_anual
    elif 35*UIT_2026 < s_neto <= 45*UIT_2026:
        imp_anual = 5*UIT_2026 * 0.08
        imp_anual = imp_anual + (20*UIT_2026-5*UIT_2026)*0.14
        imp_anual = imp_anual + (35*UIT_2026-20*UIT_2026)*0.17
        imp_anual = imp_anual + ((s_neto-(35*UIT_2026))*0.20)
        return imp_anual
    elif s_neto > 45*UIT_2026:
        imp_anual = 5*UIT_2026 * 0.08
        imp_anual = imp_anual + (20*UIT_2026-5*UIT_2026)*0.14
        imp_anual = imp_anual + (35*UIT_2026-20*UIT_2026)*0.17
        imp_anual = imp_anual + (45*UIT_2026-35*UIT_2026)*0.20
        imp_anual = imp_anual + ((s_neto-(45*UIT_2026))*0.30)
        return imp_anual
    
def calculo_retencion_mensual(inicio,imp_anual):
    reten = []
    for i in range(12):
        no_retencion = 0
        reten.append(no_retencion)

    for i in range(inicio-1,12):
        if 0 <= i < 3:
            reten[i] = imp_anual/12
        elif 3 <= i < 4:
            new_imp = imp_anual- sum(reten[0:3])
            reten[i] = new_imp/9
        elif 4 <= i < 7:
            new_imp = imp_anual - sum(reten[0:4])
            reten[i] = new_imp/8
        elif 7 <= i < 8:
            new_imp = imp_anual - sum(reten[0:7])
            reten[i] = new_imp/5
        elif 8 <= i < 11:
            new_imp = imp_anual - sum(reten[0:8])
            reten[i] = new_imp/4
        elif i == 11:
            reten[i] = imp_anual - sum(reten[0:11])
    return reten


def retencion_adicional_mes(monto_adic,rem_neta,i_anual_p):
    adicional = monto_adic + rem_neta
    adicional = tasa_impuesto(adicional)
    adicional = adicional - i_anual_p
    return adicional

def imprimir_retenciones(meses_reten):
    print("Enero: S/." + str(round(meses_reten[0],1)))
    print("Febrero: S/." + str(round(meses_reten[1],1)))
    print("Marzo: S/." + str(round(meses_reten[2],1)))
    print("Abril: S/." + str(round(meses_reten[3],1)))
    print("Mayo: S/." + str(round(meses_reten[4],1)))
    print("Junio: S/." + str(round(meses_reten[5],1)))
    print("Julio: S/." + str(round(meses_reten[6],1)))
    print("Agosto: S/." + str(round(meses_reten[7],1)))
    print("Setiembre: S/." + str(round(meses_reten[8],1)))
    print("Octubre: S/." + str(round(meses_reten[9],1)))
    print("Noviembre: S/." + str(round(meses_reten[10],1)))
    print("Diciembre: S/." + str(round(meses_reten[11],1)))
    return

# VARIABLES A UTILIZAR
sueldo_nuevo = 0.00
mes_au = 0

#CALCULO DE LA RETENCION DE QUINTA CATEGORÍA 

print("------------------------------")
print("RETENCIÓN DE QUINTA CATEGORÍA")
print("------------------------------")

retencion_mensual = []
nombre = input("Ingrese su nombre: ")
print("")
print(nombre + ", responda las siguientes preguntas para realizar el cálculo de la retención de su sueldo que le corresponde")
print("")
sueldo_mes = float(input("Ingresa tu sueldo mensual(s/.): "))
print("")
# Validacion
if sueldo_mes < 0:
    sys.exit("Tu sueldo no puede ser negativo") 
# -----------------------------------------
mes_ingreso = int(input("¿En qué mes ingresó a trabajar? (1 -> Enero al 12 -> Diciembre): "))
print("")

# Asignacion Familiar
AF = int(input("¿Te corresponde Asignación Familiar?(1.SI   2.NO): "))
print("")
asig_familiar = 113.0 if AF == 1 else 0.0
sueldo_mes = sueldo_mes + asig_familiar

remunera_bruta = sueldo_bruto_grati(sueldo_mes,mes_ingreso)

# Bonificaciones / Pagos extraordinarios / Comisión / Horas extras

# Vector para guardar ingresos variables por mes
# (índice 0 = enero, ..., 11 = diciembre)
ingresos_variables = [0.0] * 12

print("------------------------------------------------------------------")
print("INGRESOS VARIABLES (bonificaciones, comisiones, horas extras, etc.)")
print("------------------------------------------------------------------")

tiene_ingreso = int(input("¿Ha recibido algún ingreso variable? (1.SI   2.NO): "))
print("")

while tiene_ingreso == 1:
    print("Tipo de ingreso:")
    print("1. Bonificación")
    print("2. Pago extraordinario")
    print("3. Comisión")
    print("4. Horas extras")
    
    tipo = int(input("Seleccione una opción: "))
    
    mes = int(input("¿En qué mes lo recibió? (1 -> Enero al 12 -> Diciembre): "))
    monto = float(input("¿Qué monto recibió? (s/.): "))

    # Validaciones
    if not (1 <= mes <= 12):
        print("Mes inválido. Intente nuevamente.")
    elif monto < 0:
        print("El monto no puede ser negativo.")
    elif tipo not in [1, 2, 3, 4]:
        print("Tipo de ingreso inválido.")
    else:
        # Acumulamos en el mes correspondiente
        ingresos_variables[mes - 1] += monto

        # (Opcional por ahora) sumar al total anual
        remunera_bruta += monto

    print("")
    tiene_ingreso = int(input("¿Ha recibido otro ingreso variable? (1.SI   2.NO): "))
    print("")

# ==============================
# UTILIDADES
# ==============================

# Vector para utilidades por mes 
utilidades_por_mes = [0.0] * 12

print("-----------")
print("UTILIDADES")
print("-----------")

recibio_utilidades = int(input("¿Recibió utilidades durante el año? (1.SI   2.NO): "))
print("")

if recibio_utilidades == 1:
    mes_utilidades = int(input("¿En qué mes las recibió? (1 -> Enero al 12 -> Diciembre): "))
    monto_utilidades = float(input("¿Qué monto recibió por utilidades? (s/.): "))

    # Validaciones
    if not (1 <= mes_utilidades <= 12):
        print("Mes inválido. No se registrarán las utilidades.")
    elif monto_utilidades < 0:
        print("El monto no puede ser negativo.")
    else:
        utilidades_por_mes[mes_utilidades - 1] += monto_utilidades

        # (Nivel actual) sumar al total anual
        remunera_bruta += monto_utilidades

print("")

# ==============================
# VALIDACIÓN DE RETENCIÓN
# ==============================

remunera_neta = remunera_bruta - (7 * UIT_2026)

if remunera_neta <= 0:
    print("No le corresponde retención de quinta categoría.")
else:
    imp_anual_proyectado = tasa_impuesto(remunera_neta)

    # ------------------------------
    # PASO 4: Retención mensual proyectada
    # ------------------------------

    # Calculamos retención mensual según mes de ingreso
    retenciones_mensuales = calculo_retencion_mensual(mes_ingreso, imp_anual_proyectado)

    # ------------------------------
    # PASO 5: Ajustes por ingresos adicionales y utilidades
    # ------------------------------

    for mes in range(12):
        monto_adic = ingresos_variables[mes] + utilidades_por_mes[mes]
        
        if monto_adic > 0:
            # Calculamos retención adicional solo por ese mes
            adicional_mes = retencion_adicional_mes(monto_adic, remunera_neta, imp_anual_proyectado)
            
            # Sumamos al mes correspondiente
            retenciones_mensuales[mes] += adicional_mes

    print("Tu impuesto anual proyectado es: S/." + str(round(imp_anual_proyectado,2)))
    print("")
    print("La retención que te corresponde por cada mes es la siguiente.")
    print("")
    imprimir_retenciones(retenciones_mensuales)


