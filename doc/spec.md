# Transfer of Account Transactions to Disk

**Spanish Banking Association**  
**Banking Procedures and Standards Series No. 43**  
Madrid – November 2003

---

## Index

1. [Definition and Characteristics of the Service](#1-definition-and-characteristics-of-the-service)
   - [1.1 Payment of salaries and pensions](#11-payment-of-salaries-and-pensions)
   - [1.2 Other orders for transfers and issuing of bank cheques](#12-other-orders-for-transfers-and-issuing-of-bank-cheques)
2. [General Characteristics of Magnetic Media](#2-general-characteristics-of-magnetic-media)
   - [2.1 Medium](#21-medium)
   - [2.2 Organization of medium](#22-organization-of-medium)
   - [2.3 File structure](#23-file-structure)
   - [2.4 Method of sending medium](#24-method-of-sending-medium)
3. [Annexes](#annexes)
   - [Annex 1: Design and Description of Records](#annex-1-design-and-description-of-records)
   - [Annex 2: Description of the Client Account Code and Control Digits Calculation and Branch Codes](#annex-2-description-of-the-client-account-code-and-control-digits-calculation-and-branch-codes)

---

## INTRODUCTION

To satisfy the demands of certain companies wishing to receive account transactions from their Banks by electronic means, the Interbank Technical Committee produced a standardized current account statement on a magnetic medium, the use of which was recommended to the whole banking community in Supreme Banking Council Circular No. 12/82 of 27 February 1982, the first version of this Pamphlet No. 43 being issued in May 1982.

Now, with the expanding computerized infrastructure of the Banks' operating networks, new current account services have been introduced with a more specific focus for companies.

The Interbank Technical Committee has therefore produced an updated version of this pamphlet on "standardized current account information" covering three types of standardized information, which respond to three types of service or use of the bank operating network.

This issue was approved by the Supreme Banking Council at its Plenary Meeting held on 28 April 1986 (Supreme Banking Council Circular No. 31/86 of 12 May 1986).

---

## I. Types of Service and Use

### **First:**

This refers to the general and ordinary operation of the current account, where transactions are executed in the Branch of the bank where the account is domiciled.

The Bank produces the current account statement which includes, as well as the specific item codes of the Bank itself, the transfer item codes shown in Annex, for use by all the Credit Agencies.

This is basically the form already applied by this pamphlet 43 in its May 1982 version.

### **Second:**

This refers to the current account which, subject to the contract and special conditions agreed between both parties, may receive executed transactions from different Branches of the same Bank.

The Bank provided the current account statement and, in addition to specifying all the data included in the first type, provides information of the branch in which the transaction entry is executed.

### **Third:**

This is for when a service or special data capture and information application, or additional references on individual transactions related to a current account, are executed from different branches of the same Bank.

The Bank produces the current account statement and, in addition to specifying the data included in the first type above, provides information on the branch in which the transaction entry is executed and the references and additional information agreed and standardized with the company holding the account.

---

## II. Magnetic Support

### **1. File Characteristics**

- **Recording density:** 1,600 b.p.i.
- **Labels:** Without head or end labels.
- **Tape marking:** No marking of tape at beginning. With marking of tape at end.
- **Block:** 100 records.
- **Record length:** 80 characters.
- **Code:** EBCDIC
- **Label on outside (minimum data):** remitting Bank, code, receiving client, creation date, account number.

### **2. Records contents**

There will be 5 record types:

- Account header.
- Main transactions.
- Where appropriate, item accessories, to a maximum of 5 optional records.
- End of account.
- End of file.

The same magnetic medium may contain information on more than one account, which is why the record sequence "Account Header", "Main Transactions", with their possible "Item Accessories" (when agreed) and "End of Account", will be repeated as many times on the magnetic tape as there are accounts.

The optional records "Item Accessories", to a maximum of 5 records, each contain fields with a length of 38 positions. If the two fields are not needed, the one not used will be left blank.

These optional records are there, whenever required and only when expressly and mutually agreed, for specifying in alphanumerical characters the numerical field "own item" or transfer code automatically assigned, without the need for the Credit Agency to input data, in order to replace the printed information currently in use.

---

## ANNEXES

### **ANNEX 1. FILE FORMAT FOR TRANSFER OF ACCOUNT TRANSACTIONS TO DISK**

#### **00-FILE HEADER RECORD**

| Field Description                                                         | Initial Position | Length | Record Type |
| :------------------------------------------------------------------------ | :--------------- | :----- | :---------- |
| Record Code, 2 positions "00"                                             | 1                | 2      | Numerical   |
| Bank Code used in the file, 4 positions                                   | 3                | 4      | Numerical   |
| Accounting Date of the period to which the information corresponds YYMMDD | 7                | 6      | Numerical   |
| Free: 68 positions                                                        | 13               | 68     |             |

#### **11-ACCOUNT HEADER RECORD**

| Field Description                                                                                                                                                       | Initial Position | Length | Record Type    |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------- | :----- | :------------- |
| Record Code, "11"                                                                                                                                                       | 1                | 2      | Numerical      |
| Bank Code used in the file                                                                                                                                              | 3                | 4      | Numerical      |
| Branch Code of where the account is held                                                                                                                                | 7                | 4      | Numerical      |
| Account No.                                                                                                                                                             | 11               | 10     | Numerical      |
| Start Date of the period to which the information corresponds YYMMDD                                                                                                    | 21               | 6      | Numerical      |
| End Date of the period to which the information corresponds YYMMDD                                                                                                      | 27               | 6      | Numerical      |
| Initial Balance Code; initial field sign: 1=debit, 2=credit                                                                                                             | 33               | 1      | Numerical      |
| Initial Balance Amount of the account (balance at the end of the previous day, which must coincide with the final balance of the previous information) 2 decimal places | 34               | 14     | Numerical      |
| Currency Category, numerical code                                                                                                                                       | 48               | 3      | Numerical      |
| Information Mode Code (in this case it is: 3)                                                                                                                           | 51               | 1      | Numerical      |
| Abbreviated Name (of the Client holding the Account)                                                                                                                    | 52               | 26     | Alphanumerical |
| Client Code                                                                                                                                                             | 78               | 3      | Numerical      |

#### **22-MAIN TRANSACTIONS RECORD**

| Field Description                                                       | Initial Position | Length | Record Type    |
| :---------------------------------------------------------------------- | :--------------- | :----- | :------------- |
| Record Code, "22"                                                       | 1                | 2      | Numerical      |
| Free (filled in with spaces. It may, exceptionally, show the bank code) | 3                | 4      | Alphanumerical |
| Branch Code of origin (where the entry is executed)                     | 7                | 4      | Numerical      |
| Transaction Date YYMMDD                                                 | 11               | 6      | Numerical      |
| Value Date YYMMDD                                                       | 17               | 6      | Numerical      |
| Shared Item                                                             | 23               | 2      | Numerical      |
| Own Item (that given by each Bank to its transactions)                  | 25               | 3      | Numerical      |
| Debit or Credit Code: 1=Debit Entries, 2=Credit Entries                 | 28               | 1      | Numerical      |
| Amount (of Entry, 12 full number positions and 2 decimal places)        | 29               | 14     | Numerical      |
| Document No.                                                            | 43               | 10     | Numerical      |
| Reference 1                                                             | 53               | 12     | Numerical      |

#### **23-ADDITIONAL RECORDS FOR OPTIONAL ITEMS (maximum of 5)**

| Field Description                                                                                                       | Initial Position | Length | Record Type    |
| :---------------------------------------------------------------------------------------------------------------------- | :--------------- | :----- | :------------- |
| Record Code, "23"                                                                                                       | 1                | 2      | Numerical      |
| Data Code: 01 for the first additional record, 02 for the second, 03 for the third, 04 for the fourth, 05 for the fifth | 3                | 2      | Numerical      |
| Item (First Additional Item Field)                                                                                      | 5                | 38     | Alphanumerical |
| Item (Second Additional Item Field)                                                                                     | 43               | 38     | Alphanumerical |

#### **33-END OF ACCOUNT RECORD**

| Field Description                     | Initial Position | Length | Record Type |
| :------------------------------------ | :--------------- | :----- | :---------- |
| Record Code, "33"                     | 1                | 2      | Numerical   |
| Bank Code used in the file            | 3                | 4      | Numerical   |
| Branch Code                           | 7                | 4      | Numerical   |
| Account No.                           | 11               | 10     | Numerical   |
| No. of Debit Entries                  | 21               | 5      | Numerical   |
| Total Debit Amounts                   | 26               | 14     | Numerical   |
| No. of Credit Entries                 | 40               | 5      | Numerical   |
| Total Credit Amounts                  | 45               | 14     | Numerical   |
| Final Balance Code: 1=Debit, 2=Credit | 59               | 1      | Numerical   |
| Final Balance Amount                  | 60               | 14     | Numerical   |
| Currency Code                         | 74               | 3      | Numerical   |
| Free                                  | 77               | 4      |             |

#### **88-END OF FILE RECORD**

| Field Description                                                                                              | Initial Position | Length | Record Type |
| :------------------------------------------------------------------------------------------------------------- | :--------------- | :----- | :---------- |
| Record Code, "88"                                                                                              | 1                | 2      | Numerical   |
| Nines (filled in with nines)                                                                                   | 3                | 18     | Numerical   |
| Record No. (Total No. of Records contained in the File, excluding the record itself and record 00 File Header) | 21               | 6      | Numerical   |
| Free                                                                                                           | 27               | 54     |             |

---

### **ANNEX 2. DESCRIPTION OF THE CLIENT ACCOUNT CODE AND CONTROL DIGITS CALCULATION AND BRANCH CODES**

The Client Account Code (CCC) is made up of a set of 20 numerical characters, which relate to the following data:

- **Agency Code:** 4 Digits
- **Branch Code:** 4 Digits
- **Control Digits:** 2 Digits
- **Account Number:** 10 Digits

The Agency and Branch Codes, as well as the Account Number, will be used with all their digits filled in with zeros to the left.

The first Control Digit verifies the Agency and Branch Codes, and the second, the Account Number.

To obtain each control digit, the **modulus 11** is used: The sum of the products obtained from multiplying each of the figures contained in the elements by assigned weights, is divided by 11; the remainder of said Division is subtracted from 11, and the result is the Control Digit, with the following exceptions: if it is 10, it will be taken as 1; if it is 11, zero.

**The Weights to use are:**

- Units: 6
- Tens: 3
- Hundreds: 7
- Thousands: 9
- Tens of thousands: 10
- Hundreds of thousands: 5
- Millions: 8
- Tens of millions: 4
- Hundreds of millions: 2
- Thousands of millions: 1

#### **Example: To verify the CCC of account 6/789-0 of Branch 345 of Agency 12:**

**First Control Digit (Agency and Branch)**

For calculation purposes: `00120345`

| Position              | Digit | Weight | Product |
| :-------------------- | :---- | :----- | :------ |
| Units                 | 5     | 6      | 30      |
| Tens                  | 4     | 3      | 12      |
| Hundreds              | 3     | 7      | 21      |
| Thousands             | 0     | 9      | 0       |
| Tens of thousands     | 2     | 10     | 20      |
| Hundreds of thousands | 1     | 5      | 5       |
| Millions              | 0     | 8      | 0       |
| Tens of millions      | 0     | 4      | 0       |

**SUM** = 88

The remainder of 88 divided by 11 is 0, which when subtracted from 11, gives us 11, which is why the Control Digit is **0**.

---

**Second Control Digit (Account Number)**

For calculation purposes: `0000067890`

| Position              | Digit | Weight | Product |
| :-------------------- | :---- | :----- | :------ |
| Units                 | 0     | 6      | 0       |
| Tens                  | 9     | 3      | 27      |
| Hundreds              | 8     | 7      | 56      |
| Thousands             | 7     | 9      | 63      |
| Tens of thousands     | 6     | 10     | 60      |
| Hundreds of thousands | 0     | 5      | 0       |
| Millions              | 0     | 8      | 0       |
| Tens of millions      | 0     | 4      | 0       |
| Hundreds of millions  | 0     | 2      | 0       |
| Thousands of millions | 0     | 1      | 0       |

**SUM** = 206

206 divided by 11 gives a remainder of 8 which, when subtracted from 11, gives **3**.

**The full CCC is therefore:** `0012034503 0000067890`
