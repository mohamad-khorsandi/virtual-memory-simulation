from state import State
class Instruction:
    def __int__(self, ins_type, ins_num, process):
        self.ins_type = ins_type
        self.ins_num = ins_num
        self.process = process

    def run(self):

        
        if self.ins_type == "load":
            self.process.IR = self.ins_type
            self.process.TMP = self.ins_num
            self.process.ACC = self.ins_num
        elif self.ins_type == "add":
            self.process.IR = self.ins_type
            self.process.TMP = self.ins_num
            self.process.ACC += self.process.TMP
        elif self.ins_type == "sub":
            self.process.IR = self.ins_type
            self.process.TMP = self.ins_num
            self.process.ACC -= self.process.TMP
        elif self.ins_type == "mul":
            self.process.IR = self.ins_type
            self.process.TMP = self.ins_num
            self.process.ACC *= self.process.TMP
        

        self.process.PC += 1
        
        


        