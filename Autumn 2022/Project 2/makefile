CXX = g++
CXXFLAGS = --std=c++14 -Wall
OBJ = obj
BIN = bin
$(info $(shell mkdir -p $(OBJ)))
$(info $(shell mkdir -p $(BIN)))

test_ArrayList_SRCs = test_array_list.cpp array_list.cpp
test_LinkedList_SRCs = test_linked_list.cpp linked_list.cpp
LinkedArrayList_SRCs = array_list.cpp linked_array_list.cpp

execute: LinkedArrayList.exe
	$(BIN)/$^

test: test_LinkedList.exe test_ArrayList.exe
	$(BIN)/test_ArrayList.exe
	$(BIN)/test_LinkedList.exe

test_ArrayList.exe: $(patsubst %.cpp, $(OBJ)/%.o, $(test_ArrayList_SRCs))
	$(CXX) $(CXXFLAGS) $^ -o $(BIN)/$@

test_LinkedList.exe: $(patsubst %.cpp, $(OBJ)/%.o, $(test_LinkedList_SRCs))
	$(CXX) $(CXXFLAGS) $^ -o $(BIN)/$@

LinkedArrayList.exe: $(patsubst %.cpp, $(OBJ)/%.o, $(LinkedArrayList_SRCs))
	$(CXX) $(CXXFLAGS) $^ -o $(BIN)/$@

$(OBJ)/%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $^ -o $@

clean:
	rm $(OBJ)/* $(BIN)/*
