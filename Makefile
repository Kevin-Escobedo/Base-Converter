all: converter
converter: base_class.cpp base_convert.cpp
	g++ base_class.cpp -o base_class -std=c++11
clean:
	/bin/rm base_class
