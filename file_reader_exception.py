import logging
import time

logging.basicConfig(filename="error_log.txt", level=logging.ERROR, format="%(asctime)s:%(levelname)s:%(message)s")
def read_file():
    filename = "file.txt"
    while True:  
        try:

            with open(filename, "r") as file:
                content = file.readlines()
                if not content:
                    raise ValueError("the file is empty!" )
                for line in content:
                    print(line.strip())
            print("\n File read succesfully!\n")
            break

        except FileNotFoundError as e:
            print(f"Error: {e}")
            logging.error(e)
            retry = input("do you want to retry? (yes/no): ").strip().lower()
            if retry != "yes":
                print("exiting program: ")
                break

        except PermissionError:
            err_msg = f"error: permission denied to read '{filename}'!"
            print(err_msg)
            logging.error(err_msg)
            break
            
        except ValueError as e:
            print(f"Warning: {e}")
            logging.warning(e)
            break

        except KeyboardInterrupt:
            print("\n process interrupted exiting...")
        except Exception as e:
            err_msg = f"an unexpected error occured: {e}"
            print(err_msg)
            logging.error(err_msg)
            break
        time.sleep(1)

read_file()