#💻Patrones de diseño usados en el proyeto
### **Patrón Observer (Actualización de interfaz en ventas y stock)**  
   - **¿Por qué se usó?**  
     - Permite que las **interfaces gráficas y otras clases dependientes** se actualicen automáticamente cuando cambian los datos del modelo (ej: stock, lista de artículos, resumen de compra).  
     - Evita el acoplamiento directo entre los componentes lógicos (modelo) y visuales (vista), favoreciendo una arquitectura desacoplada y flexible.  
   - **Beneficio clave:**  
     - Asegura que múltiples elementos de la interfaz se mantengan **sincronizados en tiempo real** con los cambios del sistema, sin necesidad de invocar manualmente métodos de actualización.  
![image](https://github.com/user-attachments/assets/74262ad0-0fc8-4dee-99c5-7348b5b46671)

### **Patrón Singleton (Clase `Tienda`)**  
   - **¿Por qué se usó?**  
     - Garantiza que exista **una única instancia global** de la tienda, centralizando el acceso a listas de clientes, artículos y ventas.  
     - Evita inconsistencia de datos y duplicación de recursos.  
   - **Beneficio clave:**  
     - Coordinación segura en operaciones críticas (ej: actualizar inventario durante una venta).  

![image](https://github.com/user-attachments/assets/e4884d27-2eea-4550-b226-150e901164ee)


### **Patrón Factory Method (Creación de `Ticket`)**  
   - **¿Por qué se usó?**  
     - Permite crear diferentes tipos de tickets (ej: simple, PDF, email) **sin modificar el código de la venta**.  
     - Facilita la extensión futura: nuevos formatos de tickets se añaden con mínimos cambios.  
   - **Beneficio clave:**  
     - Separa la lógica de creación de tickets de la lógica comercial, cumpliendo el principio *Open/Closed*.  

![image](https://github.com/user-attachments/assets/1627f7be-7988-4af6-857a-c80725715a70)
![image](https://github.com/user-attachments/assets/03d4473f-26dc-4c20-a84e-610695ea657f)
![image](https://github.com/user-attachments/assets/6b3f2ada-b94f-4a4f-aa67-172267c57175)

