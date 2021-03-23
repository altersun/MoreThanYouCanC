
EXE := "XMarksTheSpot.exe"
OBJS = $(patsubst ./%.c,./%.o,$(wildcard ./*.c))
OBJS += $(patsubst ./%.cpp,./%.opp,$(wildcard ./*.cpp))
$(info $(OBJS))

.PHONY: all clean derp
all: $(EXE)

run: $(EXE)
	@./$(EXE)

$(EXE): $(OBJS)
	@echo 'Linking source file(s) $(OBJS) together into $@...'
	@$(CXX) -o "$@" $(OBJS)
	@echo "Built $@"

# Build cpp
%.opp: %.cpp 
	@echo 'Building source file $<...'
	@$(CXX) --std=c++2a -g -c -o "$@" "$<" 
	@echo 'Built $@'
	@echo

# Build c
%.o: %.c 
	@echo 'Building source file $<...'
	@$(CC) -std=gnu17 -g -c -o "$@" "$<"
	@echo 'Built $@'
	@echo

clean:
	@rm -f *.o* *.exe	
	@echo "All clean!"

