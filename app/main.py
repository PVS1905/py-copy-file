def copy_file(command: str) -> None:
    file1 = command.split()[1]
    file2 = command.split()[2]

    if not file1 == file2:
        with open(file1, "r") as file_in, open(file2, "w") as file_out:
            file_out.write(file_in.read())
