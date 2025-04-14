def main():
    anton : int = 21 # Anton's age is given aa 21 years old
    beth : int  = 6 + anton # Beth is 6 years older than Anton
    chen : int  = 20 + beth # Chen is 20 years older than Beth
    drew : int = chen + anton # Drew is as old as Chen and Anton combined
    ethan : int = chen # Ethan is the same age as Chen

# print out the ages of each person
    print(f"Anton is {str(anton)} years old.")
    print(f"Beth is {str(beth)} years old.")
    print(f"Chen is {str(chen)} years old.")
    print(f"Drew is {str(drew)} years old.")
    print(f"Ethan is {str(ethan)} years old.")


if __name__ == "__main__":
    main()