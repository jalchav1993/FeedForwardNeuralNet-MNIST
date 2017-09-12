The interface is coded in python and it consists of a module for the model, mathematical calculations, and a module for the control which reads inputs and converts them into the “one-hot” encoding. The file called “filehandler.py” is the control, this module is loaded with the methods needed to read and understand the MNIST database; these methods output objects that are easier to understand and manage using the python application programming interface. Python was chosen because of its extensive application programming interface (API) with convenient methods such as max () (maximum integer of a list) or exp () (exponential numbers of base e). The API also provides robust list interface, split () was used to quickly encode the comma separated values (CSV) into list objects. The file called “Math.py” provides the model for the network, these are the linear algebra operations that each layer needs to perform in order to process the input and generate an output. These are matrix of size i*j multiplication with a vector of size j, addition of two vectors each of size j, a rectifier method that provides logic processing for each layer and a Sigmund corrector. The lists are rectified each time, the logic of the rectifier is represented in the following table: 
Negative value
zero
Positive value
one
