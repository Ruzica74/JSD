# JSD
Jezici specificni za domen

# Primjer br. 1:
  Za funkciju TtErrorType funkcija1(uint8 len, uint8 data) je potrebno kreirati unit testove. Funkcija ne posjeduje pozive funkcija koje je potrebno stub-ovati i nije potrebno označavati klase ekvivalencije.

Jezik kojim se zadaje komanda za keiranje unit testova:
function funkcija1
par1 uint8 len
  value 0, 256, 1
par2 uint8 data
  value 0, 20, 256
expected TT_E_OK, TT_E_NOT_OK, TT_E_NOT_OK
  desc there is no error, parameter len is equal to 256, parameter data is equal to 256
EQ no

Unit testovi koji se dobiju na izlazu:

# 1)


The test case checks the behaviour of funkcija1 function in case there is no error.

{Test Specification}
1. Call funkcija1 function with the following arguments:
  * len = 0				
  * data = 0							
 2. Check expected results.

{Expected Results}
 Expected result is Passed
 1. funkcija1 function returns TT_E_OK.



	void UT_Testovi_funcija1_TC_00()
	{
	  uint8 test_len = 0;
	  uint16 test_data = 0;
		  {
		    TtErrorType _return  = funkcija1( test_len, test_data);
		    CPPTEST_ASSERT_UINTEGER_EQUAL(TT_E_OK, _return);
		  }
	}

2)

/**
 * The test case checks the behaviour of funkcija1 function in case parameter len is equal to 256.
 *
 * \field{Test Specification}
 * 1. Call funkcija1 function with the following arguments:
 *  * len = 256				
 *  * data = 20							
 * 2. Check expected results.
 * \endfield
 *
 * \field{Expected Results}
 * Expected result is Passed
 * 1. funkcija1 function returns TT_E_NOT_OK.
 * \endfield
 */

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

3)

/**
 * The test case checks the behaviour of funkcija1 function in case parameter data is equal to 256.
 *
 * \field{Test Specification}
 * 1. Call funkcija1 function with the following arguments:
 *  * len = 1				
 *  * data = 256						
 * 2. Check expected results.
 * \endfield
 *
 * \field{Expected Results}
 * Expected result is Passed
 * 1. funkcija1 function returns TT_E_NOT_OK.
 * \endfield
 */

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

# Primjer br. 2:
  Za funkciju TtErrorType funkcija2(uint16 len, TtData* data) je potrebno kreirati unit testove. Funkcija posjeduje jedan poziv funkcije koju je potrebno stub-ovati i nije potrebno označavati klase ekvivalencije.

Jezik kojim se zadaje komanda za keiranje unit testova (cmplx označava da je u pitanju komppleksni tip, a pointer da je pokazivač u pitanju, stub upućuje na funkciju za stabovanje i calls na broj poziva stub-ovane funkicije koji se ocekuje):
function funkcija2
par1 uint8 len
  value 0, 1, 256, 1
par2 cmplx pointer TtData data
  cmplx1 status, enable
  value1 1, True
  value2 1, False
  value3 1, True
  value4 20, True
stub1 someFunc calls 1 
  void CppTest_StubCallback_funkcija1_someFunc(CppTest_StubCallInfo* stubCallInfo, TtErrorType* __returnuint32, uint8 value){
  	CPPTEST_ASSERT_PTR_EQUAL(1, value);
  	*__return = TT_E_OK;
  }
expected TT_E_OK, TT_E_OK, TT_E_NOT_OK, TT_E_INVALID_PARAMETER
  desc there is no error and value of enable a struct member of data is true, there is no error and value of enable a struct member of data is false, parameter len is equal to 256, parameter status is invalid
EQ no


Primjer prvog unit test-a koji bi se dobio na izlazu:

/**
 * The test case checks the behaviour of funkcija1 function in case there is no error.
 *
 * \field{Test Specification}
 * 1. Define the data_example of TtData type with the following elements:
 *   status = 1
 *   enable = True
 * 2. Stub function
 * 1. Call funkcija1 function with the following arguments:
 *  * len = 0				
 *  * data = 0							
 * 2. Check expected results.
 * \endfield
 *
 * \field{Expected Results}
 * Expected result is Passed
 * 1. funkcija1 function returns TT_E_OK.
 * 2. Function someFunc is called 1 time with the following parameter:
 *  value = 1
 * \endfield
 */

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


 
