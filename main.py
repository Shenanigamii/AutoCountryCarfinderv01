#list of available vehicles for sale
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']


while True:
  #formatting of prompt
  print("********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print("Please Enter the following number below from the following menu:\n")

  #client response options
  userInput = input("1. PRINT all Authorized Vehicles\n2. Exit\n")

#output
  #if user typed "1" 
  if userInput == '1':
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for model in AllowedVehiclesList:
        print(model)
  #if user typed 2
  elif userInput == '2':
      print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
  #if user input blank
  else:
      print("You have failed.  Try again.")
  break