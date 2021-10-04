from bme68x import BME68X
import json

def read_conf(path: str):
    with open(path, 'rb) as conf_file:
        conf = [int.from_bytes(bytes([b]), 'little') for b in conf_file.read()]
        conf = conf[4:]
    return conf

def main():
    s = BME68X(0x77, 0)

    meat_n_cheese = read_conf('/home/pi/Desktop/DigitalNose/Algorithms/CheeseVsMeat/2021_08_09_17_10_bsec_NormalAi_Meat_Cheese_2_0_6_1.config')

    default_conf = read_conf('/home/pi/Desktop/DigitalNose/BSEC_2.0.6.1_Generic_Release_04302021/config/bsec_sel_iaq_33v_4d/2021_04_29_02_51_bsec_h2s_nonh2s_2_0_6_1 .config')

    air_meat_cheese = read_conf('/home/pi/Desktop/DigitalNose/Algorithms/AirMeatCheese/2021_09_27_19_24_bsec_NormalAi_Meat_Cheese_2_0_6_1.config')

    print(f'SET BSEC CONF {s.set_bsec_conf(meat_n_cheese)}')
    # print(f'SET BSEC CONF {s.set_bsec_conf(air_meat_cheese)}')
    # print(f'SET BSEC CONF DEFAULT SELECTIVITY {s.set_bsec_conf(default_conf)}')

    BSEC_SAMPLE_RATE_HIGH_PERFORMANCE = 0.055556
    BSEC_SAMPLE_RATE_LP = 0.33333

    # print(f'SUBSCRIBE STANDARD OUTPUTS {s.set_sample_rate(BSEC_SAMPLE_RATE_HIGH_PERFORMANCE)}')
    print(f'SUBSCRIBE GAS ESTIMATES {s.subscribe_gas_estimates(3)}')

    # print(f'SET HEATER PROFILE {s.set_heatr_conf(1, [320, 100, 100, 100, 200, 200, 200, 320, 320, 320], [150, 150, 150, 150, 150, 150, 150, 150, 150, 150], 2)}')
    print(f'INIT BME68X {s.init_bme68x()}')

    print('\n\nSTARTING MEASUREMENT\n')

    while(True):
        # print(s.get_bsec_data())
        try:
            data = s.get_digital_nose_data()
        except Exception as e:
            print(e)
            main()
        if data:
            # for entry in s.get_digital_nose_data():
            entry = data[-1]
            print(f'NORMAL AIR {entry["gas_estimate_1"]}\nMEAT {entry["gas_estimate_2"]}\nCHEESE {entry["gas_estimate_3"]}')
            print()

            NormalAir = "{:.1%}".format(entry["gas_estimate_1"])
            Meat = "{:.1%}".format(entry["gas_estimate_2"])
            Cheese = "{:.1%}".format(entry["gas_estimate_3"])

            d = {
                'NormalAir': NormalAir,
                'Meat': Meat,
                'Cheese': Cheese,
            }

            with open('/home/pi/Desktop/DigitalNose/data.json', 'w') as file:
                json.dump(d, file)



if __name__ == '__main__':
    main()

