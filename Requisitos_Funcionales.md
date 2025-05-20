# ✅ Requisitos Funcionales - Abarrotes Tizimín  
**Rango de prioridad:**  
- **1:** Crítica  
- **2:** Alta  
- **3:** Media  
- **4:** Baja  
- **5:** Muy baja  

---

## Gestión de Clientes  

### RF-01: Registrar cliente  
**Prioridad:** 1  
**Descripción:**  
Registrar clientes con:  
- ID único  
- Nombre y Apellido Paterno  
- Dirección (Calle, Número, Colonia, CP, Ciudad, Estado)  
- Teléfono  

**Validación:**  
- Sistema asigna ID automático no editable.  
- Mensaje: *"Cliente [Nombre] registrado exitosamente"*.  

---

## Gestión de Artículos  

### RF-02: Registrar artículo  
**Prioridad:** 1  
**Descripción:**  
Registrar artículos con:  
- ID único  
- Nombre  
- Precio público  
- Precio proveedor  
- Stock inicial  

**Validación:**  
- Stock mínimo = 0.  

---

## Proceso de Compra  

### RF-03: Realizar compra  
**Prioridad:** 1  
**Descripción:**  
- Seleccionar cliente registrado.  
- Agregar artículos al carrito (ID + cantidad).  
- Calcular total basado en precios públicos.  

**Flujo:**  
1. Validar stock antes de confirmar (RF-04).  
2. Actualizar stock automáticamente (RF-05).  

---

### RF-04: Verificar existencia  
**Prioridad:** 1  
**Descripción:**  
- Bloquear compra si no hay stock suficiente.  
- Mostrar mensaje: *"Error: Stock insuficiente de [Artículo]"*.  

---

### RF-05: Actualizar stock automáticamente  
**Prioridad:** 2  
**Descripción:**  
- Reducir stock tras compra exitosa.  
- Revertir cambios si la compra se cancela.  

**Validación:**  
- Mensaje post-venta: *"Stock actualizado: [Artículo] = [Nuevo Stock]"*.  

---

## Generación de Tickets  

### RF-06: Generar ticket de compra  
**Prioridad:** 2  
**Contenido Obligatorio:**  
- Nombre del cliente y fecha.  
- Lista de artículos (nombre, cantidad, precio unitario).  
- Total general.  
- Logo de la tienda.  

**Formato:**  
- PDF imprimible o vista previa en pantalla.  

---

## Interfaz Gráfica  

### RF-07: Menú gráfico interactivo  
**Prioridad:** 3  
**Opciones Principales (JavaFX/Swing o PyQt):**  
1. Registrar cliente  
2. Registrar artículo  
3. Realizar compra  
4. Buscar clientes/artículos (RF-08)  
5. Historial de compras (RF-09)  
6. Salir  

---

## Búsquedas y Consultas  

### RF-08: Buscar clientes y artículos  
**Prioridad:** 3  
**Criterios de Búsqueda:**  
- **Clientes:** ID, nombre, apellido.  
- **Artículos:** ID, nombre, rango de precios (público o proveedor).  

**Interfaz:**  
- Resultados en tabla con opción de selección múltiple.  

---

## Historiales y Reportes  

### RF-09: Historial de compras por cliente  
**Prioridad:** 3  
**Contenido:**  
- Listado cronológico de compras.  
- Detalles por transacción: fecha, artículos, montos.  

**Restricción:**  
- Solo visible si el cliente tiene ≥1 compra registrada.  

---

## Alertas y Notificaciones  

### RF-10: Notificaciones de stock bajo  
**Prioridad:** 4  
**Activación:**  
- Al realizar compras que dejen stock <5 unidades.  
- Al abrir el menú de registro de artículos.  

**Mensaje:**  
- *"¡Atención! [Artículo] tiene bajo stock (Unidades: [X]). ¿Reponer ahora? [Sí/No]"*.  
