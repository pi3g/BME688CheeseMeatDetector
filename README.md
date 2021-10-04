# Cheese Meat Detector Example
### Example for BME688 sensor and RaspberryPi to distinguish cheese :cheese: and meat :bacon:
### published by pi3g e.K. under MIT license

## How to setup and run the example
| Step | Command |
| ---- | ------- |
| clone BME688CheeseMeatDetector repository | `git clone https://github.com/pi3g/BME688CheeseMeatDetector.git` |
| download the BSEC 2.0.6.1 package from the BOSCH website (you need to accept the license) | `none` |
| replace the BSEC_2.0.6.1_Generic_Release_04302021 placeholder directory by the BSEC 2.0.6.1 package | `sudo unzip path/to/BSEC_2.0.6.1_Generic_Release_04302021.zip -d path/to/BME688CheeseMeatDetector/bme68x-extension` |
| build and install the bme68x python extension | `pip3 install -e path/to/BME688CheeseMeatDetector/bme68x-extension` |
| install guizero (dependency) | `pip3 install guizero` |
| make sure the bme688 sensor is connect (should see 0x77) | `i2cdetect -y 1` |
| run get_data.py | `python3 path/to/BME688CheeseMeatDetector/get_data.py` |
| run gas_estimates_gui.py (optional) | `python3 path/to/BME688CheeseMeatDetector/gas_estimates_gui.py ` |

## Explanation
This example is using a pretrained algorithm by pi3g to differenciate normal air, meat and cheese.
The get_data.py utilises the bme68x python module to read the sensor data and calculate the probability percentages for each class.
The results are written to data.json.
Optionally you can run the gas_estimates_gui.py script to read data.json and display the results in a fullscreen application.
Leave the application via Alt+F4.
To collect data for the algorithm we put the specimens into plastic boxes with a lid.
This means the algorithm works best if you put the sensor and the specimen into a box or any relativly air tight container.

## Contact
For questions or bug reports send an E-Mail to nathan@pi3g.com
