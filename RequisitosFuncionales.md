# Requisitos Funcionales 
## Gestión de Clientes
### RF-01: Registrar cliente

Descripción:

El sistema debe permitir registrar clientes con sus datos personales:

-Identificador del Cliente (ID único).

-Nombre y Apellido Paterno.

-Dirección (compuesta por: Calle, Número, Colonia, CP, Ciudad, Estado).

-Teléfono.

## Gestión de Artículos
### RF-02: Registrar artículo

Descripción:

El sistema debe permitir registrar artículos con los siguientes atributos:

-Identificador del artículo (ID único).

-Nombre del artículo.

-Precio al público.

-Precio del proveedor.

-Cantidad total en existencia (stock).

## Proceso de Compra
### RF-03: Realizar compra

Descripción:
El sistema debe permitir:

-Seleccionar un cliente registrado.

-Agregar artículos al carrito de compra, especificando la cantidad deseada.

-Verificar automáticamente la existencia en stock antes de confirmar la compra (RF-04).

-Calcular el importe total basado en los precios al público.


### RF-04: Verificar existencia

Descripción:

El sistema debe validar que haya suficiente stock para los artículos seleccionados. Si no hay suficiente, mostrar un mensaje de error y evitar finalizar la compra.

## Generación de Tickets
### RF-05: Generar ticket de compra

Descripción:

El sistema debe emitir un ticket con la siguiente información:

-Nombre del cliente.

-Fecha de la compra.

-Lista de artículos comprados (nombre, cantidad, precio unitario).

-Importe total de la compra.

## Interfaz Gráfica
### RF-06: Menú gráfico interactivo

Descripción:

El sistema debe mostrar un menú principal con las siguientes opciones (usando una librería como JavaFX o Swing):

-Registrar un cliente.

-Registrar un artículo.

-Realizar una compra.

-Salir del sistema.

