def agenda_telefonica():
    agenda = {}

    while True:
        print("\n--- AGENDA TELEFÓNICA ---")
        print("1. Agregar contacto")
        print("2. Consultar contacto")
        print("3. Eliminar contacto")
        print("4. Mostrar agenda")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre: ").upper()
            telefono = input("Ingrese el teléfono: ")
            agenda[nombre] = telefono
            print("Contacto guardado correctamente.")

        elif opcion == "2":
            nombre = input("Ingrese el nombre a consultar: ").upper()
            if nombre in agenda:
                print(f"Teléfono de {nombre}: {agenda[nombre]}")
            else:
                print("El contacto no existe.")

        elif opcion == "3":
            nombre = input("Ingrese el nombre a eliminar: ").upper()
            if nombre in agenda:
                del agenda[nombre]
                print("Contacto eliminado.")
            else:
                print("El contacto no existe.")

        elif opcion == "4":
            if agenda:
                print("\n--- CONTACTOS ---")
                for nombre, telefono in agenda.items():
                    print(f"{nombre}: {telefono}")
            else:
                print("La agenda está vacía.")

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


# Ejecutar programa
agenda_telefonica()