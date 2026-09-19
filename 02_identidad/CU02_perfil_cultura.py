"""
CU02_perfil_cultura.py
Diagnostico de Cultura Organizacional con el Competing Values Framework (OCAI)
Caso: Municipalidad Provincial de Tacna (MPT)
Curso: SI-886 Planeamiento Estrategico de TI - Semana 05
Docente: Dr. Oscar Juan Jimenez Flores
Universidad Privada de Tacna
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("=" * 80)
    print("MUNICIPALIDAD PROVINCIAL DE TACNA - DIAGNOSTICO DE CULTURA (CVF / OCAI)")
    print("Programa de Procesamiento Estadistico y Control de Calidad")
    print("=" * 80)

    # 1. Cargar datos
    csv_path = os.path.join(os.path.dirname(__file__), "encuesta_cultura.csv")
    if not os.path.exists(csv_path):
        csv_path = "02_identidad/encuesta_cultura.csv"
    
    if not os.path.exists(csv_path):
        print(f"Error: No se encontro el archivo {csv_path}")
        sys.exit(1)
        
    df_raw = pd.read_csv(csv_path)
    total_encuestados = len(df_raw)
    print(f"\n[+] Total de instrumentos recolectados: {total_encuestados}")

    # 2. Control de Calidad Metodologico (Suma obligatoria = 100 puntos)
    control_calidad_reporte = []
    ids_validos = []

    print("\n--- EJECUTANDO CONTROL DE CALIDAD AUTOMATIZADO ---")
    for idx, row in df_raw.iterrows():
        resp_id = row['id_respondiente']
        area = row['area']
        es_valido = True
        errores_resp = []

        for d in range(1, 7):
            # Validar Actual
            cols_act = [f"d{d}_act_a", f"d{d}_act_b", f"d{d}_act_c", f"d{d}_act_d"]
            suma_act = sum(row[c] for c in cols_act)
            if suma_act != 100:
                es_valido = False
                errores_resp.append(f"Dim {d} Actual = {suma_act} pts (desviacion: {suma_act - 100:+d})")

            # Validar Deseado
            cols_des = [f"d{d}_des_a", f"d{d}_des_b", f"d{d}_des_c", f"d{d}_des_d"]
            suma_des = sum(row[c] for c in cols_des)
            if suma_des != 100:
                es_valido = False
                errores_resp.append(f"Dim {d} Deseado = {suma_des} pts (desviacion: {suma_des - 100:+d})")

        if es_valido:
            ids_validos.append(resp_id)
        else:
            msg = f"[RECHAZADO] Respondiente {resp_id} ({area}): " + "; ".join(errores_resp)
            control_calidad_reporte.append(msg)
            print(f"  X {msg}")

    df_valid = df_raw[df_raw['id_respondiente'].isin(ids_validos)].copy()
    validos_count = len(df_valid)
    descartados_count = total_encuestados - validos_count
    tasa_efectividad = (validos_count / total_encuestados) * 100

    print(f"\n[+] Resumen de Control de Calidad:")
    print(f"    - Muestra total recibida: {total_encuestados}")
    print(f"    - Respuestas validas admitidas: {validos_count} ({tasa_efectividad:.1f}%)")
    print(f"    - Respuestas inconsistentes excluidas: {descartados_count}")

    # Guardar reporte de control de calidad
    os.makedirs("docs/evidencias/S05/salidas", exist_ok=True)
    with open("docs/evidencias/S05/salidas/control_calidad.txt", "w", encoding="utf-8") as f:
        f.write("REPORTE DE CONTROL DE CALIDAD METODOLOGICO - MUNICIPALIDAD PROVINCIAL DE TACNA\n")
        f.write("Instrumento Competing Values Framework (OCAI)\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Muestra bruta procesada: {total_encuestados} servidores publicos\n")
        f.write(f"Muestra neta valida: {validos_count} servidores publicos\n")
        f.write(f"Instrumentos excluidos: {descartados_count}\n\n")
        f.write("Detalle de exclusiones por violacion de la regla de suma 100 puntos:\n")
        for rep in control_calidad_reporte:
            f.write(f" - {rep}\n")

    # 3. Calculo de Medias por Dimension y Global
    dimensiones_nombres = [
        "1. Caracteristicas dominantes",
        "2. Liderazgo institucional",
        "3. Gestion del personal",
        "4. Cohesion institucional",
        "5. Enfasis estrategico",
        "6. Criterio de exito"
    ]

    tipos_cultura = ["Clan (A)", "Adhocracia (B)", "Mercado (C)", "Jerarquia (D)"]
    codigos_q = ['a', 'b', 'c', 'd']

    resultados_dim = []

    for d_idx, d_nom in enumerate(dimensiones_nombres, start=1):
        fila = {"Dimension": d_nom}
        for q_idx, q in enumerate(codigos_q):
            media_act = df_valid[f"d{d_idx}_act_{q}"].mean()
            media_des = df_valid[f"d{d_idx}_des_{q}"].mean()
            brecha = media_des - media_act
            t_nombre = tipos_cultura[q_idx].split()[0]
            fila[f"{t_nombre}_Actual"] = round(media_act, 2)
            fila[f"{t_nombre}_Deseado"] = round(media_des, 2)
            fila[f"{t_nombre}_Brecha"] = round(brecha, 2)
        resultados_dim.append(fila)

    df_dim = pd.DataFrame(resultados_dim)

    # Medias Globales
    global_act = {
        "Clan": np.mean([df_valid[f"d{d}_act_a"].mean() for d in range(1, 7)]),
        "Adhocracia": np.mean([df_valid[f"d{d}_act_b"].mean() for d in range(1, 7)]),
        "Mercado": np.mean([df_valid[f"d{d}_act_c"].mean() for d in range(1, 7)]),
        "Jerarquia": np.mean([df_valid[f"d{d}_act_d"].mean() for d in range(1, 7)])
    }

    global_des = {
        "Clan": np.mean([df_valid[f"d{d}_des_a"].mean() for d in range(1, 7)]),
        "Adhocracia": np.mean([df_valid[f"d{d}_des_b"].mean() for d in range(1, 7)]),
        "Mercado": np.mean([df_valid[f"d{d}_des_c"].mean() for d in range(1, 7)]),
        "Jerarquia": np.mean([df_valid[f"d{d}_des_d"].mean() for d in range(1, 7)])
    }

    global_brecha = {k: global_des[k] - global_act[k] for k in global_act}

    # Fila resumen global para tabla
    fila_global = {
        "Dimension": "PROMEDIO GLOBAL MPT",
        "Clan_Actual": round(global_act["Clan"], 2),
        "Clan_Deseado": round(global_des["Clan"], 2),
        "Clan_Brecha": round(global_brecha["Clan"], 2),
        "Adhocracia_Actual": round(global_act["Adhocracia"], 2),
        "Adhocracia_Deseado": round(global_des["Adhocracia"], 2),
        "Adhocracia_Brecha": round(global_brecha["Adhocracia"], 2),
        "Mercado_Actual": round(global_act["Mercado"], 2),
        "Mercado_Deseado": round(global_des["Mercado"], 2),
        "Mercado_Brecha": round(global_brecha["Mercado"], 2),
        "Jerarquia_Actual": round(global_act["Jerarquia"], 2),
        "Jerarquia_Deseado": round(global_des["Jerarquia"], 2),
        "Jerarquia_Brecha": round(global_brecha["Jerarquia"], 2)
    }

    df_consolidado = pd.concat([df_dim, pd.DataFrame([fila_global])], ignore_index=True)
    df_consolidado.to_csv("02_identidad/CU02_perfil_cultura.csv", index=False, encoding="utf-8")
    print("\n[+] Guardado consolidado en 02_identidad/CU02_perfil_cultura.csv")

    # Identificar Cultura Dominante Actual y Deseada
    cultura_dom_act = max(global_act, key=global_act.get)
    puntaje_dom_act = global_act[cultura_dom_act]

    cultura_dom_des = max(global_des, key=global_des.get)
    puntaje_dom_des = global_des[cultura_dom_des]

    max_brecha_pos = max(global_brecha, key=global_brecha.get)
    max_brecha_neg = min(global_brecha, key=global_brecha.get)

    print("\n" + "=" * 80)
    print("RESULTADOS DEL PERFIL CULTURAL GLOBAL (MPT):")
    print("=" * 80)
    print(f"  * Cultura Dominante ACTUAL: {cultura_dom_act.upper()} ({puntaje_dom_act:.2f} pts)")
    print(f"  * Cultura Dominante DESEADA: {cultura_dom_des.upper()} ({puntaje_dom_des:.2f} pts)")
    print(f"  * Mayor Brecha POSITIVA (Apetito de transformacion): {max_brecha_pos.upper()} (+{global_brecha[max_brecha_pos]:.2f} pts)")
    print(f"  * Mayor Brecha NEGATIVA (Sobredimensionamiento burocratico): {max_brecha_neg.upper()} ({global_brecha[max_brecha_neg]:.2f} pts)")
    print("-" * 80)
    print("Puntajes Globales Consolidados:")
    for k in ["Clan", "Adhocracia", "Mercado", "Jerarquia"]:
        print(f"  - {k:<12}: Actual = {global_act[k]:5.2f} | Deseado = {global_des[k]:5.2f} | Brecha = {global_brecha[k]:+5.2f}")

    # 4. Analisis de Congruencia Cultural
    print("\n--- ANALISIS DE CONGRUENCIA CULTURAL ---")
    incongruencias = []
    for idx, row in df_dim.iterrows():
        dim = row["Dimension"]
        act_vals = {
            "Clan": row["Clan_Actual"],
            "Adhocracia": row["Adhocracia_Actual"],
            "Mercado": row["Mercado_Actual"],
            "Jerarquia": row["Jerarquia_Actual"]
        }
        dom_dim = max(act_vals, key=act_vals.get)
        congruente = (dom_dim == cultura_dom_act)
        if not congruente:
            incongruencias.append(f"{dim} dominada por {dom_dim} ({act_vals[dom_dim]} pts) != {cultura_dom_act}")
        print(f"  - {dim:<32}: Dominante = {dom_dim:<10} ({act_vals[dom_dim]:.2f} pts) -> {'CONGRUENTE' if congruente else 'DISCREPANTE'}")

    veredicto_congruencia = "ALTA CONGRUENCIA" if len(incongruencias) == 0 else f"CONGRUENCIA MODERADA ({len(incongruencias)} divergencias)"
    print(f"\nVeredicto de Congruencia: {veredicto_congruencia}")

    # 5. Analisis por Areas (Gerencias con >= 5 respondientes validos)
    print("\n--- ANALISIS POR AREAS FUNCIONALES (N >= 5) ---")
    areas_analisis = df_valid['area'].value_counts()
    areas_validas = areas_analisis[areas_analisis >= 5].index.tolist()

    reporte_areas = []
    for ar in areas_validas:
        sub_df = df_valid[df_valid['area'] == ar]
        sub_act = {
            "Clan": np.mean([sub_df[f"d{d}_act_a"].mean() for d in range(1, 7)]),
            "Adhocracia": np.mean([sub_df[f"d{d}_act_b"].mean() for d in range(1, 7)]),
            "Mercado": np.mean([sub_df[f"d{d}_act_c"].mean() for d in range(1, 7)]),
            "Jerarquia": np.mean([sub_df[f"d{d}_act_d"].mean() for d in range(1, 7)])
        }
        sub_des = {
            "Clan": np.mean([sub_df[f"d{d}_des_a"].mean() for d in range(1, 7)]),
            "Adhocracia": np.mean([sub_df[f"d{d}_des_b"].mean() for d in range(1, 7)]),
            "Mercado": np.mean([sub_df[f"d{d}_des_c"].mean() for d in range(1, 7)]),
            "Jerarquia": np.mean([sub_df[f"d{d}_des_d"].mean() for d in range(1, 7)])
        }
        sub_dom_act = max(sub_act, key=sub_act.get)
        sub_dom_des = max(sub_des, key=sub_des.get)
        sub_brecha_adh = sub_des["Adhocracia"] - sub_act["Adhocracia"]
        sub_brecha_jer = sub_des["Jerarquia"] - sub_act["Jerarquia"]

        res_ar = (
            f"Area: {ar} (n={len(sub_df)})\n"
            f"  Actual: Clan={sub_act['Clan']:.1f}, Adhoc={sub_act['Adhocracia']:.1f}, Merc={sub_act['Mercado']:.1f}, Jer={sub_act['Jerarquia']:.1f} (Dominante: {sub_dom_act})\n"
            f"  Deseado: Clan={sub_des['Clan']:.1f}, Adhoc={sub_des['Adhocracia']:.1f}, Merc={sub_des['Mercado']:.1f}, Jer={sub_des['Jerarquia']:.1f} (Dominante: {sub_dom_des})\n"
            f"  Brechas clave: Adhocracia = {sub_brecha_adh:+.1f} | Jerarquia = {sub_brecha_jer:+.1f}"
        )
        print(res_ar)
        reporte_areas.append(res_ar)

    # Guardar reporte de analisis de perfil
    with open("docs/evidencias/S05/salidas/analisis_perfil.txt", "w", encoding="utf-8") as f:
        f.write("ANALISIS DE PERFIL CULTURAL Y CONGRUENCIA - MUNICIPALIDAD PROVINCIAL DE TACNA\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Cultura Dominante ACTUAL: {cultura_dom_act} ({puntaje_dom_act:.2f} puntos)\n")
        f.write(f"Cultura Dominante DESEADA: {cultura_dom_des} ({puntaje_dom_des:.2f} puntos)\n")
        f.write(f"Brecha Adhocracia: {global_brecha['Adhocracia']:+.2f} puntos\n")
        f.write(f"Brecha Jerarquia: {global_brecha['Jerarquia']:+.2f} puntos\n\n")
        f.write(f"Veredicto de Congruencia: {veredicto_congruencia}\n\n")
        f.write("PERFILES POR AREA (N >= 5):\n")
        for ra in reporte_areas:
            f.write(ra + "\n\n")

    # 6. Generacion del Grafico de Radar (Competing Values Framework)
    generar_grafico_radar(global_act, global_des)
    print("\n[+] Grafico de radar guardado exitosamente en 02_identidad/CU_perfil_cultura.png y anexos/anexo_C_perfil_cultura.png")
    print("=" * 80)

def generar_grafico_radar(global_act, global_des):
    # Cuadrantes en orden tradicional CVF:
    # Arriba-Izq: Clan | Arriba-Der: Adhocracia | Abajo-Der: Mercado | Abajo-Izq: Jerarquia
    categorias = ['Clan (Colaborativa)', 'Adhocracia (Innovadora)', 'Mercado (Competitiva)', 'Jerarquia (Control)']
    claves = ['Clan', 'Adhocracia', 'Mercado', 'Jerarquia']
    
    valores_act = [global_act[k] for k in claves]
    valores_des = [global_des[k] for k in claves]
    
    # Cerrar el poligono
    valores_act += valores_act[:1]
    valores_des += valores_des[:1]
    
    N = len(categorias)
    angulos = [n / float(N) * 2 * np.pi for n in range(N)]
    angulos += angulos[:1]
    
    fig, ax = plt.subplots(figsize=(9, 8), subplot_kw=dict(polar=True))
    
    # Configuracion de orientacion y sentido
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    
    # Ejes por categoria
    plt.xticks(angulos[:-1], categorias, color='#1A2B4C', size=11, weight='bold')
    
    # Configurar escala radial
    ax.set_rlabel_position(45)
    plt.yticks([10, 20, 30, 40, 50], ["10", "20", "30", "40", "50 pts"], color="#555555", size=9)
    plt.ylim(0, 55)
    
    # Dibujar Perfil Actual
    ax.plot(angulos, valores_act, linewidth=2.5, linestyle='solid', color='#D9381E', label=f'Cultura ACTUAL (Dominante: Jerarquia {global_act["Jerarquia"]:.1f})')
    ax.fill(angulos, valores_act, color='#D9381E', alpha=0.25)
    
    # Dibujar Perfil Deseado
    ax.plot(angulos, valores_des, linewidth=2.5, linestyle='dashed', color='#1565C0', label=f'Cultura DESEADA 2030 (Dominante: Adhocracia {global_des["Adhocracia"]:.1f})')
    ax.fill(angulos, valores_des, color='#1565C0', alpha=0.20)
    
    # Marcar puntos
    for ang, val in zip(angulos[:-1], valores_act[:-1]):
        ax.plot(ang, val, 'o', color='#D9381E', markersize=6)
        ax.text(ang, val + 2.5, f"{val:.1f}", color='#900C3F', size=9, weight='bold', ha='center')

    for ang, val in zip(angulos[:-1], valores_des[:-1]):
        ax.plot(ang, val, 's', color='#1565C0', markersize=6)
        ax.text(ang, val - 3.5, f"{val:.1f}", color='#0D47A1', size=9, weight='bold', ha='center')

    plt.title("PERFIL DE CULTURA ORGANIZACIONAL (CVF / OCAI)\nMunicipalidad Provincial de Tacna - Diagnostico PETI", size=14, weight='bold', color='#0E1E38', pad=25)
    plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), frameon=True, facecolor='#F8FAFC', edgecolor='#CBD5E1', fontsize=10)
    
    plt.tight_layout()
    plt.savefig("02_identidad/CU_perfil_cultura.png", dpi=300, bbox_inches='tight')
    plt.savefig("anexos/anexo_C_perfil_cultura.png", dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    main()
