# ANEXO E: SECCIONES 2.3 Y 2.4 DEL PETI
## Municipalidad Provincial de Tacna

---

# Sección 2.3 · Valores Institucionales y Tecnológicos
## Municipalidad Provincial de Tacna (MPT)

**Documento:** `2.3_valores.md`  
**Instrumentos Base:** Ley N° 27815 (Código de Ética de la Función Pública), PEI 2025-2030, RISST 2024 y Diagnóstico CVF/OCAI.  
**Premisa Operativa:** Un valor que no define conductas observables ni establece renuncias concretas no orienta ninguna decisión. Los valores de la MPT se formulan como compromisos de acción verificables y exigibles.

---

## 2.3 Valores

### 2.3.1 Valores de la Organización (Formulación Conductual)

| # | Valor (Enunciado Conductual) | Conducta que lo Cumple | Conducta que lo Viola | Consecuencia del Incumplimiento | ¿A qué se Renuncia al Sostenerlo? |
|---|---|---|---|---|---|
| **V1** | **Integridad y Probidad en el Servicio Público**<br>Actuamos con honestidad irreprochable, priorizando el interés colectivo tacneño y resguardando los recursos municipales con total transparencia. | Registrar cada transacción, expediente y acto administrativo de forma trazable en los sistemas informáticos institucionales, reportando anomalías de inmediato. | Alterar registros, eliminar trazas de auditoría (logs), favorecer a particulares en trámites o utilizar bienes tecnológicos ediles con fines personales. | Apertura de Procedimiento Administrativo Disciplinario (PAD) sancionador, inhabilitación de la función pública y denuncia penal ante la Fiscalía. | Se renuncia a la discrecionalidad informal, al "favor político" y a la opacidad en la toma de decisiones. |
| **V2** | **Vocación de Servicio y Empatía Ciudadana**<br>Diseñamos y entregamos servicios orientados a resolver las necesidades reales del vecino tacneño con calidez, celeridad y accesibilidad. | Resolver los requerimientos del administrado dentro del plazo legal, promoviendo canales digitales accesibles e informando en lenguaje claro. | Maltratar al usuario, postergar expedientes intencionalmente (inercia burocrática) o exigir requisitos no contemplados en el TUPA institucional. | Amonestación escrita en legajo personal, remoción del puesto de atención al público y descuento salarial por mora injustificada. | Se renuncia a la comodidad del horario estricto en ventanilla y a la desidia del "vuelva mañana". |
| **V3** | **Innovación Abierta y Mejora Continua**<br>Cuestionamos activamente la inercia del trámite en papel, adoptando metodologías ágiles y tecnologías seguras para simplificar la gestión. | Proponer mejoras en los flujos de trabajo, capacitarse en plataformas digitales y adoptar la firma digital eliminando copias físicas redundantes. | Resistirse al uso del sistema digital, exigir expedientes paralelos impresos "por si acaso" o boicotear nuevas herramientas informáticas. | Reasignación de funciones operativas, exclusión de incentivos de productividad institucional y evaluación de desempeño negativa. | Se renuncia a la "zona de confort" de los métodos tradicionales y a la falsa seguridad del sello de tinta. |
| **V4** | **Transparencia Activa y Responsabilidad por los Datos**<br>Reconocemos que la información pública pertenece a la ciudadanía y a la institución, no a quien la custodia temporalmente. | Publicar y compartir datos institucionales abiertos, interoperar sistemas con otras gerencias y mantener actualizadas las bases de datos públicas. | Ocultar información, negar el acceso a bases de datos a otras áreas de la municipalidad ("feudos de información") o cobrar por copias indebidas. | Sanción de suspensión temporal sin goce de haber según la Ley de Transparencia y Ley 27815 del Código de Ética. | Se renuncia al poder personal derivado de la retención exclusiva de información ("la información es poder"). |
| **V5** | **Colaboración Interdisciplinaria y Respeto Mutuo**<br>Trabajamos como un solo equipo municipal integrado, superando barreras jerárquicas para cumplir los objetivos del PEI. | Participar activamente en mesas técnicas transversales, brindar soporte oportuno a otras gerencias y compartir aprendizajes técnicos. | Culpar a otras áreas por demoras en los proyectos, trabajar de espaldas a los objetivos institucionales o desacreditar aportes técnicos de colegas. | Llamada de atención formal del Comité de Ética y compromiso vinculante de mediación con Recursos Humanos. | Se renuncia al aislamiento departamental ("esto no es de mi gerencia") y a las disputas de protagonismo. |

---

### 2.3.2 Valores Aplicados a las Decisiones Tecnológicas

| # | Tensión Tecnológica Real en la MPT | Valor que la Resuelve | Criterio de Decisión Derivado (Política Vinculante del PETI) |
|---|---|---|---|
| **T1** | **Disponibilidad Inmediata vs Seguridad Estricta:**<br>Las gerencias demandan instalar software comercial sin controles para agilizar trámites urgentes, arriesgando la seguridad informática. | **Integridad y Probidad (V1)** | *Ninguna aplicación, base de datos o dispositivo se conecta a la red municipal sin certificación previa de seguridad y política de privilegios mínimos de OGTIC, sin importar la jerarquía de quien lo solicite.* |
| **T2** | **Desarrollo Propietario Aislado vs Arquitectura Interoperable:**<br>Gestión Tributaria desea contratar un sistema cerrado propio mientras Desarrollo Urbano licita otro sistema geográfico independiente. | **Transparencia y Responsabilidad por los Datos (V4)** | *Todo sistema de software nuevo o modernizado debe fundamentarse en estándares abiertos de interoperabilidad (PIDE / APIs REST) y base de datos relacional compartida; se prohíbe la adquisición de sistemas cerrados que impidan la integración.* |
| **T3** | **Cultura de Sanción Punitiva vs Reporte Temprano de Fallas:**<br>Los operadores ocultan incidentes de ciberseguridad o caídas del sistema por temor a procesos administrativos de OCI. | **Innovación y Mejora Continua (V3)** | *Se implanta una política institucional de "Reporte Libre de Culpa" (Blameless Post-Mortem); todo incidente de TI reportado en menos de 60 minutos se trata como oportunidad de mejora técnica, blindando al operador de sanciones disciplinarias salvo dolo comprobado.* |
| **T4** | **Reemplazo Masivo de Hardware vs Reingeniería de Procesos:**<br>Presión sindical y de gerencias por comprar cientos de computadoras nuevas (AEI.07.04) manteniendo los mismos flujos lentos en papel. | **Vocación de Servicio y Empatía Ciudadana (V2)** | *La renovación de equipamiento informático queda estrictamente condicionada a la previa digitalización, simplificación y adopción del flujo cero papel en la gerencia solicitante.* |

---

### 2.3.3 Trazabilidad de los Valores Institucionales

La formulación de esta escala de valores responde a una rigurosa trazabilidad entre las normas de origen, los valores declarados en el PEI y las evidencias empíricas levantadas en el diagnóstico cultural:

```mermaid
flowchart LR
    A["<b>Fuentes Normativas</b><br/>Ley 27815 (Código Ética)<br/>PEI 2025-2030 (OEI.05)<br/>RISST 2024"] --> D["<b>Matriz de Valores PETI</b>"]
    B["<b>Diagnóstico CVF (OCAI)</b><br/>Jerarquía actual: 44.1 pts<br/>Brecha Adhocracia: +21.5 pts"] --> D
    C["<b>Supuestos Básicos</b><br/>Silos de datos<br/>Temor a OCI<br/>Firma en papel"] --> D
    D --> E["<b>V1</b> Integridad y Probidad<br/><b>V2</b> Vocación de Servicio<br/><b>V3</b> Innovación Abierta<br/><b>V4</b> Transparencia de Datos<br/><b>V5</b> Colaboración"]
    classDef box fill:#EEF4FB,stroke:#1A365D,stroke-width:1.5px,color:#0F2942;
    class A,B,C,D,E box;
```

1. **Valores Conservados y Fortalecidos:**
   - *Integridad y Probidad:* Proviene del Art. 6 de la Ley N° 27815. Se conserva integralmente pero se operacionaliza en el entorno digital mediante la obligatoriedad del no repudio y trazabilidad en logs.
2. **Valores Reformulados:**
   - *Vocación de Servicio:* Proveniente de la Misión del PEI 2025-2030. Se reformula desde una declaración genérica hacia la eliminación de barreras burocráticas y respeto al tiempo del ciudadano mediante canales virtuales.
   - *Transparencia Activa:* Proveniente del deber de Transparencia de la Ley 27815. Se reconvierte en "Responsabilidad por los Datos" para desarticular el supuesto arraigado de "los datos son propiedad de mi gerencia".
3. **Valores Nuevos Incorporados por el Diagnóstico:**
   - *Innovación Abierta y Mejora Continua:* Surge directamente de la brecha de +21.52 puntos en Adhocracia y la necesidad de erradicar el supuesto "si funciona hoy, no se toca para evitar a la Contraloría".
   - *Colaboración Interdisciplinaria:* Nace para cerrar la divergencia cultural detectada entre áreas administrativas (Jerarquía) y operativas (Mercado), promoviendo equipos ágiles multidisciplinarios.


---

# Sección 2.4 · Diagnóstico de Cultura Organizacional
## Municipalidad Provincial de Tacna (MPT)

**Documento:** `2.4_cultura.md`  
**Metodología:** Competing Values Framework (CVF) / Organizational Culture Assessment Instrument (OCAI) — Cameron & Quinn.  
**Vinculación Estratégica:** Plan Estratégico Institucional (PEI 2025-2030) · OEI.07 Fortalecer el Gobierno Digital.

---

## 2.4 Diagnóstico de Cultura Organizacional

### 2.4.1 Metodología

El diagnóstico cultural de la Municipalidad Provincial de Tacna se llevó a cabo aplicando el **Organizational Culture Assessment Instrument (OCAI)** fundamentado en el marco de valores en competencia de Cameron y Quinn (2011).

#### A. Instrumento y Regla de Suma Forzada
El cuestionario evalúa **seis dimensiones nucleares**:
1. Características dominantes de la organización
2. Estilo de liderazgo directivo
3. Gestión del personal y ambiente de trabajo
4. Cohesión institucional (lo que mantiene unida a la institución)
5. Énfasis estratégico corporativo
6. Criterios de éxito institucional

En cada dimensión, el respondiente distribuye obligatoriamente **100 puntos** entre cuatro alternativas que tipifican los cuadrantes culturales:
- **A — Clan:** Enfoque interno, flexibilidad, trabajo en equipo, mentoría y desarrollo del talento.
- **B — Adhocracia:** Enfoque externo, flexibilidad, innovación, emprendimiento y adaptabilidad.
- **C — Mercado:** Enfoque externo, estabilidad y control, orientación a resultados y competitividad.
- **D — Jerarquía:** Enfoque interno, estabilidad y control, formalización procedimental y cumplimiento de normas.

La distribución se evalúa de manera bicrónica: **Estado ACTUAL** (cómo percibe el servidor a la municipalidad hoy) y **Estado DESEADO a 5 años** (cómo debería ser al 2030 para cumplir los objetivos de modernización del PEI).

#### B. Población, Muestra y Control de Calidad
- **Población objetivo:** Servidores de los diversos regímenes laborales (D.L. 276 Nombrados, D.L. 728, Contratados CAS y locadores de servicios) adscritos a órganos de alta dirección, asesoramiento, apoyo y de línea de la sede central de la MPT.
- **Muestra recolectada:** $N = 35$ instrumentos completados.
- **Control de calidad automatizado:** El script estadístico (`CU02_perfil_cultura.py`) verificó la restricción matemática estricta $\sum(A+B+C+D) = 100$ en cada dimensión y momento.
  - **Respuestas conformes admitidas:** 32 instrumentos (91.43% de efectividad).
  - **Respuestas inconsistentes rechazadas:** 3 instrumentos (R015 de OGAF con 110 pts en Dim 2; R024 de OGACGD con 90 pts en Dim 5; R031 de GTPSC con 105 pts en Dim 1).
- **Representatividad multi-área:** La muestra incluye 5 gerencias y oficinas con $n \ge 5$ respondientes válidos, garantizando una perspectiva transversal de la corporación edil y no sesgada únicamente al personal informático.

#### C. Limitaciones del Diagnóstico
1. *Muestreo no probabilístico por conveniencia:* Si bien cubre las áreas críticas para el PETI, áreas operativas descentralizadas (como maestranza o áreas verdes) tuvieron menor acceso a la encuesta.
2. *Sesgo de deseabilidad social:* Servidores bajo régimen transitorio (CAS) podrían moderar sus respuestas críticas por temor a represalias, a pesar de haberse garantizado el anonimato bajo la Ley N° 29733.

---

### 2.4.2 Perfil de Cultura Actual y Deseada

El procesamiento estadístico sobre los 32 instrumentos válidos arrojó los siguientes puntajes consolidados por dimensión y globales:

#### Tabla 2.4.1 · Consolidado de Puntajes CVF y Brechas Netas (MPT)
| Dimensión Evaluada | Clan (A) Act | Clan (A) Des | Brecha Clan | Adhoc (B) Act | Adhoc (B) Des | Brecha Adhoc | Merc (C) Act | Merc (C) Des | Brecha Merc | Jerarq (D) Act | Jerarq (D) Des | Brecha Jerarq |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1. Características dominantes | 18.00 | 29.12 | +11.12 | 12.28 | 34.31 | +22.03 | 26.25 | 18.06 | -8.19 | **43.47** | 18.50 | -24.97 |
| 2. Liderazgo institucional | 17.47 | 28.72 | +11.25 | 12.31 | 33.47 | +21.16 | 26.22 | 17.59 | -8.62 | **44.00** | 20.22 | -23.78 |
| 3. Gestión del personal | 16.91 | 28.69 | +11.78 | 12.53 | 34.25 | +21.72 | 25.88 | 18.41 | -7.47 | **44.69** | 18.66 | -26.03 |
| 4. Cohesión institucional | 17.38 | 29.16 | +11.78 | 12.88 | 34.47 | +21.59 | 25.22 | 18.16 | -7.06 | **44.53** | 18.22 | -26.31 |
| 5. Énfasis estratégico | 18.03 | 27.75 | +9.72 | 12.75 | 34.38 | +21.62 | 25.84 | 18.03 | -7.81 | **43.38** | 19.84 | -23.53 |
| 6. Criterio de éxito | 17.56 | 28.75 | +11.19 | 13.00 | 33.97 | +20.97 | 24.91 | 18.47 | -6.44 | **44.53** | 18.81 | -25.72 |
| **PROMEDIO GLOBAL MPT** | **17.56** | **28.70** | **+11.14** | **12.62** | **34.14** | **+21.52** | **25.72** | **18.12** | **-7.60** | **44.10** | **19.04** | **-25.06** |

#### Diagnóstico del Radar Cultural
![Radar de Cultura MPT](file:///c:/Users/PC/Desktop/PETI/05/02_identidad/CU_perfil_cultura.png)

* **Cultura Dominante ACTUAL: JERARQUÍA (44.10 puntos).** La Municipalidad Provincial de Tacna opera bajo un esquema clásico burocrático-legalista donde el procedimiento, la directiva formal y el blindaje ante el Órgano de Control Institucional (OCI) gobiernan la toma de decisiones cotidianas.
* **Cultura Dominante DESEADA (2030): ADHOCRACIA (34.14 puntos).** Los servidores demandan una transición drástica hacia un modelo dinámico, innovador y ágil, secundado por un fuerte incremento en la cultura **Clan (28.70 puntos)**.
* **Dimensión de Mayor Brecha Positiva: ADHOCRACIA (+21.52 puntos).** Evidencia un apetito reprimido de modernización tecnológica y frustración con la lentitud del trámite manual.
* **Dimensión de Mayor Brecha Negativa: JERARQUÍA (-25.06 puntos).** Los servidores perciben la sobredimensión de controles como un factor paralizante que frena la atención de calidad al ciudadano tacneño.

---

### 2.4.3 Congruencia Cultural

#### A. Congruencia entre Dimensiones (Veredicto: ALTA CONGRUENCIA)
El análisis dimensional demuestra una **alineación estructural homogénea**: en las 6 dimensiones evaluadas, la cultura Jerarquía ocupa sin excepción el primer lugar con puntajes casi idénticos (entre 43.38 y 44.69 puntos), y la cultura Adhocracia ocupa invariablemente el último lugar (entre 12.28 y 13.00 puntos). No existen contradicciones aisladas entre liderazgo y criterios de éxito; la formalidad burocrática impregna transversalmente todas las facetas institucionales.

#### B. Congruencia Interdepartamental y Divergencias Internas
Al desagregar los perfiles por áreas con representatividad ($n \ge 5$), se evidencian marcadas divergencias que condicionan la estrategia del PETI:

```mermaid
quadrantChart
    title Perfil Cultural Actual por Áreas Funcionales (MPT)
    x-axis Enfoque Interno --> Enfoque Externo
    y-axis Estabilidad / Control --> Flexibilidad / Agilidad
    quadrant-1 Adhocracia (Innovación)
    quadrant-2 Clan (Colaboración)
    quadrant-3 Jerarquía (Control Normativo)
    quadrant-4 Mercado (Competitividad / Resultados)
    "OGTIC (TI)": [0.25, 0.35]
    "OGAF (Administración)": [0.22, 0.20]
    "GGT (Tributaria)": [0.72, 0.22]
    "GTPSC (Seguridad)": [0.65, 0.28]
    "OGACGD (Atención Vecino)": [0.38, 0.30]
```

1. **Oficina General de Tecnologías de la Información y Comunicación (OGTIC - n=6):**
   - *Actual:* Jerarquía (49.5 pts), Adhocracia (18.4 pts), Clan (17.6 pts), Mercado (14.5 pts).
   - *Deseado:* Adhocracia (47.9 pts), Clan (27.2 pts), Jerarquía (14.7 pts), Mercado (10.2 pts).
   - *Brecha:* **+29.6 en Adhocracia** y **-34.9 en Jerarquía**. Es el área que experimenta con mayor intensidad la asfixia del trámite en papel y busca una transformación digital radical.
2. **Gerencia de Gestión Tributaria (GGT - n=7):**
   - *Actual:* Jerarquía (39.5 pts), **Mercado (34.9 pts)**, Clan (15.2 pts), Adhocracia (10.4 pts).
   - *Deseado:* Adhocracia (27.7 pts), Mercado (26.1 pts), Clan (26.1 pts), Jerarquía (20.1 pts).
   - *Análisis:* Presenta el puntaje más alto de Mercado de la MPT, guiada por metas coactivas de recaudación y metas del MEF. Requiere que los proyectos de TI se justifiquen en ingresos y no solo en "innovación".
3. **Oficina General de Administración y Finanzas (OGAF - n=6):**
   - *Actual:* Jerarquía (48.5 pts), Mercado (22.9 pts), Clan (18.4 pts), Adhocracia (10.2 pts).
   - *Deseado:* Clan (30.1 pts), Adhocracia (27.5 pts), Jerarquía (24.2 pts), Mercado (18.2 pts).
   - *Análisis:* Es el bastión del control normativo (Abastecimiento, Contabilidad y Tesorería). Aunque desean simplificar, conservan el puntaje de Jerarquía deseada más alto de la municipalidad (24.2 pts), pues asumen la responsabilidad directa ante OCI y Contraloría.
4. **Oficina General de Atención al Ciudadano y Gestión Documentaria (OGACGD - n=5):**
   - *Deseado:* Adhocracia (38.4 pts) y Clan (32.6 pts). Fuerte vocación por erradicar las colas físicas en el palacio municipal mediante expedientes virtuales accesibles.

---

### 2.4.4 Supuestos Básicos Identificados

A partir del análisis de artefactos institucionales (ROF 2022, RISST 2024 de 51 páginas, PEI 2025-2030 y Código de Ética), se inferieron los siguientes supuestos profundos que gobiernan la conducta real:

#### Tabla 2.4.2 · Matriz de Desalineación Cultural (Valores Adoptados vs Supuestos Básicos)
| # | Artefacto o Hecho Observado | Fuente Documental | Valor Adoptado Declarado | Supuesto Básico Subyacente Inferido | ¿Coinciden? |
|---|---|---|---|---|:---:|
| 1 | Trámite de compras de TI exige entre 4 y 7 firmas y sellos físicos correlativos en papel. | ROF 2022 y RISST 2024 | Modernización institucional y celeridad (PEI OEI.05) | *«La firma física en papel con sello de tinta es la única garantía real de no responsabilidad penal o civil ante el OCI».* | **NO** |
| 2 | Sistema de recaudación tributaria y catastro urbano no interoperan; el vecino traslada copias físicas entre oficinas contiguas. | PEI 2025-2030 (OEI.02 / OEI.07) | Vocación de servicio y trabajo en equipo | *«La base de datos es coto de poder y patrimonio de la gerencia, no un activo corporativo».* | **NO** |
| 3 | Servidores de producción operan en entornos legados obsoletos sin mantenimiento preventivo formal. | PEI 2025-2030 (AEI.07.03) | Innovación y excelencia operativa | *«Si el sistema funciona hoy, no se actualiza ni se modifica; innovar expone al funcionario a observaciones de auditoría».* | **NO** |
| 4 | El RISST 2024 detalla minuciosamente sanciones disciplinarias; los registros de incidentes de seguridad permanecen en blanco. | RISST 2024 (Capítulo de Sanciones) | Cuidado del trabajador y mejora continua | *«Reportar una falla técnica, incidente o error acarrea investigación disciplinaria y castigo individual».* | **NO** |
| 5 | OGTIC es convocada únicamente para cotizar computadoras e impresoras, no para rediseñar procesos. | Organigrama ROF 2022 | Liderazgo en Gobierno Digital (PEI OEI.07) | *«TI es una unidad de gasto operativo y soporte técnico de mantenimiento de PCs, no un socio estratégico de gestión».* | **NO** |
| 6 | Sesiones de Concejo Municipal y audiencias se transmiten en vivo y se asientan en actas públicas foliadas. | ROF 2022 y Ley 27972 | Transparencia, legalidad y orden institucional | *«Los actos de gobierno municipal deben ser públicos, trazables y formalizados conforme a la ley».* | **SÍ** |

---

### 2.4.5 Implicancias para la Implantación del PETI

El diagnóstico evidencia una verdad categórica: **un PETI que diseñe proyectos tecnológicos asumiendo una organización ágil y colaborativa está condenado al fracaso si no desarma previamente la cultura de Jerarquía y el temor al control.**

Las implicancias del diagnóstico determinan dos elementos directrices del plan:

1. **Condicionamiento de la Hoja de Ruta (Sección 7.3):**
   - *Prioridad Cero:* Antes de licitar o desplegar el Sistema de Gestión Documentaria o el Catastro Interoperable, la Alta Dirección debe promulgar las Directivas de Firma Digital con pleno valor probatorio legal (acreditadas por INDECOPI y RENIEC) para brindar inmunidad legal a los funcionarios que dejen el papel.
   - *Gobernanza del Dato Previa:* Designación de directores como "Custodios de Información", venciendo el supuesto de feudalismo de bases de datos antes de la integración técnica de la Plataforma de Interoperabilidad.
2. **Matriz de Comunicaciones y Despliegue Segmentado (Sección 10):**
   - Para **OGAF**, el plan debe presentarse en términos de *cumplimiento de estándares de Contraloría, seguridad jurídica y trazabilidad de auditoría*.
   - Para **GGT**, el plan debe presentarse como *un acelerador de cobranza, reducción de morosidad y cumplimiento de metas del MEF*.
   - Para **OGTIC**, el plan debe dotarle de *empoderamiento formal y presupuesto autónomo para la automatización (AEI.07.02) y no meramente compra de fierros (AEI.07.04)*.
