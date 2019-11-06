#!/usr/bin/python
import lcddriver;
import threading;
import RPi.GPIO as Gp
import time
import sys
import bluetooth

Gp.setmode(Gp.BCM)
Gp.setwarnings(False)

display = lcddriver.lcd()
cmds=['FF','BB','RR','LL','II','JJ','GG','HH','SS']
cmds1 = ['SVS','SWS']

Pin_1 = 4;
Pin_2 = 17;
Pin_3 = 27;
Pin_4 = 22;
ForwardTrue = True;
Distance = 0;
Buzzer = 25;
HeadLight = 5;

TRIG=23;
ECHO=24;
ThreadVar = True;
Gp.setup(Buzzer,Gp.OUT);
Gp.output(Buzzer,0);
Gp.setup(TRIG,Gp.OUT)
Gp.output(TRIG,0);
Gp.setup(ECHO,Gp.IN);

Gp.setup(Pin_1,Gp.OUT);
Gp.setup(Pin_2,Gp.OUT);
Gp.setup(Pin_3,Gp.OUT);
Gp.setup(Pin_4,Gp.OUT);
Gp.setup(HeadLight,Gp.OUT);

Gp.output(Pin_1,Gp.LOW);
Gp.output(Pin_2,Gp.LOW);
Gp.output(Pin_3,Gp.LOW);
Gp.output(Pin_4,Gp.LOW);
Gp.output(HeadLight,Gp.LOW);

pins = [Pin_1,Pin_2,Pin_3,Pin_4];

def write(onoff):
 for i in range(4):
  Gp.output(pins[i],int(onoff[i]));

def Honk_on():
 Gp.output(Buzzer,1);

def Honk_off():
 Gp.output(Buzzer,0);

def HeadLightOn():
 Gp.output(HeadLight,1);

def HeadLightOff():
 Gp.output(HeadLight,0);

def FF():
 display.lcd_clear()
 display.lcd_display_string("Forward",1);
 write('1001');

def BB():
 display.lcd_clear();
 display.lcd_display_string("Backward",1);
 write('0110');

def RR():
 display.lcd_clear();
 display.lcd_display_string("Turn Right",1);
 write('0101');

def LL():
 display.lcd_clear();
 display.lcd_display_string("Turn Left",1);
 write('1010');

def GG():
 display.lcd_clear();
 display.lcd_display_string("Forward Turn Left",1);
 write('1001');
 time.sleep(0.1);
 write('1000');
 time.sleep(0.1);

def HH():
 display.lcd_clear();
 display.lcd_display_string("Backward Turn Right",1);
 write('0110');
 time.sleep(0.1);
 write('0100');
 time.sleep(0.1);

def II():
 display.lcd_clear();
 display.lcd_display_string("Forward Turn Right",1);
 write('1001');
 time.sleep(0.1);
 write('0001');
 time.sleep(0.1);

def JJ():
 display.lcd_clear();
 display.lcd_display_string("Backward Turn Left",1);
 write('0110');
 time.sleep(0.1);
 write('0010');
 time.sleep(0.1);


def SS():
 write('0000');

def turn():
 display.lcd_clear();
 display.lcd_display_string("Obstacle Ahead",1);
 write('0101');
 time.sleep(.15);

def distance_thread():
 global ThreadVar;
 global Distance;
 while ThreadVar:
   Gp.output(TRIG,False)
   time.sleep(0.1);
   Gp.output(TRIG,True)
   time.sleep(0.00001)
   Gp.output(TRIG,False)

   while Gp.input(ECHO) == 0:
    pulse_start = time.time()

   while Gp.input(ECHO) == 1:
    pulse_end = time.time()

   pulse_duration = pulse_end - pulse_start

   distance = pulse_duration * 17150
   distance = round(distance,2)
   Distance = distance;
   print distance
   if(distance<20):
    global ForwardTrue
    ForwardTrue = False;
   else:
    ForwardTrue = True;
 else:
  print ("Threading Completed")


try:
  #t1 = threading.Thread(target=distance_thread)
  #t1.start()

  server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
  port = 1
  server_socket.bind(("",port))
  server_socket.listen(1)
  print "Listening !!!"

  client_socket,address=server_socket.accept()
  print "Accepted From : ",address

  while True:
   data = client_socket.recv(1024);
   temp_data = data;
   data=data.upper();
   #print Distance;
   if(data in cmds):
    eval(data)();

   """
   if(data == "FF"):
    #if(ForwardTrue):
     FF();
    #else:
     #SS();
   elif(data == "RR"):
     RR();
   elif(data == "BB"):
     BB();
   elif(data == "LL"):
     LL();
   elif(data == "II"):
     II();
   elif(data == "SS"):
     SS();


   if(temp_data == "SVS"):
    Honk_on();
   elif(temp_data == "SvS"):
    Honk_off();

   if(temp_data == "SWS"):
    HeadLightOn();
   elif(temp_data == "SwS"):
    HeadLightOff();
   """
except KeyboardInterrupt:
 #ThreadVar = False;
 time.sleep(2);
 #t1.join()
 print ("Initiating Cleaning Up !!!")

finally:
 print ("Finally Cleanup")
 client_socket.close()
 server_socket.close()
 Gp.output(Pin_1,0);
 Gp.output(Pin_2,0);
 Gp.output(Pin_3,0);
 Gp.output(Pin_4,0);
 Gp.output(Buzzer,0);
 display.lcd_clear();
 Gp.cleanup();



LETTER OF RECOMMENDATION
I am writing this letter in support of Mr. Abhay Tyagi’s application to your University, for pursuing graduate study and research at your reputed institute. 
I have known him since 3rd year of graduation during which I taught him the subject ‘Web Technology’ in his VII semester at SRM University. Additionally, I evaluated his third-year Minor project titled Shopping Cart based on online shopping. I evaluated his class progress, assignments and assessments. I was informed about his enthusiasm to learn the Agile Methodology for software development during his industrial training at Secure Private Ltd, Udaipur. I found Abhay to be a sincere and hard-working student, He displayed his potential to brilliantly practically execute theoretical concepts in his Minor project where he scored an “S” grade (Outstanding Grade) after developing a fully functional shopping website.
Being an active participant in many college seminars and workshops he demonstrated strong will to learn, apt maturity and sincerity. He encouraged fellow students to take up projects in varied inter-disciplinary fields and constantly motivated his juniors and batchmates to participate more in technical events all over the country. Also, his constant involvement in teaching rural and specially-abled kids reflected his strong extra co-curricular presence on campus and humble nature.
Abhay has a very clear view of his goals and always remains clear of indecisiveness and hesitation. He likes to lead from the front and possesses a special talent of always coming up with original and creative ideas.
Thus, I am sure of his capability to pursue the graduate program. Accordingly, I endorse his application wholeheartedly and wish him good luck for the future.
Prof. Govind Verma 
Assistant Professor, 
SRM University, __ (city)

