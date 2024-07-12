AllowedVehiclesList = ['Ford F-150','Chevrolet Silverado','Tesla Cybertruck','Toyota Tundra','Nissan Titan']



while (True):
  print("********************************")
  print("AutoCountry Vehicle Finder v0.1")
  print("********************************")
  print("Please Enter one of the following numbers below from the following menu:")
  print(" ")
  print('1. PRINT all Authorized Vehicles')
  print('2. SEARCH for Authorized Vehicle')
  print('3. Exit')
  selection = input("Please enter your choice: ")
  if int(selection) == 1:
    print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for vehicles in AllowedVehiclesList:
      print(vehicles)
    continue
  if int(selection) == 2:
    vehicleChoice = input('Please Enter the full Vehicle name: ')
    if vehicleChoice in AllowedVehiclesList:
      print((vehicleChoice) + ' is an authorized vehicle')
    if vehicleChoice not in AllowedVehiclesList:
      print((vehicleChoice) + ' is not an authorized vehicle, if you received this in error please check the spelling and try again')
    continue
  if int(selection) != 3:
    print("Invalid Choice,Please select a valid choice from the menu")
    continue
  if int(selection) == 3:
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
    break

