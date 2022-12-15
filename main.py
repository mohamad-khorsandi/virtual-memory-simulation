from process import Process

resource_file = "resource"
commands_file = resource_file + "/commands.txt"
proc_list = {}

def main():
    file = open(commands_file, 'r')
    cmd_args = file.readline().split()
    loop_counter = 0
    while cmd_args:
        print("loop: " + str(loop_counter) + " -----------------------------------------------------------------")
        loop_counter += 1
        cmd = cmd_args[0]
        proc_id = cmd_args[1]


        if cmd == "create_process":
            new_process = Process()
            proc_list[proc_id] = new_process
            inst_file = resource_file + "/" + cmd_args[2]
            new_process.create_process(proc_id, inst_file)

        elif proc_id not in proc_list :
            print("process is not valid")

        elif cmd == "run_process" :
            proc_list[proc_id].run_process()

        elif cmd == "block_process" :
            proc_list[proc_id].block_process()

        elif cmd == "unblock_process":
            proc_list[proc_id].unblock_process()

        elif cmd == "show_context":
            proc_list[proc_id].show_context()


        cmd_args = file.readline().split()


if __name__ == '__main__':
    main()
