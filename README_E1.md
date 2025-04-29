# 📦 Primera Entrega - Proyecto "Abarrotes Tizimín"

**Fecha de Entrega:** 29/04/2025 
**Versión:** 1.0  

---

## 📄 Descripción de la Entrega  
Esta primera entrega corresponde al **diseño conceptual del sistema**, incluyendo documentación técnica esencial para sentar las bases del desarrollo.  

---

## 🗂️ Componentes Entregados  

### 1. **📋 Requisitos Funcionales**  
   - Listado detallado de las funcionalidades prioritarias del sistema.  
   - Incluye: Registro de clientes, gestión de artículos, proceso de venta y generación de tickets.  

### 2. **📊 Diagrama de Casos de Uso**  
   - Representación visual de las interacciones entre el gerente y el sistema.  
   - Casos principales: Registrar cliente, registrar artículo, realizar compra.  

### 3. **⏳ Diagrama de Secuencias (Proceso de Compra)**  
   - Flujo detallado de la operación más crítica: *Realizar Compra*.  
   - Muestra la comunicación entre componentes (interfaz, lógica de negocio y datos).  

### 4. **🧩 Diagrama de Clases**  
   - Estructura central del sistema con:    
     - **Patrones de diseño aplicados:** Singleton y Factory Method.  

---

## 🔍 Explicación de Patrones de Diseño en el Diagrama de Clases  

### **Patrón Singleton (Clase `Tienda`)**  
   - **¿Por qué se usó?**  
     - Garantiza que exista **una única instancia global** de la tienda, centralizando el acceso a listas de clientes, artículos y ventas.  
     - Evita inconsistencia de datos y duplicación de recursos.  
   - **Beneficio clave:**  
     - Coordinación segura en operaciones críticas (ej: actualizar inventario durante una venta).  

### **Patrón Factory Method (Creación de `Ticket`)**  
   - **¿Por qué se usó?**  
     - Permite crear diferentes tipos de tickets (ej: simple, PDF, email) **sin modificar el código de la venta**.  
     - Facilita la extensión futura: nuevos formatos de tickets se añaden con mínimos cambios.  
   - **Beneficio clave:**  
     - Separa la lógica de creación de tickets de la lógica comercial, cumpliendo el principio *Open/Closed*.  

---

## 🚀 Próximos   
- **Siguiente entrega:** Implementación del código base usando python.  

---
