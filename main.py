from quiz import Quiz


def main():

    while True:

        try:

            game = Quiz()

            game.start()

            break

        except KeyboardInterrupt:

            print("\n\nProgram Interrupted.")

            choice = input("Do you want to Exit? (Y/N): ").strip().upper()

            if choice == "Y":

                print("Goodbye!")

                break

        except Exception as e:

            print("\nUnexpected Error")

            print(e)

            break


if __name__ == "__main__":

    main()