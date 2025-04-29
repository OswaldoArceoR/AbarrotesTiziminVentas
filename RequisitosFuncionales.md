# Requisitos Funcionales - Abarrotes Tizimín  

## Gestión de Clientes  
### RF-01: Registrar cliente  
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
**Descripción:**  
- Seleccionar cliente registrado.  
- Agregar artículos al carrito (ID + cantidad).  
- Calcular total basado en precios públicos.  

**Flujo:**  
1. Validar stock antes de confirmar (RF-04).  
2. Actualizar stock automáticamente (RF-07).  

### RF-04: Verificar existencia  
**Descripción:**  
- Bloquear compra si no hay stock suficiente.  
- Mostrar mensaje: *"Error: Stock insuficiente de [Artículo]"*.  

### RF-07: Actualizar stock automáticamente  
**Descripción:**  
- Reducir stock tras compra exitosa.  
- Revertir cambios si la compra se cancela.  

**Validación:**  
- Mensaje post-venta: *"Stock actualizado: [Artículo] = [Nuevo Stock]"*.  

---

## Generación de Tickets  
### RF-05: Generar ticket de compra  
**Contenido Obligatorio:**  
- Nombre del cliente y fecha.  
- Lista de artículos (nombre, cantidad, precio unitario).  
- Total general.  
- Logo de la tienda.  

**Formato:**  
- PDF imprimible o vista previa en pantalla.  

---

## Interfaz Gráfica  
### RF-06: Menú gráfico interactivo  
**Opciones Principales (JavaFX/Swing):**  
1. Registrar cliente  
2. Registrar artículo  
3. Realizar compra  
4. Buscar clientes/artículos (RF-08)  
5. Historial de compras (RF-09)  
6. Salir  

---

## Búsquedas y Consultas  
### RF-08: Buscar clientes y artículos  
**Criterios de Búsqueda:**  
- **Clientes:** ID, nombre, apellido.  
- **Artículos:** ID, nombre, rango de precios (público o proveedor).  

**Interfaz:**  
- Resultados en tabla con opción de selección múltiple.  

---

## Historiales y Reportes  
### RF-09: Historial de compras por cliente  
**Contenido:**  
- Listado cronológico de compras.  
- Detalles por transacción: fecha, artículos, montos.  

**Restricción:**  
- Solo visible si el cliente tiene ≥1 compra registrada.  

---

## Alertas y Notificaciones  
### RF-10: Notificaciones de stock bajo  
**Activación:**  
- Al realizar compras que dejen stock <5 unidades.  
- Al abrir el menú de registro de artículos.  

**Mensaje:**  
- *"¡Atención! [Artículo] tiene bajo stock (Unidades: [X]). ¿Reponer ahora? [Sí/No]"*.  
