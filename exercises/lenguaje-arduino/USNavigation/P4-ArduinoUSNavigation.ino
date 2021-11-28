/*
 * Nombre: P3-PythonServoControl.py
 * Descripcion: navegación del robot Arduino con el US montado
 * Autor: Julio Vega
 */
                                                                                
#include <Servo.h> // Incluimos librería Servo

// Instancias de clase Servo:
Servo servoLeft;
Servo servoRight;
Servo servoUS; // US Servo

const int servoLeftPin = 13;
const int servoRightPin = 12;
const int servoUSPin = 11;
const int pingPin = 10;
const int speakerPin = 4;

const int msPerTurnDegree = 6; // Maniobrar
const int tooCloseCm = 30; // distancia minima a objeto
int ccwLim = 1400; // Para el control del US Servo
int rtAngle = 900; // Luego comandamos al US Servo: servoUS.writeMicroseconds(ccwLim - rtAngle + (degreeVal * 10));
const int usTocm = 29; // Factor de conversion del valor devuelto por el US a CM

// Posiciones del US Servo
int usPosiciones[] = {0, 2, 4, 6, 8, 10, 9, 7, 5, 3, 1};

// Array de "elements" posiciones donde almacenar las distancias dadas por el US
const int elements = sizeof(usPosiciones);
int cm[elements];

// Segun las posiciones del US calculamos los intervalos (en grados) de cada posicion
const int gradosPorPosicion = 180/(sizeof(usPosiciones)/sizeof(int)-1);

int i = -1; // indice global
int sign = 1; // signo de incrementos
int theta = -gradosPorPosicion; // posicion inicial del US Servo

void setup() {
  tone(speakerPin, 3000, 1000); // Reproduce un tono durante 1 segundo
  delay(1000); // Retraso del tono
  
  Serial.begin(9600); // Abrimos comunicacion serie

  servoLeft.attach(servoLeftPin); // Conectamos los distintos servos a sus respectivos pines
  servoRight.attach(servoRightPin);
  servoUS.attach(servoUSPin);
  maniobrar(0, 0, 1000); // Permanece quieto durante 1 segundo
  usservo(0); // Ponemos el US Servo en 0 grados
}
 
void loop() {
  maniobrar(200, 200); // Hacia delante a toda velocidad
  i++; // incrementamos en 1 el indice del US Servo

  // Avanzamos el servo a la siguiente posicion y esperamos a que se posicione alli
  theta = usPosiciones[i] * gradosPorPosicion;       
  usservo(theta);
  delay(100);                                

  cm[i] = cmDistance(); // Almacenamos la medida desde la actual posicion del US

  // Si hay un objeto +/- 36 grados del centro y esta demasiado cerca, maniobramos
  if ((usPosiciones[i]>=3) && (usPosiciones[i]<=7) && (cm[i] < tooCloseCm)) {
    maniobrar(0, 0); // nos paramos
    int theta = buscaCaminoDespejado(); // cuantas posiciones ha de moverse a camino despejado
    theta *= gradosPorPosicion; // grados a moverse = posiciones * grados/posicion
    
    // Convertimos esos grados a tiempo que deben moverse las ruedas para apuntar en esa direccion
    int turnAngleTime = (90 - theta) * msPerTurnDegree;
    
    if(turnAngleTime < 0) { // angulo negativo
      maniobrar(-200, 200, -turnAngleTime);
    } else { // si angulo positivo
      maniobrar(200, -200, turnAngleTime);
    }

    maniobrar(200, 200); // y vamos hacia delante otra vez
  }

  if(i == 10) { // cuando el US llega a la posicion maxima, volvemos a la posicion inicial
    i = -1;
  }  
}

/*
 * Control de la direccion del robot:
 * Atras  Linear  Stop  Linear   Adelante
 * -200   -100......0......100      200
 */ 
void maniobrar(int speedLeft, int speedRight) {
  maniobrar(speedLeft, speedRight, 1); // maniobrar con 1 ms de bloqueo
}

/*
 * Control de la direccion del robot
 * msTime - tiempo a bloquear la ejecucion de codigo antes de otra llamada a maniobrar
 */ 
void maniobrar(int speedLeft, int speedRight, int msTime) {
  servoLeft.writeMicroseconds(1500 + speedLeft);
  servoRight.writeMicroseconds(1500 - speedRight);
  if(msTime==-1) { // paramos los servos
    servoLeft.detach();
    servoRight.detach();
  }
  delay(msTime); // Bloqueo/retraso durante msTime milisegundos
}

/*
 * Posicionar US Servo
 */
void usservo(int grados) {
  servoUS.writeMicroseconds(ccwLim - rtAngle + (grados * 10));
}

/*
 * Obtiene distancia (en cm) dada por el us sensor
 */ 
int cmDistance() {
  int distancia = 0;
  do { // bucle que "soporta" la medida 0
    int us = ping(pingPin); // obtenemos medida en microsegundos del us sensor
    distancia = convert(us, usTocm); // conversion a centimetros
    delay(3); // hacemos una pausa antes de reintentar (si es necesario)
  } while(distancia == 0);
                            
  return distancia; // devolvemos la distancia en cm
}

/*
 * Convierte los microsegundos del us sensor a un valor util.
 * us - valor en microsegundos de lo medido por el us sensor
 * scalar - debe valer 29 para pasar de us a cm, o 74 para pasar de us a pulgadas
 */ 
int convert(int us, int scalar) {
    return us / scalar / 2;                        // Echo round trip time -> cm
}

/*
 * Inicia el sensor y toma el tiempo del ultrasonido en ir y volver.
 * pin - pin digital al que esta conectado el sensor us
 * duracion - duracion en microsegundos del eco del ultrasonido
 */ 
long ping(int pin) {
  long duracion;
  pinMode(pin, OUTPUT);
  digitalWrite(pin, LOW); // inicializa el pin a low...
  delayMicroseconds(2); // ...y lo mantiene durante 2 microsegundos
  digitalWrite(pin, HIGH); // envía un pulso alto...
  delayMicroseconds(5); // ...durante 5 microsegundos
  digitalWrite(pin, LOW);
  pinMode(pin, INPUT);
  duracion = pulseIn(pin, HIGH, 25000);
  return duracion;
}    
          
/*
 * Encuentra un camino despejado en un rango de 180º
 * Devuelve: la distancia medida
 */ 
int buscaCaminoDespejado() {
  int Ai; // angulo inicial del us servo
  int Af; // angulo final del us servo
  int k = usPosiciones[i]; // copia local de usPosiciones
  int ki = k; // segunda copia
  int inc; // variable incremento/decremento
  int dt; // incremento de tiempo
  int repcnt = 0; // contador de repeticiones
  int sMin; // minima distancia medida

  if(k <= 5) { // según la posicion del us servo, incrementamos o decrementamos
    inc = 1;
  } else {
    inc = -1;
  }

  // Rotamos el servo del US hasta tener un camino despejado, si llegamos al tope, volvemos al principio, como un aspersor
  // Si no encontramos camino libre, rotamos al robot 90º y repetimos operacion
  do {
    repcnt++;
    if(repcnt > ((sizeof(usPosiciones) / sizeof(int)))*2) { // si no encontramos camino tras dos intentos
      maniobrar(-200, -200, 100); // Hacia atras, girar, parar e intentar otra vez
      maniobrar(-200, 200, 90*6);
      maniobrar(0, 0, 1);
    }

    k += inc; // avanzamos posicion del servo
    if ((k == -1) || (k == 11)) { // cambiamos inc/dec si alcanzamos tope
      k = ki;
      inc = -inc;
      dt = 250; // damos tiempo al servo para llegar ahi
    }

    // Colocamos el servo en la siguiente posicion
    i = findIn(k, usPosiciones, sizeof(usPosiciones)/sizeof(int)); // obtenemos el indice correspondiente...
    int theta = usPosiciones[i] * gradosPorPosicion; // ...y pasamos a grados
    usservo(theta); // posicionamos el servo
    delay(dt); // esperamos a que llegue alli
    dt = 100; // reseteamos a un pequeño delay de 100
    cm[i] = cmDistance(); // y tomamos medida desde ahi
  } while(cm[i] < 30); // estaremos buscando hasta encontrar camino (>30cm despejado)
  
  sMin = 1000; // inicializamos distancia minima a un valor imposiblemente alto
  for(int t = 0; t <= 10; t++) {  
    if(sMin > cm[t]) sMin = cm[t]; // nos quedamos con la menor distancia
  }
  if(sMin < 6) { // si es menor de 6 cm, vamos hacia atras un poco
    maniobrar(-200, -200, 350);
    k = -1; // reseteamos posicion
  }

  maniobrar(0, 0); // Avanzamos indefinidamente hasta detectar otro obstaculo a menos de 30cm
  Ai = usPosiciones[i]; // nos quedamos con el ANGULO INICIAL cuando el obstaculo desaparecio del camino
  k = usPosiciones[i]; // hacemos uns nueva copia

  int aMax = -2; // inicializamos distancia maxima a un valor imposiblemente bajo
  int cmMax = -2;

  do { // bucle de escaneo que repetimos mientras la distancia > 30 o el servo us no este cerca de sus limites
    k += inc; // inc/dec la posicion del servo
    i = findIn(k, usPosiciones, sizeof(usPosiciones)/sizeof(int)); // obtenemos el indice correspondiente...
    int theta = usPosiciones[i] * gradosPorPosicion; // ...y pasamos a grados
    usservo(theta); // posicionamos servo
    delay(100); // esperamos
    cm[i] = cmDistance(); // y tomamos medida

    if(cm[i]>cmMax) { // mantenemos la maxima distancia y su angulo correspondiente
      cmMax = cm[i];
      aMax = usPosiciones[i]; 
    }  
  } while((cm[i] > 30)&&(usPosiciones[i]!=0)&&(usPosiciones[i]!=10)); 
  
  Af = usPosiciones[i]; // guardamos el ANGULO FINAL del servo
  int A = Ai + ((Af-Ai)/2); // y calculamos el angulo intermedio

  i = findIn(5, usPosiciones, sizeof(usPosiciones)/sizeof(int)); // posicionamos el servo en posicion 5 (recto) para ir recto
  int theta = usPosiciones[i] * gradosPorPosicion;
  usservo(theta);
  
  if(sMin < 7) { // vemos sin la distancia minima obtenida es muy pequeña, en tal caso torcemos mas de la cuenta
    if (A < aMax) return aMax; else return A;
  } else {
    if (A < aMax) return A; else return aMax;
  }    
}  
 
/*
 * Devolver indice del array donde se encuentra el valor dado por parametro
 */ 
int findIn(int valor, int array[], int numElements) {
  for(int i = 0; i < numElements; i++) {
    if(valor == array[i]) return i;
  }
  return -1;
}

