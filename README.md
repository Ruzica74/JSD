# JSD

## Instalacija

### Preduslovi

Pre nego što počnete, obezbedite da imate sledeće instalirano na svom sistemu:

```
Python 3.x: Preuzmite sa python.org.
pip: Ovo je obično uključeno u instalaciju Pythona. Možete proveriti pokretanjem pip --version u terminalu.
```

### Koraci za Instalaciju

Korak 1: Klonirajte Repozitorijum
Otvorite terminal i pokrenite:

```


```

## Opis

Jezikom bi se opisivale funkcije u programskom jeziku C, za koje je potrebno kreirati Unit testove. Neke od ključnih riječi, koje bi jezik koristio, su  *function, cases, stubs, end itd. function* bi definisao ime funkcije i njene parametre, te početak opisa određenog testa. Riječ *cases* bi označavala da se u narednim linijama nalaze osnovne informacije o svakom testnom slučaju. U običnim oblim zagradama se navode vrijednosti parametara u tom testnom slučaju. Ako je tip parametra složenog tipa onda se u uglastim zagradama smještaju imena i vrijednosti atributa u sklopu složenog tipa, npr. \[name=john, age=25]. Ako je jedan od parametara pokazivač, onda ispred vrijednosti ili uglaste zagrade potrebno je staviti zvjezdicu *. Nakon definisanja vrijednosti parametara sintaksa nalaže da se stavi strelica => i očekivana povratna vrijednost tog testnog slučaja. Da bi testni slučaj bio potpun potrebn je navesti i opis testa, koji bi se nalazio nakon očekivane vrijednosti testa odvojen tačka zarezom i pod navodnicima. Svaki testni slučaj bi se odvajao zapetom. Nakon testnih slučajeva ključna riječ *stubs* bi se koristila za definisanja funkcija za koje su kreirani stub-ovi. Prilikom uvodjenja stub-ova u oblim zagradama navodio bi se naziv funkcije koja se stabuje, koliko poziva te funkcije se očekuje, te koji je naziv stub-a. *end* je riječ kojom bi se označavao kraj opisa testa. Dodatne ključne riječi će biti uključene u skladu sa potrebama, u toku izrade.  

## Primjer br. 1:
  Za funkciju TtErrorType funkcija1(uint8 len, uint8 data) je potrebno kreirati unit testove. Funkcija ne posjeduje pozive funkcija koje je potrebno stub-ovati i nije potrebno označavati klase ekvivalencije.

Jezik kojim se zadaje komanda za keiranje unit testova: 
  
function funkcija1(uint8 len, uint8 data)  
&nbsp;&nbsp;&nbsp;&nbsp;cases  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(0, 0) => TT_E_OK; 'there is no error',  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(256, 20) => TT_E_NOT_OK; 'parameter len is equal to 256',  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1, 256) => TT_E_NOT_OK; 'parameter data is equal to 256'      
end 

Unit testovi koji se dobiju na izlazu:

### 1)


The test case checks the behaviour of funkcija1 function in case there is no error.

{Test Specification}
1. Call funkcija1 function with the following arguments:
  * len = 0				
  * data = 0							
 2. Check expected results.

{Expected Results}
 Expected result is Passed
 1. funkcija1 function returns TT_E_OK.


```C
void UT_Testovi_funcija1_TC_00()
{
  /* Initializing argument 1 len */
  uint8 test_len = 0;
  /* Initializing argument 2 data */
  uint16 test_data = 0;
  {
    /* Tested function call */
    TtErrorType _return  = funkcija1( test_len, test_data);
    /* Post-condition check */
    CPPTEST_ASSERT_UINTEGER_EQUAL(TT_E_OK, _return);
  }
}
```

### 2)


The test case checks the behaviour of funkcija1 function in case parameter len is equal to 256.

{Test Specification}
1. Call funkcija1 function with the following arguments:
  * len = 256				
  * data = 20							
2. Check expected results.

{Expected Results}
Expected result is Passed
1. funkcija1 function returns TT_E_NOT_OK.

```C
void UT_Testovi_funcija1_TC_01()
{
  /* Initializing argument 1 len */
  uint8 test_len = 256;
  /* Initializing argument 2 data */
  uint16 test_data = 20;
  {
    /* Tested function call */
    TtErrorType _return  = funkcija1( test_len, test_data);
    /* Post-condition check */
    CPPTEST_ASSERT_UINTEGER_EQUAL(TT_E_NOT_OK, _return);
  }
}
```

### 3)


The test case checks the behaviour of funkcija1 function in case parameter data is equal to 256.

{Test Specification}
1. Call funkcija1 function with the following arguments:
  * len = 1				
  * data = 256						
2. Check expected results.

{Expected Results}
Expected result is Passed
1. funkcija1 function returns TT_E_NOT_OK.

```C
void UT_Testovi_funcija1_TC_02()
{
  /* Initializing argument 1 len */
  uint8 test_len = 1;
  /* Initializing argument 2 data */
  uint16 test_data = 256;
  {
    /* Tested function call */
    TtErrorType _return  = funkcija1( test_len, test_data);
    /* Post-condition check */
    CPPTEST_ASSERT_UINTEGER_EQUAL(TT_E_NOT_OK, _return);
  }
}
```

## Primjer br. 2:
  Za funkciju TtErrorType funkcija2(uint16 len, TtData* data) je potrebno kreirati unit testove. Funkcija posjeduje jedan poziv funkcije koju je potrebno stub-ovati i nije potrebno označavati klase ekvivalencije.

Jezik kojim se zadaje komanda za keiranje unit testova (cmplx označava da je u pitanju kompleksni tip, a pointer da je pokazivač u pitanju, stub upućuje na funkciju za stabovanje i calls na broj poziva stub-ovane funkicije koji se ocekuje):  
  
function funkcija2(uint8 len, TtData* data)  
&nbsp;&nbsp;&nbsp;&nbsp;cases  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(0, *\[status=1, enable=True]) => TT_E_OK; 'there is no error and value of enable a struct member of data is true',  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1, *\[status=1, enable=False]) => TT_E_OK; 'there is no error and value of enable a struct member of data is false',  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(256, *\[status=1, enable=True]) => TT_E_NOT_OK; 'parameter len is equal to 256',  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(1, *\[status=20, enable=True]) => TT_E_INVALID_PARAMETER; 'parameter status is invalid'   
&nbsp;&nbsp;&nbsp;&nbsp;stubs    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(someFunc, 1, CppTest_StubCallback_funkcija1_someFunc)  
end   

### Primjer prvog unit test-a koji bi se dobio na izlazu:


The test case checks the behaviour of funkcija1 function in case there is no error.

{Test Specification}
1. Define the data_example of TtData type with the following elements:
  * status = 1
  * enable = True
2. Stub function someFunc
1. Call funkcija1 function with the following arguments:
  * len = 0				
  * data = 0							
2. Check expected results.

{Expected Results}
Expected result is Passed
1. funkcija1 function returns TT_E_OK.
2. Function someFunc is called 1 time 

```C
void UT_Testovi_funcija1_TC_02()
{
   /* Functions called check */
   CPPTEST_EXPECT_NCALLS("someFunc", 1);
   /* Initializing argument 1 len */
   uint8 test_len = 0;
   /* Initializing argument 2 data */
   TtData data_example = { 
     .status = 1,
     .enable = True
   }
   TtData test_data = &data_example;
  
  CPPTEST_REGISTER_STUB_CALLBACK("someFunc", &CppTest_StubCallback_funkcija1_someFunc);
  {
    /* Tested function call */
    TtErrorType _return  = funkcija1( test_len, test_data);
    /* Post-condition check */
    CPPTEST_ASSERT_UINTEGER_EQUAL(TT_E_OK, _return);
  }
}
```


 
