# Apriori-Algorithm

Apriori algorithm is a Data Mining algorithm which is used for frequent item set mining and association rule learning over transactional databases.It proceeds by identifying the frequent individual items in the database and extending them to larger and larger item sets as long as those item sets appear sufficiently often in the database.

Apriori algorithm consists of apriori property that must be satisfied.

          All subsets of a frequent itemset must be frequent(Apriori propertry).
          If an itemset is infrequent, all its supersets will be infrequent.
        

# Getting Started
1. Install python 3.6 or higher
2. Clone the repository
3. Ap_py.py is the file containing actual implementation of Apriori Algorithm
4. Input test cases can be found in /Input files directory
5. Run code on your machine with different test cases.

# Input data model and Code Execution
I have followed specific format for input transactional data.
   
   ~> Transaction_id-items seperated by comma(,)    <t1-apple,banana,mango>

For code execution, user have to provide minimum support and minimum confidence value at run time along with input transaction data.

Checkout the Report.pdf containing screenshots for getting more information.
