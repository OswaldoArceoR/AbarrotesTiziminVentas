# 📦 Segunda Entrega - Sistema de Gestión "Abarrotes Tizimín"

## 📋 [Requisitos Funcionales](https://github.com/OswaldoArceoR/AbarrotesTiziminVentas/blob/Segunda_Entrega/Requisitos_Funcionales.md)  

## 📊 Diagramas UML  

### 1.[Casos de Uso](enlace_a_imagen_casos_de_uso.png)  
*Descripción*: Interacciones del usuario (gerente) con el sistema.  

### 2. [Diagrama de Clases](enlace_a_imagen_clases.png)  
*Incluye patrones*:  
- **Singleton**: Clase `Tienda` (una única instancia).  
- **Factory Method**: Creación de `Ticket` mediante `TicketFactory`.  
- **Observer**: Notificaciones de stock bajo (`Articulo` → `VistaPrincipal`).  

### 3. [Secuencia](enlace_a_imagen_secuencia.png)  
*Flujo*: Proceso de venta desde selección de artículos hasta generación de ticket.  

### 4. [Estado](enlace_a_imagen_estado.png)  
*Estados de una venta*: Iniciada → En proceso → Completada/Cancelada.  

### 5. [Colaboración](enlace_a_imagen_colaboracion.png)  
*Interacción entre objetos*: `VistaVenta`, `VentaController`, `Articulo`, `Ticket`.  

### 6. [Actividad](enlace_a_imagen_actividad.png)  
  

---

## 💻 Código Fuente  
### **Repositorio GitHub**  
[![GitHub](https://img.shields.io/badge/GitHub-Código_Fuente-%23181717)](https://github.com/tu-usuario/abarrotes-tizimin)  

## 📱 Prototipos de Interfaz - Sistema de Gestión "Abarrotes Tizimín"

### 🔗 Enlaces a los Prototipos en Figma

### 1. **Estructura del Prototipo (Diseño Visual)**  
[![Figma Design](https://img.shields.io/badge/FIGMA-Design_Structure-%23F24E1E)](https://www.figma.com/design/ZaXGLYtUoOKzb6gdU0PfbP/base?node-id=0-1&t=Tqirw7eSpDGOMEA4-1)  
- **Descripción**:  
  Diseño completo de la interfaz gráfica, incluyendo componentes, paleta de colores y disposición de elementos.  
- **Características**:  
  - Registro de clientes y artículos.  
  - Flujo entre ventanas.  
  - Menú principal interactivo.  

---

### 2. **Prototipo Interactivo (Demo)**  
[![Figma Prototype](https://img.shields.io/badge/FIGMA-Interactive_Prototype-%23F24E1E)](https://www.figma.com/proto/ZaXGLYtUoOKzb6gdU0PfbP/base?node-id=2-6&p=f&t=aHADA9qrbsNlrJOa-0&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=2%3A6)  
- **Descripción**:  
  Versión navegable para probar el flujo de usuario (haz clic en los botones para simular acciones).  
- **Características**:  
  - Simulación de ventanas.  
  - Visualización clara de ideas.  
  - Navegación entre módulos (clientes, artículos, ventas).  

---

