# Implicancias del Diagnóstico Cultural para la Implantación del PETI
## Municipalidad Provincial de Tacna (MPT)

**Código del Documento:** `CU04_implicancias_peti.md`  
**Articulación Estratégica:** PEI 2025-2030 (OEI.07 Fortalecer el Gobierno Digital / AEI.07.01 - AEI.07.04)  
**Finalidad:** Traducir los hallazgos del Competing Values Framework (CVF) y los supuestos básicos identificados en estrategias operativas y salvaguardas que garanticen la viabilidad de los proyectos tecnológicos del PETI.

---

## 1. Matriz de Implicancias y Estrategias de Implantación

| # | Hallazgo Cultural Identificado | Riesgo Concreto para el PETI | Estrategia de Implantación Adoptada | Sección del PETI donde se Materializa |
|---|---|---|---|---|
| **1** | **Cultura dominante actual en JERARQUÍA (44.10 pts)**<br>Excesivo formalismo procedimental, cultura del memo en papel y temor a responsabilidades ante el OCI. | Resistencia a la adopción del **Sistema de Gestión Documental y Expediente Digital (SGD)**; los funcionarios exigirán duplicar expedientes en físico con sellos manuales. | **Formalización normativa previa y blindaje legal:** Cada hito del SGD debe contar con Directiva Municipal aprobada por Resolución de Gerencia Municipal (RGM) y Decreto de Alcaldía con valor probatorio legal (Firma Digital RENIEC). | **Sección 7:** Portafolio de Proyectos (Proyecto SGD-01)<br>**Sección 10:** Marco de Gobernanza y Gestión del Cambio |
| **2** | **Aspiración masiva a ADHOCRACIA (+21.52 pts de brecha)**<br>Fuerte demanda de modernización, agilidad y automatización (Deseado = 34.14 pts). | Generación de "Shadow IT" (sistemas piratas, hojas de cálculo compartidas o macros no controladas creadas por áreas impacientes) generando vulnerabilidades y pérdida de datos. | **Mecanismo formal de co-creación e incubación digital:** Implementar un Comité de Transformación Digital con metodología ágil (Scrum/Kanban) que canalice iniciativas de innovación bajo estándares de OGTIC. | **Sección 6.2:** Objetivos Estratégicos de TI<br>**Sección 7.2:** Programa de Innovación Abierta |
| **3** | **Supuesto básico: "La información es coto de poder del área"**<br>Silos de datos herméticos entre Gestión Tributaria (GGT), Desarrollo Urbano (GDU) y Tránsito (GTPSC). | Boicot pasivo al proyecto de **Plataforma de Interoperabilidad Espacial y Catastro Multipropósito**; las gerencias se negarán a ceder o compartir sus bases de datos. | **Gobernanza del Dato e Inventario Oficial de Activos:** Designar formalmente a los directores de gerencia como "Data Owners" (Custodios de Información) con responsabilidades tipificadas antes de iniciar la integración técnica. | **Sección 7.3:** Hoja de Ruta (Secuencia obligatoria de proyectos)<br>**Sección 8:** Arquitectura de Datos |
| **4** | **Supuesto básico: "El error se castiga y expone al OCI"**<br>Cultura punitiva documentada en el RISST y aversión extrema al riesgo operacional. | El registro de incidentes de seguridad y fallas de sistemas permanecerá en blanco; no habrá datos para mejora continua ni respuesta a ciberataques. | **Política de "Just Culture" (Cultura Justa) y reporte no punitivo:** Establecer un protocolo formal de reporte de incidentes y vulnerabilidades TI enfocado en la causa raíz técnica y no en la sanción individual, avalado por Gerencia Municipal. | **Sección 9:** Gestión de Ciberseguridad y Riesgos<br>**Sección 10.3:** Gestión del Cambio Organizacional |
| **5** | **Divergencia cultural entre áreas (OGTIC=Adhocracia 47.9 vs OGAF=Jerarquía 48.5 vs GGT=Mercado 34.9)** | Un enfoque genérico de comunicación y despliegue causará el rechazo frontal de Administración o indiferencia de Tributaria. | **Matriz de Comunicaciones y Despliegue Diferenciada:**<br>- Para OGAF: Énfasis en cumplimiento normativo, auditoría y ahorro documental.<br>- Para GGT: Énfasis en incremento de recaudación y reducción de mora.<br>- Para OGTIC: Énfasis en autonomía tecnológica y arquitectura ágil. | **Sección 10.2:** Matriz de Stakeholders y Plan de Comunicaciones |
| **6** | **Supuesto básico: "TI es solo soporte de hardware y mantenimiento"**<br>OGTIC marginada de las mesas de decisiones de inversión misional del PEI. | Reducción del PETI a simple renovación de computadoras (AEI.07.04) sin financiamiento para la reingeniería y automatización de procesos (AEI.07.02). | **Reposicionamiento de OGTIC en el ROF:** Elevar a la OGTIC al Comité de Gerentes con voz técnica y voto vinculante sobre cualquier proyecto de modernización o software en la provincia. | **Sección 2.1:** Rol Estratégico de TI<br>**Sección 10.1:** Estructura Organizativa de TI |

---

## 2. Decisiones Clave para la Hoja de Ruta del PETI (Sección 7.3)

A partir de estas implicancias, la secuencia técnica de ejecución del PETI no podrá ser puramente tecnológica, sino socio-técnica:

1. **Fase 0 (Meses 1-3) — Marco Institucional y Desarme del Temor:**  
   Emisión de resoluciones municipales de validez legal del expediente digital, creación del Comité de Transformación Digital y firma de acuerdos de confidencialidad y gobernanza del dato con OGAF, GGT y GDU.
2. **Fase 1 (Meses 4-8) — Proyectos "Quick Wins" de Alta Adhocracia y Visibilidad:**  
   Implementación de la Ventanilla Única Digital y Pasarela de Pagos Virtual para GGT (satisface la orientación a Mercado y canaliza el apetito de Adhocracia).
3. **Fase 2 (Meses 9-18) — Núcleo de Integración y Expediente Electrónico:**  
   Despliegue del Sistema de Gestión Documental Cero Papel con firma digital integrada y el Catastro Digital Interoperable.
