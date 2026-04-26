import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc

# Inicialización de estado en Streamlit
if "tipo_mov" not in st.session_state:
    st.session_state.tipo_mov = []

# Inicializar arrays en sesión
if "nombres" not in st.session_state:
    st.session_state.nombres = np.array([], dtype=object)
    st.session_state.categorias = np.array([], dtype=object)
    st.session_state.precios = np.array([], dtype=float)
    st.session_state.cantidades = np.array([], dtype=int)
    st.session_state.totales = np.array([], dtype=float)

# Inicializar historial
if "historial" not in st.session_state:
    st.session_state.historial = []

# Inicialización de CRUD en Streamlit
if "disponibilidad" not in st.session_state:
    st.session_state.disponibilidad = []

# Menú en la barra lateral
st.sidebar.title("Opciones")
opcion = st.sidebar.selectbox(
    "Selecciona una opción:",
    ("🏠 Home","📋 Ejercicio 1", "📋 Ejercicio 2", "📋 Ejercicio 3","📋 Ejercicio 4")
)

# Mostrar contenido según la opción elegida
if opcion == "🏠 Home":
    st.subheader("PROYECTO 1-APLICACIÓN EN STREAMLIT")
    st.image("python_1.png",width=200)
    st.write("**Nombre completo del estudiante**: Luis Anderson Polo Benites")
    st.write("**Nombre del módulo**: Python Fundamentals")
    st.write("**Información general del estudiante**: Analista de Datos")
    st.write("**Año**: 2026")
    st.write("**Breve descripción del proyecto**: Este proyecto representa la primera aplicación práctica del módulo")
    st.write("**Tecnologías utilizadas**: La libreria utilizada hasta el momento es : streamlit")



if opcion == "📋 Ejercicio 1":
    st.subheader("Ejercicio 1 - Flujo de caja con listas")
    
    st.markdown("*Se debe ingresar el concepto, escoger el tipo de movimiento e ingresar el valor* .")

    concepto=st.text_input("**Ingrese el Concepto**")
    tipo=st.selectbox("**Selecciona un tipo de Movimiento**",("Ingreso","Gasto"))
    val=st.number_input("**Ingrese el Valor**",min_value=0.0, format="%.2f")
    
    # Botón para agregar
    if st.button("Agregar"):
        if concepto != "" and val > 0:
            movimiento = {
                "Concepto": concepto,
                "Tipo": tipo,
                "Valor": val
            }
            st.session_state.tipo_mov.append(movimiento)
            st.success("Movimiento agregado")
        else:
            st.warning("Completa los datos correctamente")

    # ---- Mostrar lista ----
    st.subheader("Lista de movimientos")

    if len(st.session_state.tipo_mov) > 0:        
        df = pd.DataFrame(st.session_state.tipo_mov)
        st.dataframe(df)          
    else:
        st.write("No hay movimientos registrados")

    # ---- Totales de movimientos ----
    total_ingresos = 0
    total_gastos = 0

    for m in st.session_state.tipo_mov:
        if m["Tipo"] == "Ingreso":
            total_ingresos += m["Valor"]
        else:
            total_gastos += m["Valor"]

    saldo_final= total_ingresos - total_gastos

    st.subheader("Total de Movimientos")
    st.write(f"**Total Ingresos**: S/ {total_ingresos}")
    st.write(f"**Total Gastos**: S/ {total_gastos}")
    st.write(f"**Saldo Final**: S/ {saldo_final}")

    st.subheader("Flujo de Caja")
    if saldo_final  > 0:
        st.write("Flujo de caja a Favor")
    elif saldo_final  < 0:
        st.write("Flujo de caja en contra")

elif opcion == "📋 Ejercicio 2":

    st.subheader("Ejercicio 2 - Registro con NumPy, arrays y DataFrame")
    st.markdown("*En este ejercicio se deberá crear un formulario para registrar información usando arreglos de NumPy.* .")

    # ---- Formulario ----
    st.subheader("Agregar producto")

    nombre = st.text_input("Nombre del producto")
    categoria = st.selectbox("Categoría", ["Alimentos", "Bebidas", "Tecnología", "Otros"])
    precio = st.number_input("Precio", min_value=0.0, format="%.2f")
    cantidad = st.number_input("Cantidad", min_value=1, step=1)

    # Total
    total = precio * cantidad
    st.write(f"Total: S/ {total:.2f}")

    # ---- Botón ----
    if st.button("Agregar"):
        if nombre != "" and precio > 0 and cantidad > 0:
            # Agregar a arrays de NumPy
            st.session_state.nombres = np.append(st.session_state.nombres, nombre)
            st.session_state.categorias = np.append(st.session_state.categorias, categoria)
            st.session_state.precios = np.append(st.session_state.precios, precio)
            st.session_state.cantidades = np.append(st.session_state.cantidades, cantidad)
            st.session_state.totales = np.append(st.session_state.totales, total)

            st.success("Registro agregado")
        else:
            st.warning("Completa los datos correctamente")

    # ---- Convertir a DataFrame ----
    st.subheader("Tabla de registros")

    if len(st.session_state.nombres) > 0:
        df = pd.DataFrame({
            "Producto": st.session_state.nombres,
            "Categoría": st.session_state.categorias,
            "Precio": st.session_state.precios,
            "Cantidad": st.session_state.cantidades,
            "Total": st.session_state.totales
        })

        st.dataframe(df)
    else:
        st.write("No se han registros productos")

elif opcion == "📋 Ejercicio 3":
    st.subheader("Ejercicio 3 - Uso de funciones desde una librería externa")

    st.subheader("Ingresar valores")

    val_tamano_mb = st.number_input("Tamaño de MB", value=0.0)
    val_vel_mb = st.number_input("Velocidad MB", value=0.0)

    # ---- Botón para ejecutar ----
    if st.button("Ejecutar"):
        resultado = lf.calcular_tiempo_transferencia_archivo(val_tamano_mb, val_vel_mb)

        # Mostrar resultado
        st.success(f"Resultado: {resultado}")

        # Guardar en historial
        registro = {
            "Número 1": val_tamano_mb,
            "Número 2": val_vel_mb,
            "Resultado": resultado
        }
        st.session_state.historial.append(registro)

    # ---- Mostrar historial ----
    st.subheader("Historial de resultados")

    if len(st.session_state.historial) > 0:
        df = pd.DataFrame(st.session_state.historial)
        st.dataframe(df)
    else:
        st.write("No hay valores que presentar")

elif opcion == "📋 Ejercicio 4":
    st.subheader("Ejercicio 4 - Uso de clases desde una librería externa con CRUD")

    # Menú de navegación
    opcion = st.sidebar.selectbox("Selecciona una acción", ["Agregar Disponibilidad", "Ver Disponibilidad", "Actualizar Disponibilidad", "Eliminar Disponibilidad"])

    # Agregar nueva Disponibilidad
    if opcion == "Agregar Disponibilidad":
        st.subheader("➕ Agregar Nueva Disponibilidad")
        nombre = st.text_input("Nombre")
        tiempo_total = st.number_input("Tiempo Total H", min_value=0.0)
        tiempo_caida = st.number_input("Tiempo Caida H", min_value=0.0)
        almacenamiento_total = st.number_input("Almacenamiento Total GB", min_value=0.0)
        almacenamiento_caida = st.number_input("Almacenamiento Caida GB", min_value=0.0)

        if st.button("Agregar"):
            nueva = lc.Servidor(nombre, tiempo_total, tiempo_caida, almacenamiento_total,almacenamiento_caida)
            st.session_state.disponibilidad.append(nueva)
            st.success("✅ Disponibilidad agregada con éxito.")

    # Ver Disponibilidad
    elif opcion == "Ver Disponibilidad":
        st.subheader("📋 Lista de Disponibilidad de Servidor")
        if st.session_state.disponibilidad:
            for act in st.session_state.disponibilidad:
                st.dataframe(act.resumen())
        else:
            st.info("No hay Disponibilidad de servidor registradas.")

    # Actualizar Disponibilidad
    elif opcion == "Actualizar Disponibilidad":
        st.subheader("🔄 Actualizar Disponibilidad del Servidor")
        nombres = [a.nombre for a in st.session_state.disponibilidad]
        if nombres:
            seleccion = st.selectbox("Selecciona una Servidor Disponible", nombres)
            nuevo_tiempo_caida = st.number_input("Nuevo Tiempo de Caida Horas", min_value=0.0)
            if st.button("Actualizar"):
                for act in st.session_state.disponibilidad:
                    if act.nombre == seleccion:
                        act.tiempo_caida = nuevo_tiempo_caida
                        st.success("Tiempo de Caida actualizado correctamente.")
        else:
            st.info("No hay Disponibilidad de Servidores para actualizar.")

    # Eliminar Disponibilidad
    elif opcion == "Eliminar Disponibilidad":
        st.subheader("🗑️ Eliminar Disponibilidad")
        nombres = [a.nombre for a in st.session_state.disponibilidad]
        if nombres:
            seleccion = st.selectbox("Selecciona una Disponibilidad para eliminar", nombres)
            if st.button("Eliminar"):
                st.session_state.disponibilidad = [a for a in st.session_state.disponibilidad if a.nombre != seleccion]
                st.success("Disponibilidad eliminada correctamente.")
        else:
            st.info("No hay Disponibilidad de Servidor para eliminar.")
