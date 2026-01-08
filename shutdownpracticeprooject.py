def shutdown():
    print("System is shutting down...")
    answer= input("\nSome of your apps are open. Would you like to close them and continue? Enter yes to continue:  ")
    if answer == 'yes':
        print("\nApps have been successfully closed.")
        print("System shutting down...")
        print("Shutdown complete.\n")
    elif answer == 'no':
        print("\nCannot complete system shutdown without closing all apps. Please try again.")
        exit()
    else:
        print("\nError. Please try again later.\n")
        exit()

shutdown()