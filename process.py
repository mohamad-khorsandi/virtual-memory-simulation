from instruction import Instruction
from state import State
class Process:
    def __init__(self):
        self.id = None
        self.state = None
        self.inst_list = []

        self.PC = 0
        self.IR = None
        self.TMP = None
        self.ACC = None

    def create_process(self, id, file_name):
        self.id = id
        file = open(file_name, 'r')
        line = file.readline()

        while line:
            ins_type = line.split(' ')[0]
            ins_num = line.split(' ')[1]
            inst = Instruction(ins_type, float(ins_num), self)
            self.inst_list.append(inst)
            line = file.readline()
            
    def run_process(self):
        if self.state == State.blocked :
            return

        self.state = State.running

        self.inst_list[self.PC].run()

        self.state = State.ready
    
    def block_process(self):
        self.state = State.blocked
    
    def unblock_process(self):
        self.state = State.ready
    
    def show_context(self):
        print("Process ID : {}".format(self.id))
        print("Instruction Register : {}".format(self.IR).endswith("\n\n"))
        print("Accumulator : {}".format(self.ACC).endswith("\t\t"))
        print("Temp : {}".format(self.TMP))
        print("Program Counter : ".format(self.PC).endswith("\t\t"))
        print("State : {}".format(self.state.value))



