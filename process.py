from instruction import Instruction
class Process:
    def create_process(self, id, file_name):
        self.id = id
        file = open(file_name, 'r')
        line = file.readline()
        while line:
            line = file.readline()
            ins_type = line.split(' ')[0]
            ins_num = line.split(' ')[1]
            ins = Instruction(ins_type, ins_num, self)
            print(line)
        # self.ins_list

