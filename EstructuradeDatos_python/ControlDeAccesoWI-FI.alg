Algoritmo ControlAccesosWiFi
    // Definición de variables globales
    Definir dispositivosAutorizados Como Caracter
    Definir conexionesActivas Como Caracter
    Definir maxConexiones Como Entero
    Definir registrosAcceso Como Caracter
    Definir numDispositivos, numRegistros Como Entero
    
    // Inicialización de variables
    maxConexiones <- 5
    numDispositivos <- 0
    numRegistros <- 0
    Dimension dispositivosAutorizados[100, 3]  // MAC, IP, Estado
    Dimension conexionesActivas[50, 4]         // MAC, IP, Hora, Tipo
    Dimension registrosAcceso[200, 4]          // MAC, IP, Hora, Evento
    
    // Menú principal
    Definir opcion Como Entero
    Repetir
        Escribir "=== SISTEMA DE CONTROL DE ACCESOS WiFi ==="
        Escribir "1. Registrar dispositivo"
        Escribir "2. Validar acceso"
        Escribir "3. Mostrar dispositivos autorizados"
        Escribir "4. Mostrar conexiones activas"
        Escribir "5. Generar reporte de alertas"
        Escribir "6. Salir"
        Escribir "Seleccione una opción: "
        Leer opcion
        
        Segun opcion Hacer
            1: 
                RegistrarDispositivo(dispositivosAutorizados, numDispositivos)
            2:
                ValidarAcceso(dispositivosAutorizados, numDispositivos, conexionesActivas, registrosAcceso, numRegistros, maxConexiones)
            3:
                MostrarDispositivos(dispositivosAutorizados, numDispositivos)
            4:
                MostrarConexiones(conexionesActivas)
            5:
                GenerarAlertas(registrosAcceso, numRegistros)
            6:
                Escribir "Saliendo del sistema..."
            De Otro Modo:
                Escribir "Opción no válida"
        FinSegun
    Hasta Que opcion = 6
FinAlgoritmo

// Función para registrar un nuevo dispositivo
SubProceso RegistrarDispositivo(dispositivosAutorizados Por Referencia, numDispositivos Por Referencia)
    Definir mac, ip Como Caracter
    Definir i Como Entero
    Definir existe Como Logico
    
    Escribir "=== REGISTRAR NUEVO DISPOSITIVO ==="
    Escribir "Ingrese MAC del dispositivo (formato: XX:XX:XX:XX:XX:XX): "
    Leer mac
    Escribir "Ingrese IP del dispositivo: "
    Leer ip
    
    // Validar si el dispositivo ya existe
    existe <- Falso
    Para i <- 0 Hasta numDispositivos - 1 Hacer
        Si dispositivosAutorizados[i, 0] = mac Entonces
            existe <- Verdadero
        FinSi
    FinPara
    
    Si existe = Verdadero Entonces
        Escribir "Error: El dispositivo con MAC ", mac, " ya está registrado"
    Sino
        dispositivosAutorizados[numDispositivos, 0] <- mac
        dispositivosAutorizados[numDispositivos, 1] <- ip
        dispositivosAutorizados[numDispositivos, 2] <- "Autorizado"
        numDispositivos <- numDispositivos + 1
        Escribir "Dispositivo registrado exitosamente"
    FinSi
FinSubProceso

// Función para validar acceso a la red
SubProceso ValidarAcceso(dispositivosAutorizados Por Referencia, numDispositivos Por Referencia, conexionesActivas Por Referencia, registrosAcceso Por Referencia, numRegistros Por Referencia, maxConexiones Por Referencia)
    Definir mac, ip, hora Como Caracter
    Definir i, j, k Como Entero
    Definir dispositivoEncontrado, espacioEncontrado Como Logico
    Definir conexionesSimultaneas Como Entero
    
    Escribir "=== VALIDAR ACCESO A LA RED ==="
    Escribir "Ingrese MAC del dispositivo: "
    Leer mac
    Escribir "Ingrese IP del dispositivo: "
    Leer ip
    Escribir "Ingrese hora de conexión (HH:MM): "
    Leer hora
    
    dispositivoEncontrado <- Falso
    conexionesSimultaneas <- 0
    
    // Buscar dispositivo en la lista de autorizados
    Para i <- 0 Hasta numDispositivos - 1 Hacer
        Si dispositivosAutorizados[i, 0] = mac Entonces
            dispositivoEncontrado <- Verdadero
            
            // Contar conexiones activas
            Para j <- 0 Hasta 49 Hacer
                Si conexionesActivas[j, 0] <> "" Entonces
                    conexionesSimultaneas <- conexionesSimultaneas + 1
                FinSi
            FinPara
            
            // Verificar si hay espacio disponible
            Si conexionesSimultaneas < maxConexiones Entonces
                // Buscar espacio libre en conexiones activas
                espacioEncontrado <- Falso
                Para k <- 0 Hasta 49 Hacer
                    Si conexionesActivas[k, 0] = "" Y espacioEncontrado = Falso Entonces
                        conexionesActivas[k, 0] <- mac
                        conexionesActivas[k, 1] <- ip
                        conexionesActivas[k, 2] <- hora
                        conexionesActivas[k, 3] <- "Conectado"
                        espacioEncontrado <- Verdadero
                    FinSi
                FinPara
                
                // Registrar en logs
                registrosAcceso[numRegistros, 0] <- mac
                registrosAcceso[numRegistros, 1] <- ip
                registrosAcceso[numRegistros, 2] <- hora
                registrosAcceso[numRegistros, 3] <- "Acceso autorizado"
                numRegistros <- numRegistros + 1
                
                Escribir "Acceso AUTORIZADO para ", mac
            Sino
                Escribir "Acceso DENEGADO: Límite de conexiones simultáneas alcanzado"
                
                // Registrar alerta
                registrosAcceso[numRegistros, 0] <- mac
                registrosAcceso[numRegistros, 1] <- ip
                registrosAcceso[numRegistros, 2] <- hora
                registrosAcceso[numRegistros, 3] <- "ALERTA: Límite conexiones"
                numRegistros <- numRegistros + 1
            FinSi
        FinSi
    FinPara
    
    Si dispositivoEncontrado = Falso Entonces
        Escribir "Acceso DENEGADO: Dispositivo no autorizado"
        
        // Registrar alerta de acceso no autorizado
        registrosAcceso[numRegistros, 0] <- mac
        registrosAcceso[numRegistros, 1] <- ip
        registrosAcceso[numRegistros, 2] <- hora
        registrosAcceso[numRegistros, 3] <- "ALERTA: Acceso no autorizado"
        numRegistros <- numRegistros + 1
    FinSi
FinSubProceso

// Función para generar alertas y reportes
SubProceso GenerarAlertas(registrosAcceso Por Referencia, numRegistros Por Referencia)
    Definir i Como Entero
    Definir alertasEncontradas Como Logico
    
    Escribir "=== REPORTE DE ALERTAS ==="
    alertasEncontradas <- Falso
    
    Para i <- 0 Hasta numRegistros - 1 Hacer
        Si SubCadena(registrosAcceso[i, 3], 1, 6) = "ALERTA" Entonces
            Escribir "Alerta: ", registrosAcceso[i, 3]
            Escribir "  Dispositivo: ", registrosAcceso[i, 0]
            Escribir "  IP: ", registrosAcceso[i, 1]
            Escribir "  Hora: ", registrosAcceso[i, 2]
            Escribir "----------------------------------------"
            alertasEncontradas <- Verdadero
        FinSi
    FinPara
    
    Si alertasEncontradas = Falso Entonces
        Escribir "No se encontraron alertas en el sistema"
    FinSi
FinSubProceso

// Función para mostrar dispositivos autorizados
SubProceso MostrarDispositivos(dispositivosAutorizados, numDispositivos)
    Definir i Como Entero
    
    Escribir "=== DISPOSITIVOS AUTORIZADOS ==="
    Si numDispositivos = 0 Entonces
        Escribir "No hay dispositivos registrados"
    Sino
        Para i <- 0 Hasta numDispositivos - 1 Hacer
            Escribir "Dispositivo ", i + 1, ":"
            Escribir "  MAC: ", dispositivosAutorizados[i, 0]
            Escribir "  IP: ", dispositivosAutorizados[i, 1]
            Escribir "  Estado: ", dispositivosAutorizados[i, 2]
            Escribir "----------------------------------------"
        FinPara
    FinSi
FinSubProceso

// Función para mostrar conexiones activas
SubProceso MostrarConexiones(conexionesActivas)
    Definir i, contador Como Entero
    
    Escribir "=== CONEXIONES ACTIVAS ==="
    contador <- 0
    
    Para i <- 0 Hasta 49 Hacer
        Si conexionesActivas[i, 0] <> "" Entonces
            Escribir "Conexión ", contador + 1, ":"
            Escribir "  MAC: ", conexionesActivas[i, 0]
            Escribir "  IP: ", conexionesActivas[i, 1]
            Escribir "  Hora: ", conexionesActivas[i, 2]
            Escribir "  Estado: ", conexionesActivas[i, 3]
            Escribir "----------------------------------------"
            contador <- contador + 1
        FinSi
    FinPara
    
    Si contador = 0 Entonces
        Escribir "No hay conexiones activas"
    FinSi
FinSubProceso
