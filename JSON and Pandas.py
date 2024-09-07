import pandas as pd
import json


Vehicles = {"cars": ["Honda", "Suzuki", "Toyota", "Kia", "Sazgar"], "Prices": [5000000, 3000000, 6000000, 3500000, 8000000]
          }

# list = {[12, 35, 55, 74, 31]: [10,25,58,56,87]}

Timemenu = {"Morning": "breakfast", "Night": "Supper", "Evening": "dinner"}

json_data = json.dumps(Timemenu)
print(json_data)

x = pd.DataFrame(Vehicles)
# y = pd.DataFrame(list)
# z = pd.DataFrame(Nimra)

# print(x)
# print(y)
# print(z)

# a = pd.DataFrame(Vehicles)

Jaanu = [{
  "pipettingProfileType": "SerialDilution",
  "userGuid": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "string",
  "content": "{\"Aspirate\":{\"Tip\":{\"Value\":1,\"Position\":\"BelowLiquidSurface\",\"Change\":\"Always\",\"ReturnToCaddy\":false,\"Detection\":\"Collision\",\"Mode\":null},\"Mixing\":{\"Enabled\":false,\"Volume\":{\"Value\":50.0,\"Unit\":\"AspiratePercentageVolumeUnit\"},\"Cycle\":3,\"TipPosition\":\"Automatic\",\"Tracking\":\"DLLT\",\"TipPositionValue\":1,\"TipPositionUnit\":\"BelowLiquidSurface\",\"TipPositionBottomDetection\":\"Collision\"},\"Optimization\":{\"EnableTrailingAirGap\":false,\"AirGapVolume\":0,\"EnableOverAspirate\":false,\"ExtraVolume\":0},\"Advanced\":{\"EnableALT\":true,\"EnableDLLT\":true,\"PipettingSpeed\":100,\"MixingSpeed\":100}},\"Dispense\":{\"Tip\":{\"Value\":1,\"Position\":\"BelowLiquidSurface\",\"Detection\":\"Collision\"},\"Mixing\":{\"Enabled\":false,\"Volume\":{\"Value\":50.0,\"Unit\":\"DispensePercentageVolumeUnit\"},\"Cycle\":3,\"TipPosition\":\"Automatic\",\"Tracking\":\"DLLT\",\"TipPositionValue\":1,\"TipPositionUnit\":\"BelowLiquidSurface\",\"TipPositionBottomDetection\":\"Collision\"},\"Optimization\":{\"DispenseAtSideWell\":false,\"EnableTimedPurge\":true,\"EnablePurgeVolume\":true,\"PurgeVolume\":{\"Mode\":\"Automatic\",\"Value\":0,\"OffsetPosition\":0},\"EnableTipTouchOff\":false,\"TouchOffOption\":{\"Mode\":\"Right\",\"Delay\":0},\"EnableMultiDispense\":false},\"Advanced\":{\"EnableALT\":true,\"EnableDLLT\":true,\"PipettingSpeed\":100,\"MixingSpeed\":100},\"DispenseFirstMount\":true},\"Name\":null,\"ID\":0,\"UID\":\"00000000-0000-0000-0000-000000000000\",\"Type\":\"RegularTransfer\"}",
  "folderType": "PipettingProfile",
  "isDefault": "true"
}]

# df = pd.DataFrame(Jaanu)
# print(df)


# # df.to_csv("friends.csv")
# x.to_csv("friends1.csv")
# df.to_csv("Nimra.csv")
# y.to_csv("fileextention.csv", index=["55","56","57","58","59"])
# print(z.tail(2))
# y.describe()





