# p2xmlGen
A tool which can generate equivalent XML(tag based) code for the given Python Code. 
p2xmlGen has been developed by updating the grammar file and tree generation process of lark parser library. 
python3.lark contains the grammar of python3, which can be parsed by the lark parser. 
Some new productions has been added in the grammar file, and renamed as updated_python3.lark. 
You can use it for XML based equivalent code of python.
We have just perform some updations as mentioned above in the grammar and lark parser code taken from the web resource: https://github.com/lark-parser/

# Installation Process:

Require python 3.5 or above.

1. Clone or Download from the Github.
2. Unzip the folder.
## From the ternimal
3. Jump to the p2xmlGen folder
4. $pip install updated_lark.zip  #Install updated Lark Parser. Have a look at https://github.com/lark-parser/ for more information.
   Now lark is installed.
5. test_data.py file is given which contains example python code.
6. How to Run:
   $python command_line.py <input.py> <output.xml>
 
XML generated code saved into <output.xml> file. Open the xml file in web browser for better visualization.
Based on requirement change the demo file. Keep the python3.lark file parallel to demo.py for simplicity.

# GUI Tool:

GUI tool is built using the PyQt library (https://riverbankcomputing.com/software/pyqt/intro). 
We have used an existing implementation (Notepad) of PyQt given at the following link: https://www.binpress.com/building-text-editor-pyqt-1/
Some updation performed in the source code to run our p2xmlGen through the existing implementation.

#### install PyQt:
$sudo apt-get install python-qt4.

Next, run the gui.py file from the commandline as follows:
$sudo pythongui.py
