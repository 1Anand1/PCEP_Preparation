class BatteryPowered:
  def battery_status(self):
    print("Battery at 80%")


class WiFiEnabled:
  def wifi_status(self):
    print("WiFi connected")


class Smartphone(BatteryPowered,WiFiEnabled):
  def device_info(self):
    print("Smartphone is ready to use")
