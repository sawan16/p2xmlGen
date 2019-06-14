# p2xmlGen
A tool which can generate equivalent XML(tag based) code for the given Python Code. 
p2xmlGen has been developed by updating the python3.lark and tree generation process of lark parser library. 
python3.lark contains the grammar of python3, which can be parsed by the lark parser. 
Some new productions has been added in the grammar file and renamed to updated_python3.lark.
You can use it for generating the XML based equivalent code of the python source code.
We have just perform some updations as mentioned above in the grammar and lark parser code taken from the web resource: https://github.com/lark-parser/

# Installation Process:

Require python 3.5 or above.

1. Clone or Download from the Github.
2. Unzip the folder.

## From the ternimal
3. Jump to the p2xmlGen folder
4. $pip install Updated_lark.zip  #Install Updated Lark Parser. Have a look at https://github.com/lark-parser/ for more information.
   Now lark is installed.
5. test_data.py file is given which contains example python code.
6. How to Run:
   $python command_line.py <input.py> <output.xml>
   
 ## Using the GUI Tool
 
XML generated code saved into xml_data.xml file. Open the xml file in web browser for better visualization.
Based on requirement change the demo file. Keep the python3.lark file parallel to demo.py for simplicity.
